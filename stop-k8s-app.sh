kubectl -f prodtasksproj-service.yaml delete
kubectl -f nginx-service.yaml delete
kubectl -f prodtasksproj-deployment.yaml delete
kubectl -f nginx-deployment.yaml delete
kubectl -f static-pv.yaml delete
kubectl -f static-data-persistentvolumeclaim.yaml delete
kubectl get all
kubectl get pvc
