import os
import certifi

from dotenv import load_dotenv
load_dotenv()
mongo_db_url = os.getenv("MONGO_URL_KEY")
print(mongo_db_url)
import pymongo

from src.pipeline.training_pipeline import TrainingPipeline

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from uvicorn import run as run_app
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd

from src.utils.utils import load_object
from src.utils.estimator_utils import NetworkModel
from src.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME, DATA_INGESTION_DATABASE_NAME

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory = "./templates")
ca = certifi.where()
client = pymongo.MongoClient(mongo_db_url, tlsCAFile = ca)

database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI()
origin = ["*"]

# accessing the browser
app.add_middleware(
    CORSMiddleware,
    allow_origins = origin,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/", tags = ["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def train_route():
    training_pipeline = TrainingPipeline()
    training_pipeline.run_pipeline()
    return Response("training is successfull")

@app.post("/predict")
async def predict_route(request: Request, file: UploadFile= File(...)):
    df = pd.read_csv(file.file)

    preprocessor = load_object(r'E:\environments\network_security_system\final_model\preprocessor.pkl')
    final_model = load_object(r'E:\environments\network_security_system\final_model\model.pkl')
    network_model = NetworkModel(preprocessor, final_model)
    print(df.iloc[0])
    y_pred = network_model.predict(df)
    print(y_pred)
    df['predicted values'] = y_pred
    print(df)
    table_html = df.to_html(classes = 'table table-striped')
    return templates.TemplateResponse("table.html", {"request": request, "table": table_html})



if __name__ == "__main__":
    run_app(app, host = 'localhost', port= 8000)



