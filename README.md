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


### DVC
```bash
dvc init
dvc repro
dvc dag

### DEPLOYMENT

1. Build docker image of the source code

2. Push docker image to ECR

3. Launch EC2

4. Pull docker image from ECR to EC2

5. launch docker image in EC2

