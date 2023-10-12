## WORKflow

Update config.yaml

Update secrets.yaml
Update params.yaml
Update entity
update configuration manager in src config
update components
update pipeline
update main,py
update dvc.yaml
app


### DAGSHUB credentials

MLFLOW_TRACKING_URI=https://dagshub.com/sandmanGPU/kdc_mlflow.mlflow \
MLFLOW_TRACKING_USERNAME=sandmanGPU \
MLFLOW_TRACKING_PASSWORD=170fae55eed33119e40cf121df270c286e09c95f \
python script.py

Export these variables

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/sandmanGPU/kdc_mlflow.mlflow
export MLFLOW_TRACKING_USERNAME=sandmanGPU
export MLFLOW_TRACKING_PASSWORD=170fae55eed33119e40cf121df270c286e09c95f
```

### DVC
```bash
dvc init
dvc repro
dvc dag
```
### DEPLOYMENT

Take care to comment out or remove mflow tracking before deployment

1. Build docker image of the source code

2. Push docker image to ECR

3. Launch EC2

4. Pull docker image from ECR to EC2

5. launch docker image in EC2

## AWS Policies:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

## Create ECR repo to store docker image on aws

- URI: 185544852451.dkr.ecr.ap-southeast-2.amazonaws.com/kdc

## Create EC2 machine, t2.large and 32 gb storage for now

## Open EC2 and install docker in that machine

```bash
sudo apt-get update -y

sudo apt-get upgrade

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

## Configure EC2 as self-hosted runner:

```bash
in github setting>actions>runner>new self hosted runner>choose os> then run command one by one
```

## Setup github secrets

```bash
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = ap-southeast-2

AWS_ECR_LOGIN_URI = 185544852451.dkr.ecr.ap-southeast-2.amazonaws.com/kdc

ECR_REPOSITORY_NAME = kdc
```

Get the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY from aws downloaded csv file