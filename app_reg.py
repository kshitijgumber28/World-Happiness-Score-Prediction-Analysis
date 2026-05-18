from flask import Flask, request
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load trained pipeline
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, 'happiness_pipeline.pkl')

model = joblib.load(model_path)

@app.route('/')
def home():
    return '''
    <h1>World Happiness Score Predictor 🌍</h1>

    <form action="/predict" method="post">

        Regional Indicator:
        <input name="region" required><br><br>

        Log GDP per capita:
        <input name="gdp" required><br><br>

        Social Support:
        <input name="social_support" required><br><br>

        Healthy Life Expectancy:
        <input name="life_expectancy" required><br><br>

        Freedom to make life choices:
        <input name="freedom" required><br><br>

        Generosity:
        <input name="generosity" required><br><br>

        Perceptions of corruption:
        <input name="corruption" required><br><br>

        <button type="submit">Predict Happiness Score</button>

    </form>
    '''

@app.route('/predict', methods=['POST'])
def predict():

    try:
        # Read user inputs

        region = request.form['region']

        gdp = float(request.form['gdp'])

        social_support = float(request.form['social_support'])

        life_expectancy = float(request.form['life_expectancy'])

        freedom = float(request.form['freedom'])

        generosity = float(request.form['generosity'])

        corruption = float(request.form['corruption'])

        # Create dataframe EXACTLY matching training columns

        input_df = pd.DataFrame({

            'Log GDP per capita': [gdp],

            'Social support': [social_support],

            'Healthy life expectancy': [life_expectancy],

            'Freedom to make life choices': [freedom],

            'Generosity': [generosity],

            'Perceptions of corruption': [corruption],

            'Regional indicator': [region]

        })

        # Predict happiness score

        prediction = model.predict(input_df)

        result = round(prediction[0], 3)

        return f'''
        <h2>Predicted Happiness Score 🌍:</h2>

        <h1>{result}</h1>

        <a href="/">Try Again</a>
        '''

    except Exception as e:

        return f'''
        <h3>Error: Invalid Input</h3>

        <p>{e}</p>

        <a href="/">Go Back</a>
        '''

if __name__ == '__main__':
    app.run(debug=True)