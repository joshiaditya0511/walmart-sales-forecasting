# Analysis

## Importing Libraries and Dataset

## Preliminary Data Cleaning

## Final/Major Observations

```{admonition} Final/Major Observations
:class: dropdown

1. There are 45 unique stores and we have data on weekly sales for 143 weeks for each store starting from 5th Feb 2010 to 26 Oct 2012
2. Except holiday_flag, all other variables like weekly_sales, temperature, fuel_price, cpi, unemployment are unique to each store and date. holiday_flag is common for all stores.
3. There are no missing values in the dataset.
4. Holiday_flag is highly imbalanced with only 10% of the data being holiday weeks.
5. From visually inspecting the total sales for each week overlapped with holiday weeks, we can clearly see a seasonal trend. The holiday_flags are mostly set for these occassions:
    - Valentines day or superbowl (2nd week of Feb)
    - Labour day/ back to school (1st or 2nd week of Sept)
    - Thanksgiving and Black Friday (3rd and/or 4th week of Nov around Nov 24th)
    - Christmas and New Years (3rd and/or 4th week of Dec around Dec 24th)
    - Also, very few stores also see boost in Sales for Independence day (1st week of July around July 4th)
6. From visual inspection of the Times series decomposition plot using STL, what I noticed is it cannot properly decompose the sales into a "nice" continuous seasonal component. The seasonal effect is directly due to the recurring holiday sales boots, but they are randomly distributed over the year and repeat yearly. It's not like every month there's a holiday at a fixed interval. They are inconsistently distributed. So, technically the season is 52 weeks long. But, the seasonal effect is not efficiently captured by the STL decomposition.
6. From visual inspection, most sales get boosted by Balck Friday and New Years. Valentines week does see some boost in sales but not as significant as others. Labour day does not seem to have a significant impact on sales.
7. The series looks additive for all stores from visual inspection of plots.
8. Unemployment is highly negatively correlated with cpi for almost all stores.
9. Unemployment is also substantially negatively correlated with fuel_price for almost all stores. Not as strongly correlated as with cpi, but still significant.
10. Store 36 is definitely an odd one out. It's weekly sales show a clear downward trend with no seasonal effects.
11. Unemployment
    - When looking at coorelation coefficients for weekly_sales vs unemployment; Looking at it, the trend component of weekly sales is definitely more correlated with unemployment than regular weekly_sales. But, there's high contrast in how it's correlated. Sometimes it's strongly positive, sometimes it's strongly negative. Few times it's close to zero. So, I'm not sure if it's a good indicator of whether there's a relationship between weekly_sales and unemployment.
12. Consumer Price Index:
    - When looking at weekly_sales and cpi directly, the correlations is insignificant. But, when considering only the trend component with respect to CPI, there seems to be a significant correlation.
    - Most of the correlations are strongly positive. Very few are strongly negative. And even fewer are weakly positive or negative.
    - If for all stores the correlations were in same direction with significant magnitude, then it would hold some meaning. But, it doesn't.
13. Temperature:
    - There is no correlation between weekly_sales and temperature
14. CPI and Fuel price are strongly positively correlated with each other for ALL stores with average Pearson correlation coefficient of 0.814. This is intuitive because fuel pice is generally considered when calculating CPI.
15. Unemployment and CPI are negatively correlated for most stores. For 75% of then stores, the correlation is greater in magnitude than 0.73 and for 85% of the stores it's greater in magnitude than 0.51. But, for the rest of the stores, the correlation gets closer to zero. And for store 24, the correlation is strongly positive with the coefficient being 0.86
16. Fuel Price and Unemployment are negatively correlated for most stores. This correlation isn't as strong as Unemployment and CPI. For 75% of then stores, the correlation is greater in magnitude than 0.53. But, for the rest of the stores, the correlation gets closer to zero. And for store 24, the correlation is strongly positive with the coefficient being 0.6
17. PCA on CPI, Unemployment and Fuel Price:
    - The 3 features cpi, unemployment and fuel_price are reduced to 2 principal components which on average (across all stores) explains 97% variance across the 3 features.
    - When I tried reducing the features to just 1 principal component, I got worse results where on average (across all stores) the variance explained was only 83%
```


## Checking if features vary only with date or store too

### Conclusions/observations

- Except holiday_flag, all other variables like weekly_sales, temperature, fuel_price, cpi, unemployment are unique to each store and date.
- holiday_flag is common for all stores. 

## Miscellaneous Analysis

### Observaitons

The data is incomplete for years 2010 and 2012. So, the yearly cycle needs to be offset while considering 2010 values as the starting point

### Checking sales with respect to date and holidays

#### Observations

- From visually inspecting the weekly_sales, we can clearly see a seasonal trend. The holiday_flags are mostly set for these occassions:
    - Valentines day (Feb 2nd week)
    - Labour day/ back to school (Sep 1st week)
    - Thanksgiving and Black Friday (Nov 24th weeok)
    - Christmas and New Years (Dec 25th week)
    - Also, very few stores also see boost in Sales for Independence day (July 4th week)

- From visual inspection, most sales get boosted by Balck Friday and New Years. Valentines week does see some boost in sales but not as significant as others. Labour day does not seem to have a significant impact on sales.

- Extra and isolated Holiday effects:
    - April 6 (specifically 2012)
    - August 6
    - June 4 (specifically 2011, 2012)

## Unemployment Rate Analysis
   - Investigate whether the weekly sales are affected by the unemployment rate.
   - Identify which stores are suffering the most if an effect exists.

### Sales and Unemployment comparison

From Visual inspection of Weekly sales and Unemployment side-byside, no direct correlation can be observed between sales and unemployment rate. However, seasonal decompose might tell us something

### Correlation between unemployment rate and sales

### Observations
Looking at it, the trend component of weekly sales is definitely more correlated with unemployment than regular weekly_sales. But, there's high contrast in how it's correlated. For most of the stores, it's strongly negative. For some other stores it's strongly positive. Few times it's close to zero. So, I'm not sure if it's a good indicator of whether there's a relationship between weekly_sales and unemployment.

## Decomposition of Store-wise Weekly Sales

### STL Decomposition of weekly_sales for selected stores

### MSTL to capture monthly and annual seasonality separately?

### Observations

From visual inspection of the Times series decomposition plot using STL and MSTL, what I noticed is it cannot properly decompose the sales into a "nice" continuous seasonal component. The seasonal effect is directly due to the recurring holiday sales boots, but they are randomly distributed over the year and repeat yearly. It's not like every month there's a holiday at a fixed interval. They are inconsistently distributed. So, technically the season is 52 weeks long. But, the seasonal effect is not efficiently captured by the STL decomposition.



## Temperature Effect
- Examine if temperature influences weekly sales.

### Checking correlation between weekly_sales and temperature

#### Observations

- From visual inspection of the correlation heatmaps, weekly sales are definitely not correlated with temperature.
- No need for further hypothesis testing to determine if there is a relationship between temperature and weekly sales.

### Seasonal Decomposition of Temperature

#### Observations

- From visual inspection, temperature is obviously seasonal, with peaks in summer (American season)

## Consumer Price Index

### Checking correlation between weekly_sales and its trend component with CPI

### Observations
- When looking at weekly_sales and cpi directly, the correlations is insignificant. But, when considering only the trend component with respect to CPI, there seems to be a significant correlation.
- Most of the correlations are strongly positive. Very few are strongly negative. And even fewer are weakly positive or negative.
- If for all stores the correlations were in same direction with significant magnitude, then it would hold some meaning. But, it doesn't.

## Fuel Price

### Checking correlation between weekly_sales and its trend component with Fuel Price

### Observations

- Similar to CPI, Fuel Price also for most stores seems to have a strong positive correlation with the sales.
- However, similar to CPI, Fuel Price some of the stores seems to have a negative or insignificant correlation with the sales.
- So, Fuel Price is not a good "global" indicator of the sales.

## Store Performance Analysis

Performance metrics:

1. Average sales:
    - This won't be a good metric as the scale of sales differs across stores.
    - But, it can be a good starting point.

2. Total relative growth irrespective of seasons and trends
    - Basically percentage growth of sales from first week to last week.
    - This is relatively a better metric compared to the previous one. But, it might still be susceptible to volatility in first and last weeks.

3. Total relative growth in terms of trend only
    - What this metric does is fits a linear regression model to the growth of sales over time.
    - And then, the slope of the regression line is this metric.
    - This is a better metric than both the previous ones, because it accounts for all the data along with its trend.

4. Stability/volatility of sales
    - This metric analyzes the volatility of sales relative to the trend.
    - It is measured by the standard deviation of the residuals of seasonal decomposition of sales.
    - Note: Since the scale of sales differs across stores, I normalize the residuals to bring them on scale of 1 to -1.
    - Then their standard deviation is multiplied by 100 to give us final percentage volatility.

5. Composite score based on all the above metrics
    - This is the final metric that combines all the above metrics.
    - It is calculated by taking the weighted average of all the metrics.
    - The weights are based on the importance of each metric.
        - Average sales: 5%
        - Relative percentage growth: 25%
        - Linear Trend slope: 60%
        - Volatility: 10%

### Calculating all metrics and corresponding store ranks

### Average Weekly Sales

### Percentage Growth in Sales

### Linear growth in terms of Trend of Weekly Sales

### Volatility of Sales

### Composite Metric

### Conclusions

- By analyzing the composite score rank, stores [39, 4, 41, 13] are the top 5 performers in terms of sales and stores [15, 27, 14, 36, 35] seem to be the worst performers.

## Checking correlation between unemployment, fuel_price and cpi

### Observations
1. CPI and Fuel price are strongly positively correlated with each other for ALL stores with average Pearson correlation coefficient of 0.814. This is intuitive because fuel pice is generally considered when calculating CPI.
2. Unemployment and CPI are negatively correlated for most stores. For 75% of then stores, the correlation is greater in magnitude than 0.73 and for 85% of the stores it's greater in magnitude than 0.51. But, for the rest of the stores, the correlation gets closer to zero. And for store 24, the correlation is strongly positive with the coefficient being 0.86
3. Fuel Price and Unemployment are negatively correlated for most stores. This correltion isn't as strong as Unemployment and CPI. For 75% of then stores, the correlation is greater in magnitude than 0.53. But, for the rest of the stores, the correlation gets closer to zero. And for store 24, the correlation is strongly positive with the coefficient being 0.6

## PCA with CPI, Fuel Price, and Unemployment

### Why?
- PCA is used for dimensionality reduction. And while it may seem like we don't have that high dimensional data with only 5 features, but the fact that we are forecasting the sales store wise makes it so that we have only 143 rows/observations per store with 5 features.
- And that's too little data for us to consider 5 exogenous variables. So we can try to reduce the dimensionality of our data and see if it works.



### Conclusion/Observations

- The 3 features cpi, unemployment and fuel_price are reduced to 2 principal components which on average (across all stores) explains 97% variance across the 3 features.
- The minimum of this total explained various only drops to 93% across all stores. Which is pretty good.
- When I tried reducing the features to just 1 principal component, I got worse results where on average (across all stores) the variance explained was only 83%

## Stationarity

- ADF test
- KPSS test

### Transformations

#### Observations

- From manual inspection atleast, 1st and 2nd differencing make the series mostly stationary. However, the holiday effect is still present.
- Rolling averages are not helping much.

### Seasonal Decomposition of Differences

#### Observations

- STL decomposition of diff 1 shows good results. It may look like there's a trend, but comparing it's range to the range of sales diff 1, it is insignificant.
- MSTL would have been promising for seasonal periods of 5 (1 month) and 52 weeks (1 year). But, since our years are not fully divisible into whole weeks, it is difficult to capture seasonality. Same for monthly seasonality.

### Seasonal Differencing

#### Observations

- Holidays in this case repeat every 365 days (a year). But, unfortunately, we have weekly data and can only use 52 or 53 weeks for differencing instead of something like 52.5 days which would be 1 proper year.
- That's why, we can observe few peculiarities: for some holidays, the 52 week differencing nullifies the holiday effect boost (excluding the general updards trend ofcourse) and for the rest, it doesn't nullify the effect due to reasons mentioned in previous point. 
- Same for 53 weeks differencing. For some holidays, it nullifies the holiday effect boost and for the rest, it doesn't.

### ADF and KPSS test for stationarity

#### ADF for 1st order differences

##### Observations

- Maximum p-value for the storewise sales is < 0.0027 which is obviously very low than the 0.05 threshold.
- The max ADF statistic value is lower than the minimum value of 5% critical value. That implies, for ALL stores, the ADF test statistic is less than 5% critical value.
- Hence, for 1st order differencing, we can confidently reject the null hypothesis that the series is non-stationary for all stores.

#### ADF for 2nd order differences

##### Observations

- Except for stores 33 and 38, all stores have p-value less than 0.05 threshold.
- Similary, except for stores 33 and 38, all stores have ADF statistic value less than 5% critical value.
- These stores are an exception as they don't follow the general trends and seasonality found in other stores
- So, for rest of the stores, we can confidently reject the null hypothesis and conclude that the storewise sales are stationary.

#### KPSS test for 1st difference

##### Observations

- Unlike convention, for KPSS test, failure to reject null hypothesis implies that the series is stationary.
- Except for store 16, all stores have p-value more than 0.05 threshold.
- Similary, except for store16, all stores have ADF statistic value more than 5% critical value.
- This store is an exception as it doesn't follow the general trends and seasonality found in other stores
- So, for rest of the stores, we can don't have enough evidence to reject the null hypothesis and conclude that the storewise sales are stationary.

#### KPSS test for 2nd difference

##### Observations

- The results for 2nd difference are same as those for 1st difference.
- Except for store 16, all stores have p-value more than 0.05 threshold.
- Similary, except for store16, all stores have ADF statistic value more than 5% critical value.
- This store is an exception as it doesn't follow the general trends and seasonality found in other stores
- So, for rest of the stores, we can don't have enough evidence to reject the null hypothesis and conclude that the storewise sales are stationary.

## Auto-correlation and Partial Autocorrelation

#### Observations

From visual inspection of ACF and PACF plots for regular, 1st and 2nd order differenced sales, a few candidates for AR and MA orders are identified.

- ARIMA candidates
    - Difference 1 (d = 1)
        - AR orders (PACF) [6]
        - MA orders (ACF) [4, 5]
    - Difference 2 (d = 2)
        - AR orders (PACF) [6, 9]
        - MA orders (ACF) [4, 5]
    
- SARIMA candidates
    - Seasonal Difference 1 (D = 1)
        - AR orders (PACF) [3]
        - MA orders (ACF) [5]

From these candidates, these ARIMA and SARIMA models are selected:

- ARIMA
    - (6, 1, 4)
    - (6, 1, 5)
    - (6, 2, 4)
    - (6, 2, 5)
    - (9, 2, 4)
    - (9, 2, 5)

- SARIMA
    - (6, 1, 4), (2, 1, 5, 52)
    - (6, 1, 5), (2, 1, 5, 52)
    - (6, 2, 4), (2, 1, 5, 52)
    - (6, 2, 5), (2, 1, 5, 52)
    - (9, 2, 4), (2, 1, 5, 52)
    - (9, 2, 5), (2, 1, 5, 52)

