from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pickle

app = FastAPI()
origins = ["*"]

# ✅ Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    alcohal:float
    alcoholquality: int


datamodel = pickle.load(open(r"B:\Streanlit\New folder\newwinetest.sav", 'rb'))


@app.post('/winetestmodel')
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

      
        print("INPUT to model:", input_list)

        prediction = datamodel.predict([input_list])

        return {"result": "Good quality wine 🍷" if prediction[0] else "Not a good quality wine"}

    except Exception as e:
        return {"error": str(e)}
