import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
#INFO (20): General information about program execution (e.g., successful steps).
# %(asctime)s: Inserts the timestamp of when the log message was created.
# %(message)s: Inserts the actual log message provided by the user.
project_name="datascience"

list_of_files=[
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",  #components has all pipleilne(ingestion,eval etc)
    f"src/{project_name}/utils/__init__.py", #generic facilities will be defined here
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.yaml",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "app.py"

    
]

for filepath in list_of_files:
    filepath=Path(filepath) #filepath = Path("/home/user/file.txt")
                            # filepath is now a Path object, and you can do things like:
                            # print(filepath.name)  # Output: file.txt
                            # print(filepath.parent)  # Output: /home/user
    filedir,filename=os.path.split(filepath)
                            #  print(filedir)   # Output: /home/user
                            # print(filename)  # Output: file.txt


    if filedir!="":        #if filedir is empthy then the following
        os.makedirs(filedir,exist_ok=True) #if the file exist do not make it by the filefir name
        logging.info(f"Creating directory {filedir}for the file: {filename}")


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:

            pass
            logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exist")