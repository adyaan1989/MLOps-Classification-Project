# Classification_end_to_end_project (US Visa Approval)


### Git commands

```bash
git add .

git commit -m "Updated"

git push origin main

```

# 1- Create the git repository

# 2- clone the git repository into the local machine:
```bash
git clone https://github.com/adyaan1989/MLOps-Classification-Project.git
```

# 3- Create the template.py file
```bash
python template.py

```
# 4- Create the venv
```bash
conda create -p visa python==3.8 -y
```

# 5- update the requirements.txt file
# 6- update the setup.py file

### Run command
```bash
pip install -r requirements.txt
```

### Export the environment variable for MongoDB

- export MONGODB_URL="mongodb+srv://<username>:<password>...."

# 7- Workflow for data ingestion:
1-	us_visa > Constants > __init__.py
2-	us_visa > Entity > config_entity.py > artifact_entity.py
3-	us_visa > Configuration > create the file “mongo_db_connection.py”
4-	Create the folder under us_visa “data_access”> create “__init__.py” > create file “usvisa_data.py”
5-	Update the Us_visa > components > data_ingestion.py
6-	Update the us_visa > pipeline > training_pipeline.py
7-	Update the demo.py

# 8- Workflow for data validation:
1-	us_visa > Constants > __init__.py
2-	us_visa > Entity > config_entity.py 
3-	us_visa > Entity > artifact_entity.py
4-	us_visa > utils > main_utils.py
5-	config > schema.yaml
6-	Update the Us_visa > components > data_transformation.py
7-	Update the us_visa > pipeline > training_pipeline.py
8-	Update the demo.py


# 9- Workflow for data transformation:
1-	us_visa > Constants > __init__.py
2-	us_visa > Entity > config_entity.py 
3-	us_visa > Entity > artifact_entity.py
4-	us_visa > Entity > estimator.py
5-	Update the Us_visa > components > data_transformation.py
6-	Update the us_visa > pipeline > training_pipeline.py
7-	Update the demo.py

# 10- Workflow for Model Trainer:
1-	us_visa > Constants > __init__.py
2-	us_visa > Entity > config_entity.py 
3-	us_visa > Entity > artifact_entity.py
4-	config > model.yaml
5-	Update the Us_visa > components > model_trainer.py
6-	Update the us_visa > pipeline > training_pipeline.py
7-	Update the demo.py

# 11- AWS- to be set the S3 bucket before evaluation workflow
1-	us_visa > Constants > __init__.py
2-	us_visa > configuration > aws_connection.py

# 12- cloud_storage
1-	us_visa > cloud_storage > __init__.py
2-	us_visa > cloud_storage > aws_storage.py 

### Export the environment variable

export MONGODB_URL="mongodb+srv://<username>:<password>...."

- export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

- export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

# 13- Workflow for Model Evaluation:
1-	us_visa > Constants > __init__.py
2-	us_visa > Entity > config_entity.py 
3-	us_visa > Entity > artifact_entity.py
4-	Update the Us_visa > components > model_evaluation.py
5-	Update the us_visa > pipeline > training_pipeline.py

# 14- Model_pusher Workflow
1-	us_visa > Entity > config_entity.py 
2-	us_visa > Entity > artifact_entity.py
3-	Update the Us_visa > components > model_pusher.py
4-	Update the us_visa > pipeline > training_pipeline.py

# 15- prediction Workflow
1-	us_visa > Constants > __init__.py
2-	us_visa > Entity > config_entity.py
3-	Update the Us_visa > pipeline > prediction_pipeline.py
4-	Update the us_visa > pipeline > training_pipeline.py

# 16- App
1-	Create a folder in root project “templates”> create file usvisa.html
2-	Create a folder in root project “static” > create folder css > file style.css
3-	Updated the app.py file
4-	Run the python app.py
5-	Run the on local host : US Visa Prediction (http://localhost:8080/)
6-	Model Training : US Visa Prediction (http://localhost:8080/train)

# 17- AWS Deployment workflows:

Create the folder “.github”>”workflows” inside workflows folder crete the aws.yaml file
e.g.

1 - .github>workflows>aws.yaml

#### Now update the
2 - Dockerfile

# 18-  AWS-CICD-Deployment-with-Github-Actions

1. Login to AWS console.

2. Create IAM user for deployment

    #### with specific access

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws


    #Description: About the deployment

    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch Your EC2 

    4. Pull Your image from ECR in EC2

    5. Lauch your docker image in EC2

    #Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

### 3. Create ECR repo to store/save docker image

    - Save the URI: 315865595366.dkr.ecr.us-east-1.amazonaws.com/visarepo

### 4. Create EC2 machine (Ubuntu)
### 5. Open EC2 and Install docker in EC2 Machine:

#optinal

    sudo apt-get update -y

    sudo apt-get upgrade

#required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

### 6. Configure EC2 as self-hosted runner:
    - setting>actions>runner>new self hosted runner> choose os> then run command one by one 

### 7. Setup github secrets:
* MONGODB_URL
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* AWS_DEFAULT_REGION
* ECR_REPO