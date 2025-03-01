from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories
from src.datascience.entity.config_entity import DataIngestionConfig, DataValidationConfig,DataTransformationConfig

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

