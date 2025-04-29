# tasksContainer

Deploy 'Tasks' Django App to Docker and/or Kubernetes

__Switch branch to k8s for the version to deploy the app to Kubernetes__

Images to use to deploy containers:
AMD64: 
ARM64:

I know, tags!  Ran out of patience to build a dual architecture setup.  Using the docker compose yamls will built the images from scratch - then tag and push as you like.

Setting the ENVIRONMENT variable (an environment variable called ENVIRONMENT !) to 'development' uses a local sqllite3 in memory database, setting it to 'production' will use an MSSQL database (it expects a Windows VM with MSSQL as the target).

The Django Project is called __ProdTasksProj__

To deploy the app to Docker locally:
- Edit the env section of __docker-compose-deploy.yml__ and/or copy/edit __.env.dist__ to __.env__ to suit your needs. 
```sh
   $ docker compose -f docker-compose-deploy.yml up
```
   Point your browser at http://localhost:8080 to get to the deployed app.  You will be auto redirected to the /tasks path, get to the admin panel by using http://localhost:8080/admin
   For the admin, no superuser is created (a user called webadmin IS created for the Kubernetes deployment).
      <img src="tasks-iphone.jpg" 
     width="200" 
     height="auto" />
## Files

| Filename | Description | 
| -------- | ----------- |
| .env.dist |                      Copy and edit as .env for your requirements |
| requirements.txt |               Python modules to use for ProdTasksProj |
| Dockerfile  |                    Build the image for the application part of ProdTasksProj |
| nginx/Dockerfile |               Build the image for the nginx part of the application |
| docker-compose.yml |             Compose application locally |
| docker-compose-deploy.yml |      Compose deploy nginx and the app locally (doesn't pull image from Docker Hub)  Build images using Docker files first |

hardev@nutanix.com Feb '25
