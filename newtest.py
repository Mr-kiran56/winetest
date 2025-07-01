import requests
import json

# Replace with your actual Render deployment URL
url = "https://your-render-app.onrender.com/winetestmodel"

input_data = {
    "fixedacidity": 7.4,
    "volatileacidity": 0.70,
    "citricacid": 0.00,
    "residualsugar": 1.9,
    "chlorides": 0.076,
    "freesulfurdioxide": 11.0,
    "totalsulfurdioxide": 0.9978,
    "density": 3.51,
    "pH": 0.56,
    "sulphate": 9.4,
    "alcohal": 12.5,
    "alcoholquality": 5
}

newdata = json.dumps(input_data)
headers = {"Content-Type": "application/json"}

response = requests.post(url, data=newdata, headers=headers)

# Root route (GET)
@app.get("/")
def read_root():
    return {"message": response.text}
print("Status Code:", response.status_code)
print("Response:", response.text)
