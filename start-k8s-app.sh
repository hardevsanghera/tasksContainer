# Order is important
kubectl -f prodtasksproj-deployment.yaml apply
kubectl -f prodtasksproj-service.yaml apply
kubectl -f nginx-service.yaml apply
kubectl -f static-pv.yaml apply
kubectl -f static-data-persistentvolumeclaim.yaml apply
kubectl -f nginx-deployment.yaml apply
sleep 20
kubectl get all
kubectl get pv,pvc
