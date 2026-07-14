# 📊 Customer Churn Prediction

## 📌 Project Overview

Customer churn is one of the biggest challenges for businesses, especially in the banking and telecom industries. This project uses Machine Learning to predict whether a customer is likely to leave the company based on their demographic and account information.

To make the model user-friendly, a **Streamlit web application** was developed where users can enter customer details and instantly receive a churn prediction.

---

## 🎯 Objective

The objective of this project is to build a machine learning model that helps businesses identify customers who are at risk of leaving so they can take proactive retention measures.

---

## 📂 Dataset

The project uses the **Customer Churn Modeling** dataset containing customer information such as:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Has Credit Card
- Is Active Member
- Estimated Salary

**Target Variable:**
- **Exited**
  - 0 → Customer Stays
  - 1 → Customer Leaves (Churn)

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- TensorFlow/Keras (if used)
- Matplotlib
- Seaborn
- Streamlit

---

## ⚙️ Project Workflow

1. Load and explore the dataset.
2. Perform data preprocessing and cleaning.
3. Encode categorical variables.
4. Scale numerical features.
5. Split the dataset into training and testing sets.
6. Train multiple machine learning models.
7. Evaluate model performance.
8. Save the trained model.
9. Build an interactive Streamlit application for real-time predictions.

---

## 💻 Streamlit Application

The project includes a **Streamlit-based web interface** that allows users to:

- Enter customer information through an interactive form.
- Predict whether a customer is likely to churn.
- Display the prediction instantly in a user-friendly interface.
- Provide an easy way for non-technical users to interact with the machine learning model.

---

## 📊 Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC Score

---

## 📁 Project Structure

```
├── customer_churn_modeling.ipynb
├── app.py
├── model.pkl
├── scaler.pkl
├── encoder.pkl
├── requirements.txt
└── README.md
```

---

## 🚀 Future Improvements

- Deploy the application on Streamlit Community Cloud.
- Improve prediction accuracy using hyperparameter tuning.
- Add probability scores for churn risk.
- Integrate the application with a database for real-time customer analysis.

---

## 👨‍💻 Author

**Vrundalim**
