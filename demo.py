from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuartion
from housing.component.data_transformation import DataTransformation
import os

def main():
    try:
        '''
        pipeline = Pipeline()
        pipeline.run_pipeline()
        '''
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))
        pipeline.start()
        logging.info("main function execution completed.")
        #data_validation_config = Configuartion().get_data_transformation_config()
        #print(data_validation_config)
       # schema_file_path=r"D:\Ineuron\MLProjecct\MLProject-1\config\schema.yaml"
        #file_path=r"D:\Ineuron\MLProjecct\MLProject-1\housing\artifact\data_ingestion\2022-07-03-00-23-41\ingested_data\train\housing.csv"

        #df= DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        #print(df.columns)
        #print(df.dtypes)

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()
