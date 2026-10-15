# Customer Churn Prediction

## 📌 Project Overview

Customer Churn Prediction is an end-to-end Machine Learning classification project that predicts whether a telecom customer is likely to leave a company.

The project analyzes customer demographics, service subscriptions, contract details, and billing information to estimate churn risk. It also includes a Streamlit web application where users can enter customer details and receive a prediction with an estimated churn probability.

## 🎯 Project Objectives

- Predict whether a customer is likely to churn.
- Compare multiple classification algorithms.
- Evaluate model performance using classification metrics.
- Build an interactive web application for real-time predictions.
- Support customer retention decisions through churn risk insights.

## 📊 Dataset

**Dataset:** Telco Customer Churn

The dataset contains customer information, service subscriptions, contract details, billing information, and the target variable `Churn`.

**Target variable:** `Churn`
- `Yes` — Customer churned.
- `No` — Customer did not churn.

Customer ID was excluded from model training because it is an identifier rather than a useful predictive feature.

## 🤖 Machine Learning Models

The following classification algorithms were trained and evaluated:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

**Selected Model:** Logistic Regression

Logistic Regression was selected as the best model based on the project's model evaluation.

## 📈 Model Evaluation

The selected Logistic Regression model achieved the following results on the held-out test dataset:

| Metric | Score |
|---|---:|
| Accuracy | 80.55% |
| Precision (Churn = Yes) | 65.7% |
| Recall (Churn = Yes) | 55.9% |
| F1-score (Churn = Yes) | 60.4% |

### What do these metrics mean?

- **Accuracy:** 80.55% of all test predictions were correct.
- **Precision:** 65.7% of customers predicted to churn actually churned.
- **Recall:** The model identified 55.9% of customers who actually churned.
- **F1-score:** 60.4%, balancing precision and recall for the churn class.

These results highlight the importance of improving churn recall so that more customers at risk of leaving can be identified.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

## 🌐 Streamlit Application

The project includes an interactive Streamlit dashboard with:

- Customer profile input form
- Service, contract, and billing details
- Churn prediction using the trained model
- Estimated churn probability
- Visual churn risk indicators
- Suggested customer retention actions

The application uses the saved model pipeline to process customer inputs and generate predictions.

## 📁 Project Structure

```text
Customer_Churn_Prediction/
│
├── app.py
├── models/
│   └── churn_pipeline.pkl
├── requirements.txt
└── README.md
```

*Adjust the structure above if your actual project uses a `src/` folder or contains additional files.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Customer_Churn_Prediction
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

If `app.py` is in the project root:

```bash
streamlit run app.py
```

If `app.py` is inside `src/`:

```bash
streamlit run src/app.py
```

## 🔮 Future Improvements

- Improve recall for the churn class.
- Perform feature selection and compare model performance.
- Tune classification thresholds based on business requirements.
- Add model explainability using feature importance or SHAP.
- Evaluate the model on new customer data.

## 👨‍💻 Conclusion

This project demonstrates an end-to-end Machine Learning workflow, from customer data preprocessing and classification model evaluation to deployment through an interactive Streamlit application.

It provides a practical example of how Machine Learning can help businesses identify customers at risk of churn and make more informed customer retention decisions.
