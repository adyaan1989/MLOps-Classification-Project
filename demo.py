
# import os
# mongo_db_url = os.getenv('MONGO_DB_URL')
# print(mongo_db_url)

from us_visa.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()
