import requests
import json

url = "http://127.0.0.1:8000/winetestmodel"

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
    "alcohal":12.5000,
    "alcoholquality": 5
}


newdata = json.dumps(input_data)

headers = {"Content-Type": "application/json"}

requestdata = requests.post(url, data=newdata, headers=headers)

print("Status Code:", requestdata.status_code)
print("Response:", requestdata.text)
