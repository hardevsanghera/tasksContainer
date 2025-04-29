# tasksContainer
Deploy 'Tasks' Django App to Kubernetes

This is targeted at deploying to Kubernetes, however, the interim files/YAML for creating the Docker images and deploying locally with Dockerfiles and Docker Compose YAML are all included.

Images to use to deploy containers:
AMD64: docker.io/hsanghera/hardev-prodtasksproj-amd64:latest, docker.io/hsanghera/hardev-nginx-amd64:latest
ARM64: docker.io/hsanghera/hardev-prodtasksproj:latest, docker.io/hsanghera/hardev-nginx:latest

I know, tags!  Ran out of patience to build a dual architecture setup.  Using the docker compose yamls will built the images from scratch - then tag and push as you like.

Setting the ENVIRONMENT variable (an environment variable called ENVIRONMENT !) to 'development' uses a local sqllite3 in memory database, setting it to 'production' will use an MSSQL database (it expects a Windows VM with MSSQL as the target).

The Django Project is called __ProdTasksProj__

To deploy the app to Kubernetes:
- Edit the env section of __prodtasksproj-deployment.yaml__ to suit your needs, you can also edit the other k8s yaml files (See table below) to change eg. port numbers/passwords/other - be careful!
```sh
   $ ./start-k8s-app.sh
```
   Point your browser at http://external-IP-of-nginx-pod:32323 to get to the deployed app.  You will be auto redirected to the /tasks path, get to the admin panel by using http://external-IP-of-nginx-pod:32323/admin
   For the admin panel the userid is webadmin and the password is the same as the password for the SA user you set in the env section.
   
   <img src="tasks-iphone.jpg" 
     width="200" 
     height="auto" />
## Files

| Filename | Description | 
| -------- | ----------- |
| .env.dist |                      Copy and edit as .env for your requirements |
| requirements.txt |               Python modules to use for ProdTasksProj |
| start-k8s-app.sh |               Start/Deploy ProdTasksProj deployments, services and PV/PVC |
| stop=k8s-app.sh |                Stop/Delete ProdTasksProj deployments, services and PV/PVC |
| Dockerfile  |                    Build the image for application part of ProdTasksProj |
| nginx/Dockerfile |               Build the image for the nginx part of the application |
| docker-compose.yml |             Compose application locally |
| docker-compose-deploy.yml |      Compose deploy nginx and the app locally (doesn't pull image from Docker Hub)  Build images using Docker files first |
| docker-compose-deploy-img.yml |  Compose deploy nginx and the app locall (pulls image from Docker Hub) Build/push images using Docker files first or use my  images |
| prodtasksproj-deployment.yaml |  k8s Django App deployment |
| prodtasks-service.yaml |         k8s Service for above |
| nginx-deployment.yaml  |         k8s nginx deployment |
| nginx-service.yaml     |         k8s Service for above |
| static-data-persistentvolumeclaim.yaml | k8s PVC - the app doesn't have any data it wants to persist really! |
| static-pv.yaml | The PV for the app |

hardev@nutanix.com Feb '25
