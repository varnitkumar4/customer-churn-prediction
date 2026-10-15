# 📊 Customer Churn Prediction

An end-to-end Machine Learning project that predicts customer churn using classification algorithms and an interactive Streamlit web application.

<p align="center">
  <a href="https://customer-churn-prediction-cw5jh6ob68wi66c93h7nht.streamlit.app/">
    <img src="https://img.shields.io/badge/Live%20Demo-Open%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live Demo">
  </a>
  <a href="https://github.com/varnitkumar4/customer-churn-prediction">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Repository">
  </a>
</p>

## 🌐 Live Demo

**Try the application:**  
https://customer-churn-prediction-cw5jh6ob68wi66c93h7nht.streamlit.app/

The application allows users to enter customer information, predict churn, view estimated churn probability, and explore suggested customer retention actions.

## 📌 Project Overview

Customer churn occurs when a customer stops using a company's products or services. Predicting churn helps businesses identify customers who may be at risk of leaving and take appropriate retention measures.

This project uses the Telco Customer Churn dataset to build a binary classification model. It covers data exploration, preprocessing, model training, evaluation, and deployment through Streamlit.

## 🎯 Project Objectives

- Predict whether a telecom customer is likely to churn.
- Explore customer demographics, service subscriptions, contracts, and billing patterns.
- Compare multiple classification algorithms.
- Evaluate model performance using classification metrics.
- Build an interactive web application for customer churn prediction.
- Present churn probability and risk insights to support retention decisions.

## 📊 Dataset

**Dataset:** Telco Customer Churn

The dataset contains information about telecom customers, including:

- Customer demographics
- Account information and tenure
- Internet and phone services
- Contract types
- Payment methods
- Monthly and total charges
- Churn status

**Target variable:** `Churn`

- `Yes` — The customer churned.
- `No` — The customer did not churn.

The `customerID` column was excluded from model training because it is an identifier rather than a predictive customer feature.

## 🔍 Exploratory Data Analysis

The project explored churn patterns across different customer attributes.

Key observations:

- Month-to-month contracts had the highest number of churned customers.
- Electronic check users had the highest churn rate among the payment methods examined.
- Fiber optic customers showed substantial churn.
- Customer tenure and total charges were strongly correlated in the dataset.
- The target variable was imbalanced, with more non-churning customers than churning customers.

These are observations from the dataset and do not, by themselves, establish that any individual feature causes churn.

## 🤖 Machine Learning Models

Three classification algorithms were trained and evaluated:

1. **Logistic Regression**
2. **Decision Tree Classifier**
3. **Random Forest Classifier**

### Selected Model: Logistic Regression

Logistic Regression was selected based on the project's model evaluation and its balance of overall accuracy and churn-class performance.

The final trained preprocessing and classification pipeline is saved as:

`models/churn_pipeline.pkl`

The pipeline includes feature preprocessing and the trained classification model.

## 📈 Model Evaluation

The selected model was evaluated on a held-out test dataset.

| Metric | Score |
|---|---:|
| Accuracy | 80.55% |
| Precision — Churn = Yes | 65.7% |
| Recall — Churn = Yes | 55.9% |
| F1-score — Churn = Yes | 60.4% |

### Understanding the Results

- **Accuracy:** 80.55% of test predictions were correct.
- **Precision:** Of the customers predicted to churn, 65.7% actually churned.
- **Recall:** The model identified 55.9% of customers who actually churned.
- **F1-score:** 60.4%, combining precision and recall into a single metric.

The recall score indicates an opportunity to improve the identification of customers who may leave.

## 🖥️ Streamlit Application

The deployed web application provides:

- Customer profile inputs
- Service and subscription details
- Contract and billing information
- Churn prediction from the trained pipeline
- Estimated churn probability
- Visual churn risk indicators
- Suggested customer retention actions

The model's output is an estimate, not a guarantee of future customer behavior.

## 🛠️ Technologies Used

- **Python** — Programming language
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical operations
- **Scikit-learn** — Preprocessing, model training, and evaluation
- **Matplotlib** — Data visualization
- **Seaborn** — Exploratory data visualization
- **Joblib** — Saving and loading the trained model
- **Streamlit** — Interactive web application
- **Git and GitHub** — Version control and source code hosting
- **Streamlit Community Cloud** — Application deployment

## 📁 Project Structure

```text
customer-churn-prediction/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   └── processed/
│
├── models/
│   └── churn_pipeline.pkl
│
├── notebooks/
│   └── 01_eda.ipynb
│
├── reports/
├── src/
│
├── check_data.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/varnitkumar4/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app/app.py
```

The application will open in your browser, usually at `http://localhost:8501`.

## 🚀 Deployment

The application is deployed using Streamlit Community Cloud and connected to this GitHub repository.

**Live application:**  
https://customer-churn-prediction-cw5jh6ob68wi66c93h7nht.streamlit.app/

## 🔮 Future Improvements

- Improve recall for the churn class.
- Tune classification thresholds according to business requirements.
- Perform feature selection and hyperparameter tuning.
- Add model explainability using feature importance or SHAP.
- Evaluate performance on new customer data.
- Monitor model performance as customer behavior changes.

## 👨‍💻 Conclusion

This project demonstrates an end-to-end Machine Learning workflow, from exploratory data analysis and preprocessing to classification, model evaluation, and web deployment.

It provides a practical example of using customer data to estimate churn risk and support more informed customer retention decisions.

## 🔗 Project Links

- **Live Demo:** https://customer-churn-prediction-cw5jh6ob68wi66c93h7nht.streamlit.app/
- **GitHub Repository:** https://github.com/varnitkumar4/customer-churn-prediction

---

*Built with Python, Scikit-learn, and Streamlit.*
