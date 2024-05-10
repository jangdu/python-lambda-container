```bash
> docker build --platform linux/amd64 -t docker-image:test .
```

```bash
> aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 111122223333.dkr.ecr.us-east-1.amazonaws.com
```

```bash
> aws ecr create-repository --repository-name hello-world --region us-east-1 --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
```

```bash
> docker tag docker-image:test <ECRrepositoryUri>:latest
```

```bash
docker push 111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest
```

```bash
aws lambda create-function \
  --function-name hello-world \
  --package-type Image \
  --code ImageUri=111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest \
  --role arn:aws:iam::111122223333:role/lambda-ex
```

```bash
aws lambda invoke --function-name hello-world response.json
```
