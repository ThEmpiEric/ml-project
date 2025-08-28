import os
import sys
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logger import logging
from exception import CustomException

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingetion(self): 
        logging.info('Initiating data ingestion')
        try: 
            print(os.getcwd())
            df = pd.read_csv('./data/clean_data.csv')
            logging.info('Data ingestion completed successfully')

            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)
            df.to_csv(self.config.raw_data_path, index=False,header=True)

            logging.info('Train test split initiated')

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.config.train_data_path, index=False, header=True)
            test_set.to_csv(self.config.test_data_path, index=False, header=True)
            
            logging.info('Ingestion completed')

            return (
                self.config.train_data_path,
                self.config.test_data_path
            )

        except Exception as e:
            logging.error(f'Error occurred during data ingestion: {e}')
            raise CustomException(e, sys) from e


if __name__ == '__main__':
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingetion()
