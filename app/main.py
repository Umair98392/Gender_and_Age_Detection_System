from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

app = FastAPI()

# Configure CORS settings
origins = [
    
    
    "http://127.0.0.1:8086",
    # Adjust this to match your frontend's URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the pre-trained model
model = load_model('model/gender_and_age_prediction_model.h5')

# Gender labels
gender_dict = {0: 'Male', 1: 'Female'}


# Prediction route
@app.post("/predict/")
async def predict(file: UploadFile):
    # Read and process the uploaded image
    with Image.open(file.file) as img:
        img = img.resize((128, 128))
        img = np.array(img)
        img = img.reshape(1, 128, 128, 3)

        # Predict gender and age
        predictions = model.predict(img)
        pred_gender = gender_dict[round(predictions[0][0][0])]
        pred_age = round(predictions[1][0][0])
        pred_age_group = get_age(pred_age)

    return {"gender": pred_gender, "age_group": pred_age_group}

# Age distribution function
def get_age(distr):
    
    if distr >= 0 and distr <= 15: return "0-15"
    if distr >= 16 and distr <= 30: return "16-30"
    if distr >= 31 and distr <= 45: return "31-45"
    if distr >= 46 and distr <= 60: return "46-60"
    if distr >= 61 and distr <= 75: return "61-75"
    if distr >= 76 and distr <= 90: return "76-90"
    if distr >= 91: return "91+"
    return "Unknown"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
