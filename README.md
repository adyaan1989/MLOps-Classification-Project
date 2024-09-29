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
