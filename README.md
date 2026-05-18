# World Happiness Score Prediction using Machine Learning 🌍

## Project Overview
This project is a machine learning regression system built using the World Happiness Report dataset to predict a country's happiness score based on socioeconomic and regional indicators.

The project includes:
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Regression modeling
- Model evaluation
- Cross-validation
- Flask deployment

The complete workflow is documented in the Jupyter Notebook file.

---

## Dataset Features

Features used in the project:
- Log GDP per capita
- Social support
- Healthy life expectancy
- Freedom to make life choices
- Generosity
- Perceptions of corruption
- Regional indicator

Target Variable:
- Ladder score

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Statsmodels
- Flask
- Joblib

---

## Machine Learning Workflow

### Data Preprocessing
- Missing value handling
- One-hot encoding
- Feature scaling using `StandardScaler`
- Yeo-Johnson transformation using `PowerTransformer`

### Feature Engineering
- Regional dummy variable creation
- Skewness handling
- Outlier analysis
- Multicollinearity checking using VIF

### Model Used
- Linear Regression
- Dummy Regressor (Baseline Model)

---

## Model Evaluation

### Regression Metrics
- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- R² Score
- Adjusted R² Score
- Cross Validation

---

## Flask Deployment
A Flask web application was created where users can:
- Enter socioeconomic indicators
- Predict happiness score in real-time

---

## Project Structure

```bash
World-Happiness-Score-Prediction/
│
├── World_Happiness_Analysis.ipynb
├── app.py
├── world_happiness_pipeline.pkl
├── requirements.txt
├── README.md
└── dataset/
```

---

## How to Run the Project

### 1. Clone Repository

```bash
git clone <your-repo-link>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Flask App

```bash
python app.py
```

---

## Future Improvements
- Try advanced regression models
- Hyperparameter tuning
- Interactive dashboard integration
- Cloud deployment using Render/Heroku
- Feature importance visualization

---

## Notebook Contents
- Exploratory Data Analysis (EDA)
- Data Cleaning
- Feature Engineering
- Data Visualization
- Regression Modeling
- Cross Validation
- Model Evaluation
- Deployment Preparation

---

## Author
Kshitij Gumber
