# Download git and use it to clone this repo

1. Download k8s cluster manager e.g. Docker
2. Docker on a laptop is best to start with to get you commands to create images and manage them
3. Download kubectl, kops, kubeadm to manage k8s cluster and apps (kops - if youre using AWS, GCE or external cloud infra, else kubectl will do)
4. Some of the commands are built for zsh (but w/ a few tweaks can work w/ bash also)

#####################################################################################################

# Build the docker image for python
docker build -f docker/Dockerfile -t main-python:latest .

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
kubectl apply -f k8s/main-py.yaml

# Launch pod to test pv
kubectl apply -f k8s/pv-test.yaml 


#####################################################################################################
# Test app
http://localhost:5000

# This will increment counter by 10 whenever the above is relaunched/refreshed.
curl http://localhost:5000

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