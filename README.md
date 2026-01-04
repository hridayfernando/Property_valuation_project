# Property_valuation_project
It's a data science oriented project majorly aimed for property evaluation 
# Multimodal House Price Prediction: Satellite Imagery + Tabular Data

## 📌 Project Overview
This project implements a high-performance Multimodal AI system to predict house prices in King County. By fusing traditional tabular data (square footage, grade, location) with satellite imagery (visualized via CLIP), the model achieves an **R² score of 0.9108**,quite an improvement on tabualr only model
The core of the project is a "Visual-Spatial" architecture that uses **CLIP (Contrastive Language-Image Pretraining)** to extract architectural features from satellite views and **Spatial KNN** to capture neighborhood premiums.

---

## 📂 Repository Structure

| File | Description |
| :--- | :--- |
| `data_fetcher.py` | Python script that interacts with the Google Static Maps API to download satellite imagery for each property ID. |
| `preprocessing.ipynb` | Comprehensive Exploratory Data Analysis (EDA) and initial data cleaning. Handles missing values and coordinate normalization. |
model_training(folder):
    | `model_training.ipynb` | The main multimodal pipeline. Includes CLIP feature extraction, spatial feature engineering (Neighborhood Premium), CatBoost training, and Grad-CAM explainability. |+feature engineering is being done too
     | `final_submission.csv` | The final prediction file containing `id` and `predicted_price`. |:
notebook(folder):
      |`Only_Xgboost.ipynb`| it is the tabular model which utilizes Xgboost on the tabular data for prediciton after data cleaning and feature selection.
      |processed_train.csv| modified training file after EDA
      |processed_test.csv| modified test file after EDA
data(folder):
      |images|:folder contains the extracted images from the API
      |raw|:folder containing (train.xlsx and test2.xlsx)files
requirements.txt:lists all the libraries utilized.

---
--I used colab for my work as my pc doesn't have gpu on local machine--
Steps to run the model:
1)firstly we tend to extract the images from Google static msps API,and download it in the data folder(along with the test and train.xlsx files)
2)Apply EDA on the data,in which we also do data cleaning and download modified (processed_train,processed_test).csv files.(preprocessing.ipynb)
3)then these files are being utilized by (Only_Xgboost.ipynb)for prediction
4)utilized by (model_training).ipynb for resulting prediction
5)feature Engineering is also applied in (Imagary+tabular.ipynb)/(model_training.ipynb) file itself

## ⚙️ Setup & Installation

### 1. Prerequisites
Ensure you have Python 3.8+ installed. You will need a Google Cloud API Key for the `data_fetcher.py` script.

### 2. Install Dependencies
```bash
pip install torch torchvision transformers catboost scikit-learn pandas numpy opencv-python matplotlib geopy# Multimodal House Price Prediction: Satellite Imagery + Tabular Data

