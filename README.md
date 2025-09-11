# Potato Disease Classification
Farmers who grow potatoes are facing significant economic losses every year due to various diseases that can affect a potato plant. There are two common diseases known as Early Blight and Late Blight. If farmers can detect these diseases early and apply appropriate treatment, they can save a lot of waste and prevent economic losses.

## 1. Setup for Python
### 1.1 Install Python

Follow [Python installation guide](https://www.python.org/downloads/) and ensure Python 3.9+ is installed.

### 1.2 Create virtual environments

We will use two environments:

* `potato-api` → for FastAPI backend (with TensorFlow, model loading, prediction)

* `potato-streamlit` → for Streamlit UI (lightweight, only requests + streamlit)
```
# Create environments
python -m venv potato-api
python -m venv potato-streamlit
```

### 1.3 Install dependencies

For API (FastAPI + TensorFlow):
```
cd api
pip install -r requirements.txt
```

For Streamlit frontend:
```
cd frontend
pip install -r requirements.txt
```


## 2. Training the Model

1. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/arjuntejaswi/plant-village).

2. Keep only potato-related folders.

3. Open notebook:
```
jupyter notebook
```

4. Run `training/potato-disease-training.ipynb` cell by cell.

5. Save the trained model in `saved_models/potato_model.keras`.

## 3. Running the API (FastAPI Backend)

1. Get inside `api` folder

2. Activate `potato-api` environment:
```
conda activate potato-api   # or source potato-api/bin/activate
```

3. Start server:
```
cd api
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

4. API is now running at:

* Swagger Docs → http://127.0.0.1:8000/docs

* Predict Endpoint → POST /predict

## 4. Running the Streamlit App

1. Activate potato-streamlit environment:
```
conda activate potato-streamlit
```

2. Start Streamlit:
```
cd frontend
streamlit run app.py
```

3. The app will open in your browser at:
http://localhost:8501


## 5. Deployment Options

* Local: FastAPI on 127.0.0.1:8000 + Streamlit on localhost:8501

* Production:

  - Deploy FastAPI on a cloud service (AWS / GCP / Heroku).

  - Point Streamlit app to that API URL.

  - Or package everything into Docker for easier deployment.
