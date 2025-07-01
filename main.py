from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pickle

app = FastAPI()

# CORS for any frontend/clients
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the data model
class WineInput(BaseModel):
    fixedacidity: float
    volatileacidity: float
    citricacid: float
    residualsugar: float
    chlorides: float
    freesulfurdioxide: float
    totalsulfurdioxide: float
    density: float
    pH: float
    sulphate: float
    alcohal: float
    alcoholquality: int

# Load model
datamodel = pickle.load(open("newwinetest.sav", "rb"))

# Root route (GET)
@app.get("/")
def read_root():
    return {"message": "Wine Quality Prediction API is live 🍷"}

# Prediction route (POST)
@app.post("/winetestmodel")
def winetest(inputfeture: WineInput):
    try:
        input_list = [
            inputfeture.fixedacidity,
            inputfeture.volatileacidity,
            inputfeture.citricacid,
            inputfeture.residualsugar,
            inputfeture.chlorides,
            inputfeture.freesulfurdioxide,
            inputfeture.totalsulfurdioxide,
            inputfeture.density,
            inputfeture.pH,
            inputfeture.sulphate,
            inputfeture.alcohal,
            inputfeture.alcoholquality
        ]

        prediction = datamodel.predict([input_list])
        return {
            "result": "Good quality wine 🍷" if prediction[0] else "Not a good quality wine"
        }
    except Exception as e:
        return {"error": str(e)}
