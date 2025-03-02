# Forecasting

## Importing Libraries and Dataset

## Methodology

### Data

- **Source:**  
  The data for this analysis is from [Kaggle](https://www.kaggle.com/datasets/rutuspatel/walmart-dataset-retail).

- **Content:**  
  The dataset contains weekly sales for 45 Walmart stores covering the years 2010 to 2012.

- **Forecasting Strategy:**  
  Since sales patterns differ across stores, forecasts will be developed separately for each store.

### Modeling

The following models were explored for forecasting:

1. Holt-Winters Exponential Smoothing  
2. ARIMA  
3. ARIMAX  
4. SARIMA  
5. SARIMAX  
6. FB Prophet  
7. XGBoost

### Training

- **Data Length:**  
  Each store has 143 weeks of sales data. Our goal is to generate forecasts for the next 12 weeks.

- **Hold-Out Period:**  
  The last 12 weeks are set aside as a hold-out "forecast" period.

- **Training and Validation Split:**  
  The remaining 131 weeks are used for model development. To capture seasonal effects—especially because of yearly patterns—the first 105 weeks (over 2 full years) serve as our initial training set. The following 26 weeks are used as a validation period.

- **Model Development:**  
  - For time series models (ARIMA, SARIMA, and SARIMAX), we train multiple candidate models with different orders on the 105-week training data. Information criteria (Akaike Information Criterion, AIC) are used to choose the best orders for each of these models.  
  - For XGBoost and FB Prophet, several hyperparameter configurations (e.g., max depth, learning rate, changepoint sensitivity) are initially considered, but we do not use AIC/BIC for these models.

### Evaluation

- **Metric:**  
  Although each model optimizes its own internal loss, we use Mean Absolute Error (MAE) as our common metric to compare performance.

- **Growing Window Forecasting:**  
  For the 26-week validation period, we simulate a real-world forecasting scenario using a growing window approach. Specifically:
  - The model predicts one week ahead.
  - After each prediction, the actual value is added to the training set.
  - This process repeats until forecasts have been made for the entire 26-week period.

- **Model Selection:**  
  The candidate model with the lowest average MAE over the validation windows is chosen as the best model.

- **Final Forecast:**  
  Once the best model is identified, it is re-trained on the full 131 weeks (the original training plus validation periods). Finally, this retrained model is used to forecast the reserved 12 weeks.

## Different models

1. Holt Winters i.e. Triple Exponential Smoothing 

2. ARIMA with orders
    - (6, 1, 4)
    - (6, 1, 5)
    - (6, 2, 4)
    - (6, 2, 5)
    - (9, 2, 4)
    - (9, 2, 5)

3. SARIMA with orders
    - (6, 1, 4), (2, 1, 5, 52)
    - (6, 1, 5), (2, 1, 5, 52)
    - (6, 2, 4), (2, 1, 5, 52)
    - (6, 2, 5), (2, 1, 5, 52)
    - (9, 2, 4), (2, 1, 5, 52)
    - (9, 2, 5), (2, 1, 5, 52)

4. SARIMAX with cpi, holiday_flag and orders
    - (6, 1, 4), (2, 1, 5, 52)
    - (6, 1, 5), (2, 1, 5, 52)
    - (6, 2, 4), (2, 1, 5, 52)
    - (6, 2, 5), (2, 1, 5, 52)
    - (9, 2, 4), (2, 1, 5, 52)
    - (9, 2, 5), (2, 1, 5, 52)

5. XGBoost with
    - month
    - year
    - holiday_flag
    - CPI
    - lagged sales

6. FB Prophet

## Saving and/or loading previous results

## Train, Test and Eval split

## Loss metric

## Data Preparation

## Model Training

### Holt Winters 

#### Training

#### Calculate Errors

#### Visualize predictions

### ARIMA

#### Training

#### Calculate Errors

#### Visualize Predictions

### XGBoost

#### Separate train test split and growing windows

#### Training

#### Calculate Errors

#### Visualize Predictions

### FB Prophet

#### Separate train test split and growing windows

#### Training

#### Calculate Errors

#### Visualize Predictions

### SARIMA

#### Separate train test split and growing windows

#### Training

#### Calculate Errors

#### Visualize Predictions

## Model Comparison

#### Observations

- Comparing the mean and standard deviation of Mean Absolute errors across stores and across growing window forecasts, **Holt-Winters** outperforms all other models. Hence, it will be used for full forecast of the next 12 weeks.
- Prophet comes in second place with slighly worse MAE scores.
- Same with ARIMA, which comes in third place.
- XGBoost is the worst performer with significantly higher MAE scores. However, peculiarly, when looking at the the plot of actual vs. predicted values, XGBoost would have performed extremely well if only it had predicted values one week ahead. Basically, if I shifted the predictions of XGboost by one week, it would have been the best performer.
- Same case can also be observed for other models too, albeit in relatively lesser extent.
- The reason behind this might be the fact that I used 52 weeks as seasonal period of 1 year. But, 52 weeks don't completely make up 1 year. Combined with the fact that the model trained on 105 weeks (52 + 53), it might have justifyably miscalculated the seasonal effect leading to offset spikes in sales 

## Final Forecast

### Final Training

### Error Analysis

### Visualization of Results

### Observations

1. As expected, Holt Winters model does predict the future sales well enough for all 12 weeks at once.
2. It's average MAE for this forecast across all stores was 39162 dollars which is consistent with it's previous average error rate calculated during model comparison using growing window forecast.
3. However, visual inspection shows that the model underpredicted the values 83% of times i.e. for 10 of the 12 weeks.
