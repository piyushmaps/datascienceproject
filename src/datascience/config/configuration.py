from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories
from src.datascience.entity.config_entity import DataIngestionConfig, DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig

from src.datascience.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH,SCHEMA_FILE_PATH
from src.datascience.utils.common import read_yaml, create_directories
#configuration manager will load the input from src/datascience/constant
class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH):  #CONFIG_FILE_PATH WILL BE present in src\datascience\constants
        self.config=read_yaml(config_filepath)  #we want to read the yaml file so we will use read_yaml function which is defined in utils
        self.params=read_yaml(params_filepath)
        self.schema=read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])  #artifacts_root is in  config.yaml, here we are creating artifact


    def get_data_ingestion_config(self)-> DataIngestionConfig:  #here we are returning dataingestion config which is above the path for root dir, etc
        config=self.config.data_ingestion  #data_ingestion is the key config.yaml file
        create_directories([config.root_dir]) #the first folder needed to create in config.yaml is root_directories

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir

        )

        return data_ingestion_config


    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config

    def get_model_trainer_config(self)->ModelTrainerConfig:
        config=self.config.model_trainer
        params=self.params.ElasticNet
        schema=self.schema.Target_Column

        create_directories([config.root_dir])

        model_trainer_config=ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column = schema.name

        )

        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config=self.config.model_evaluation
        params=self.params.ElasticNet
        schema=self.schema.Target_Column

        create_directories([config.root_dir])


        model_evaluation_config=ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,  
            metric_file_name=config.metric_file_name,
            all_params=params,
            target_column=schema.name,
            mlflow_uri="https://dagshub.com/thakurpiyush1708/datascienceproject.mlflow"
        )

        return model_evaluation_config