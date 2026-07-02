# 🌱 Fertilizer Recommendation Agent

## Project Overview

The Fertilizer Recommendation Agent is a Machine Learning and AI-based application that recommends the most suitable fertilizer based on soil properties and crop requirements. The application is developed using the XGBoost classification algorithm and deployed using Streamlit for an interactive user interface.

---

## Problem Statement

**Problem Statement No:** 28

**Title:** Fertilizer Recommendation Agent

The objective of this project is to recommend the appropriate fertilizer using soil and crop information. The system predicts the best fertilizer to improve crop growth and productivity.

---

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Joblib

---

## Machine Learning Model

**Algorithm Used:** XGBoost Classifier

The model was trained using the fertilizer prediction dataset and evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

## Project Structure

```
Fertilizer_Recommendation_Agent/
│
├── app.py
├── xgboost_model.pkl
├── label_encoders.pkl
├── requirements.txt
└── README.md
```

---

## Features

* User-friendly Streamlit interface
* Accepts soil and crop details as input
* Predicts the suitable fertilizer
* Displays fertilizer recommendation instantly
* Fast and easy to use

---

## Input Parameters

* Temperature
* Humidity
* Moisture
* Soil Type
* Crop Type
* Nitrogen
* Potassium
* Phosphorous

---

## Output

* Recommended Fertilizer

---

## Installation

Install the required libraries:

```
pip install -r requirements.txt
```

---

## Run the Application

Execute the following command:

```
streamlit run app.py
```

The application will automatically open in your web browser.

---

## Future Enhancements

* Fertilizer application schedule
* Recommendation history
* Downloadable report
* Weather-based fertilizer suggestions
* AI chatbot support for farmers

---

## Conclusion

The Fertilizer Recommendation Agent helps farmers make informed fertilizer decisions using Machine Learning. It reduces manual effort, supports better crop management, and provides quick and accurate fertilizer recommendations through an easy-to-use Streamlit application.
