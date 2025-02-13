# tasksContainer
Deploy 'Tasks' Django App to Kubernetes

This is targeted at deploying to Kubernetes, however, the interim files/YAML for creating the Docker images and deploying locally with Dockerfiles and Docker Compose YAML are all included.

Setting the ENVIRONMENT variable (an environment variable called ENVIRONMENT !) to 'development' uses a local sqllite3 in memory database, setting it to 'production' will use an MSSQL database (it expects a Windows VM with MSSQL as the target).

The Django Project is called __ProdTasksProj__

To deploy the app to Kubernetes:
- Edit the env section of __prodtasksproj-deployment.yaml__ to suit your needs, you can also edit the other k8s yaml files (See table below) to change eg. port numbers/passwords/other - be careful!
```sh
   $ ./start-k8s-app.sh
```
   Point your browser at http://external-IP-of-nginx-pod:32323 to get to the deployed app.

## Files

| Filename | Description | 
| -------- | ----------- |
| .env.dist |                      Copy and edit as .env for your requirements |
| requirements.txt |               Python modules to use for ProdTasksProj |
| del-k8s-app.sh  |                Delete ProdTasksProj deployments, services and PVC |
| start-k8s-app.sh |               Start/Deploy ProdTasksProj deployments, services and PVC |
| Dockerfile  |                    Build the image for application part of ProdTasksProj |
| nginx/Dockerfile |               Build the image for the nginx part of the application |
| docker-compose.yml |             Compose application locally |
| docker-compose-deploy.yml |      Compose deploy nginx and the app locally (doesn't pull image from Docker Hub)  Build images using Docker files first |
| docker-compose-deploy-img.yml |  Compose deploy nginx and the app locall (pulls image from Docker Hub) Build/push images using Docker files first or use my  images |
| prodtasksproj-deployment.yaml |  k8s Django App deployment |
| prodtasks-service.yaml |         k8s Service for above |
| nginx-deployment.yaml  |         k8s nginx deployment |
| nginx-service.yaml     |         k8s Service for above |
| static-data-persistentvolumeclaim.yaml | k8s PVC - the app doesn't have any data it wants to persist really!

hardev@nutanix.com Feb '25
