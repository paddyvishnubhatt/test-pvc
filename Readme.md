# Download git and use it to clone this repo

1. Download k8s cluster manager e.g. Docker
2. Docker on a laptop is best to start with to get you commands to create images and manage them
3. Download kubectl, kops, kubeadm to manage k8s cluster and apps (kops - if youre using AWS, GCE or external cloud infra, else kubectl will do)
4. Some of the commands are built for zsh (but w/ a few tweaks can work w/ bash also)

#####################################################################################################

# Functionally test app
python app/main.py 

curl http://localhost:5000

# Build the docker image for main-python
docker build -f docker/Main_Dockerfile -t nfs-main-python:latest .

# Build the docker image for get-python
docker build -f docker/Get_Dockerfile -t get-python:latest .

# Build the docker image for roll-python
docker build -f docker/Roll_Dockerfile -t roll-python:latest .

# Build the docker image for reset-python
docker build -f docker/Reset_Dockerfile -t reset-python:latest .

# List the image
docker image ls

# Test image
docker run -p 5001:5000 main-python

# Remove image
docker image rm -f main-python 

#####################################################################################################

# Create vol
kubectl apply -f k8s/pv-vol.yaml  

# Create claim
kubectl apply -f k8s/pv-claim.yaml

# Deploy main-py
kubectl apply -f k8s/nfs-main-py.yaml

# Launch pod to test pv
kubectl apply -f k8s/pv-test.yaml 

# Launch pod for get counter
kubectl apply -f k8s/get-py.yaml

# Launch pod for roll counter
kubectl apply -f k8s/roll-py.yaml

# Launch pod for reset counter
kubectl apply -f k8s/reset-py.yaml

# Start service for main
kubectl apply -f k8s/service.yaml

# Start service for get counter
kubectl apply -f k8s/get-service.yaml

# Start service for roll counters
kubectl apply -f k8s/roll-service.yaml

# Start service for reset counter
kubectl apply -f k8s/reset-service.yaml


#####################################################################################################
# Test app  this will get the counters
http://localhost:5000

# Get Counters
curl http://localhost:5000
curl http://localhost:5000/counter/main
curl http://localhost:5000/counter/get

# Roll Counters
curl -X PUT http://localhost:8000/counter/roll/roll
curl -X PUT http://localhost:5000/counter/roll

# Reset Counters
curl -X PUT http://localhost:7000/counter/reset/reset
curl -X PUT http://localhost:5000/counter/reset

# use pv-test to launch/exec shell and check counters

kubectl exec -it dataaccess /bin/sh

# Test by bouncing/deleting pods using kubectl or mgmnt console 

kubectl pod <> 

# New pods will reconnect and continue counting from before

#####################################################################################################
# Creates mgmtn console
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.4.0/aio/deploy/recommended.yaml


# Creates account/access
kubectl create clusterrolebinding serviceaccounts-cluster-admin --clusterrole=cluster-admin --group=system:serviceaccounts 

# Browser/UI 
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/.

# This will start the mmgnt console
kubectl proxy

# Get TOKEN to log into above
APISERVER=$(kubectl config view --minify | grep server | cut -f 2- -d ":" | tr -d " ")
SECRET_NAME=$(kubectl get secrets | grep ^default | cut -f1 -d ' ')
TOKEN=$(kubectl describe secret $SECRET_NAME | grep -E '^token' | cut -f2 -d':' | tr -d " ")
echo $TOKEN

#####################################################################################################
# W/ NFS
#####################################################################################################

# Setup NFS Server (ubuntu)
ssh testuser@10.0.0.228/testuser (this has sudo)
/etc/exports
>>>/srv/data     *(rw,fsid=0,async,no_subtree_check,no_auth_nlm,insecure,no_root_squash)
exportfs -ra

# Setup NFS server (raspberry pi)

ssh pi@10.0.0.52/<usual> (this has sudo)
/etc/exports
>>>/srv/data     *(rw,fsid=0,async,no_subtree_check,no_auth_nlm,insecure,no_root_squash)
exportfs -ra

# Raspberry pi - get buster
/etc/apt/sources.list
deb http://raspbian.raspberrypi.org/raspbian/ buster main contrib non-free rpi
deb http://archive.raspberrypi.org/debian/ buster main

# Install/setup NFS server on raspberry pi
apt update
apt full-upgrade
apt-get install nfs-kernel-server
systemctl start nfs-kernel-server.service

# Test nfs mount from MAC
 mount  -t nfs -o resvport,nfsvers=4 10.0.0.228:/srv/data mnt/data

# Setup K8s w/ NFS mounts
kubectl apply -f k8s/nfs-pv-vol.yaml 
kubectl apply -f k8s/nfs-pv-claim.yaml 
kubectl apply -f k8s/nfs-pv-test.yaml

# Test NFS (make sure k8s test pod is able to see the mount point)
kubectl exec -it nfs-dataaccess /bin/sh

# Test app like above
curl http://localhost:5000
cat /mnt/data/counter.txt