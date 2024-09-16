from dataclasses import dataclass


# data ingestion path
@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str
    

#data validation path
@dataclass
class DataValidationArtifact:
    validation_status: bool
    message: str
    drift_report_file_path:str
    

# Data transformation class

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str
    transformed_train_file_path:str
    transformed_test_file_path:str

# # Metrics for evaluation
# class ClassificationMetricArtifact:
#     f1_score: float
#     precision_score: float
#     recall_score: float

@dataclass
class ClassificationMetricArtifact:
    f1_score:float
    precision_score:float
    recall_score:float

# Model Trainer
@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str
    metric_artifact: ClassificationMetricArtifact


@dataclass
class ModelEvaluationArtifact:
    is_model_accepted:bool
    changed_accuracy:float
    s3_model_path:str
    trained_model_path:str

#Model Pusher
@dataclass
class ModelPusherArtifact:
    bucket_name:str
    s3_model_path:str


