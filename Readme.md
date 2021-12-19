
1. Download k8s cluster manager e.g. Docker
2. Docker on a laptop is best to start with to get you commands to create images and manage them
3. Download kubectl, kops, kubeadm to manage k8s cluster and apps
4. Download git
5. Some of the commands are built for zsh (but w/ a few tweaks can work w/ bash also)

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

kubectl exec -it dataaccess /bin/sh

# use pv-test to launch/exec shell and check counters

# Test by bouncing/deleting pods
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

