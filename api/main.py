
from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()


MODEL = tf.keras.models.load_model("../saved_models/potato_disease_v01.keras")
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy","Unclassified"]



@app.get("/ping")
async def ping():
    return {"message": "Hello, I am alive"}

# Helper function to read and preprocess image
def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data)).convert("RGB")
    image = image.resize((256, 256))  # Resize to match model's expected input
    return np.array(image)


@app.post("/predict")
async def predict(
    file: UploadFile = File(...)

):
    # Read and preprocess image
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, axis=0)  # Add batch dimension

    # Predict
    predictions = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = float(np.max(predictions[0]))

    return {
        "class": predicted_class,
        "confidence": confidence
    }





if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

