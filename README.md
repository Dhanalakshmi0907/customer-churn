1. Problem Statement
Customer churn in banking refers to when customers stop using a bank’s services. This classification problem aims to identify patterns in customer behavior to predict whether a customer will churn (Exited = 1) or stay (Exited = 0). Solving this helps financial institutions reduce revenue loss by targeting at-risk customers with retention strategies.
2. Abstract
The project predicts customer churn using machine learning, utilizing structured bank customer data to uncover patterns and behavior linked to customer departure. Various models like Logistic Regression and Random Forest were implemented, with Random Forest achieving the best performance. Key features influencing churn include tenure, credit score, balance, and activity status. The system offers an explainable and practical approach to help banks proactively address customer attrition.
3. System Requirements
Hardware:
oMinimum 4 GB RAM
oDual-core processor
Software:
oPython 3.8+
oJupyter Notebook / Google Colab
oLibraries: pandas, numpy, scikit-learn, matplotlib, seaborn, plotly, xgboost, shap
4. Objectives
Build ML models to classify customers as churned or retained.
Achieve high recall and F1-score to reduce false negatives.
Identify features with the most influence on churn.
Offer actionable business insights from model outputs.
Deploy an interactive churn prediction interface.


5. Flowchart of Project Workflow
Include your workflow image (you can design it using draw.io or Canva). Example structure:
nginx
CopyEdit
Data Collection → Data Preprocessing → EDA → Feature Engineering → Model Training & Tuning → Evaluation → Deployment
6. Dataset Description
Source: Kaggle Bank Customer Churn Dataset
Type: Public
Rows/Columns: ~10,000 rows, 14 features
Target Column: Exited (0 or 1)
Features include: Credit Score, Age, Geography, Gender, Tenure, Balance, NumOfProducts, IsActiveMember, EstimatedSalary
Add a screenshot of df.head() from your notebook.
7. Data Preprocessing
No missing values
Dropped irrelevant columns: RowNumber, CustomerId, Surname
Label Encoding for Gender
One-Hot Encoding for Geography
StandardScaler applied to numerical features
Addressed class imbalance using class weights
Add before/after screenshots of data transformations.
8. Exploratory Data Analysis (EDA)
Churn was ~20%
Customers with high balance and low tenure churned more
Customers from Germany had higher churn rates
Inactive members had significantly higher churn
Include screenshots of:
Boxplots
Correlation heatmaps
Churn vs Tenure/Geography plots


9. Feature Engineering
Created BalancePerProduct = Balance / (NumOfProducts + 1)
Binned Tenure into categories (e.g., New, Mid, Loyal)
Removed uninformative features
Final dataset: All numeric and model-ready
Explain why these features improve interpretability or model accuracy.
10. Model Building
Models Tried: Logistic Regression, Random Forest (best), XGBoost (optional)
Train/Test Split: 80/20 stratified
Hyperparameter Tuning: GridSearchCV (for Random Forest)
Tools: scikit-learn, GridSearchCV
Add screenshots of model training and parameter outputs.
11. Model Evaluation
Metrics:
oRandom Forest: Accuracy ~85%, F1-score ~0.78, ROC-AUC ~0.87
Visuals:
oConfusion Matrix
oROC Curve
Feature Importance:
oTenure, Credit Score, NumOfProducts, IsActiveMember
Include all evaluation screenshots here.
12. Deployment
Platform: Streamlit Cloud
Link: [Add Streamlit App Link]
Deployment Method: Streamlit app with user input fields
UI Screenshot: Include screenshot of deployed web app
Sample Prediction: Show example where a customer is predicted to churn

13. Source Code
Complete code is available on GitHub:
