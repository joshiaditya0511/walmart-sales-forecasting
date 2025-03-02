# Results and Conclusions

## Analysis Summary

### Data Overview and Seasonality
I examined a complete dataset covering 143 weeks of sales data for 45 Walmart stores. The data included key variables such as weekly sales, temperature, fuel price, CPI, and unemployment. I observed strong yet irregular seasonal patterns largely driven by holidays. Sales consistently surged during events like SuperBowl, Valentine’s Day, Labour Day/ Back to School Week, Thanksgiving/Black Friday, Christmas/New Year, and occasionally Independence Day. Although most stores exhibited similar seasonal boosts, some exceptions emerged that did not strictly follow the general trend.

### Economic Variables and Their Inter-relationships
One of the most revealing aspects of my analysis was the interaction among the economic indicators:
- **CPI, Fuel Price, and Unemployment:**  
  I found that fuel price and CPI were strongly positively correlated (with an average Pearson correlation coefficient around 0.814), which is logical given that fuel costs form a significant component of the CPI. In contrast, unemployment generally correlated negatively with both CPI and fuel price, although there were a few notable exceptions.
  
- **Weekly Sales and CPI:**  
  When focusing on the trend components, the correlation between weekly sales and CPI became distinctly positive in many cases. This suggests that as consumer price indices rise—potentially reflecting broader economic conditions—sales trends align in a similar direction.

- **Dimensionality Reduction:**  
  By applying PCA to the economic variables (CPI, unemployment, and fuel price), I discovered that two principal components captured about 97% of the variance. This reduction efficiently summarized the complex interrelationships without sacrificing essential information.

### Store-Level Insights
I developed several performance metrics—such as average sales, relative growth, trend-based growth, and sales volatility—to derive a composite score for each store. This quantitative assessment helped in distinguishing higher-performing stores from those that might require further strategic improvements, providing a balanced overview of store dynamics.

## Forecasting Summary

### Modeling Approach and Methodology
To forecast the next 12 weeks of sales, I developed multiple models tailored individually for each store. The models included:
- Holt-Winters Exponential Smoothing  
- ARIMA and SARIMA (both with and without exogenous variables)  
- XGBoost  
- FB Prophet

I trained these models using the initial 105 weeks of data, validated them over 26 weeks using a growing window approach, and evaluated their performance with Mean Absolute Error (MAE). After identifying the best performing model, I retrained it on a cumulative 131 weeks of data to generate forecasts for the reserved 12-week period.

### Comparative Evaluation and Insights
- **Holt-Winters Performance:**  
  Holt-Winters consistently emerged as the strongest performer, recording an average MAE of \$39,162. Its ability to effectively capture both underlying trends and irregular seasonal boosts proved highly robust across the stores.
  
- **Insights on ARIMA, FB Prophet, and XGBoost:**  
  Although ARIMA and FB Prophet delivered competitive results, XGBoost lagged behind in overall MAE. An interesting nuance was noted: XGBoost predictions would have improved significantly if shifted by one week. This underscores a potential timing issue.
  
- **Seasonal Period Discrepancy:**  
  I observed that the conventional 52-week seasonal period does not perfectly capture an annual cycle, as some cases actually manifest a 53-week cycle. This misalignment in the seasonal layer likely contributes to why a one-week shift in the predictions would have yielded more accurate results.

### Final Forecast and Observations
For the final forecast, I retrained the Holt-Winters model using all 131 weeks of training data before forecasting the 12-week hold-out period. The final forecast results were consistent with earlier validation findings:
- **Error Analysis:**  
  While maintaining a consistent average MAE, visual inspection revealed that the model underpredicted sales in roughly 83% of the forecasted weeks, suggesting opportunities for further tuning.
  
- **Model Reliability:**  
  My analysis provides confidence that despite challenges such as irregular holiday effects and seasonal misalignment due to the 52/53-week year issue, the Holt-Winters method remains a reliable choice for forecasting Walmart sales.