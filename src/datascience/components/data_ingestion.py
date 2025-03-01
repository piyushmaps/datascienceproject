import os
import urllib.request as request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import DataIngestionConfig


##Component-Data ingestion component

#after getting the configuration details in data ingestion config, we should be downloading the entire zip file


# This class is responsible for downloading and extracting data.
# It takes a DataIngestionConfig object as input.



class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config=config
    #downloading the zip fil
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):   #request.urlretrieve(): Downloads the file from source_URL and saves it to local_data_file.
            filename, headers=request.urlretrieve(            #filename: Path where the file is saved. #headers: Response headers (metadata)
                url=self.config.source_URL,                   
                filename= self.config.local_data_file         
            )
            logger.info(f"{filename}download! with following info: \n{headers}")

        else:
            logger.info(f"Already exist")





    def extract_zip_file(self):
        """ 
        zip_file_path: str
        Extract the zip file to data directory
        function return none
        
        
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        













