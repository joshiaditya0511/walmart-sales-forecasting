---
title: "About This Project"
---

# About This Project

Welcome to my analysis of Walmart store weekly sales. This project dives into various aspects of the sales data to uncover patterns and insights. This analysis uses a dataset from [Kaggle](https://www.kaggle.com/datasets/rutuspatel/walmart-dataset-retail).

```{caution}
**Disclaimer:** Data used purely for academic purposes.
```

```{note}
The code used for my analysis and forecasting is integrated throughout the pages. If you'd like to view the raw Jupyter notebooks I used or see how I deployed this project as a webpage, feel free to check out my [GitHub repository](https://github.com/joshiaditya0511/walmart-sales-forecasting) for this project.
```

## Get in Touch

If you have any questions, suggestions, or feedback, please connect with me:
- [Personal Website](https://www.adityajoshi.in)
- [LinkedIn](https://www.linkedin.com/in/joshiaditya0511)

## Using This Site

### Best Viewing Experience

For the best experience, please view this site on a desktop or laptop browser. Although the site is accessible on mobile devices, it is not fully optimized for them. If you are using a mobile phone, consider selecting the "Desktop Site" option in your browser and viewing in landscape mode.

### Table of Contents

Use the table of contents available on the left panel to navigate through the project's sections. An intra-page table of contents on the right panel further helps you quickly access different parts of the analysis.

## Future Work

Below are some planned enhancements and additional analyses that I intend to incorporate in future iterations of this project.

```{note}
The following tasks are aimed at deepening the insights in both the Exploratory Data Analysis and the forecasting methodology.
```

### Extra EDA To Do

1. **Holiday Flags**
   - **Pre and Post-Holiday Analysis:**  
     Examine sales trends two weeks before and after holiday flags.
   - **Holiday Impact Validation:**  
     Assess whether all holiday flags truly result in a boost to sales.
   - **Quantification of Holiday Influence:**  
     Quantify which holiday flags drive the most and least sales.
   - **Store-Specific Effects:**  
     Investigate if certain holiday flags have a stronger effect on sales for specific stores by analyzing relative sales growth within a ±2 week window around each holiday. This analysis will also cover significant dates that boost sales but are not explicitly marked as holidays.
   - **Anomaly Detection:**  
     Utilize the Darts library's anomaly detector to identify actual holiday events that boost sales.

2. **Seasonal Trends**
   - **Enhanced Smoothing:**  
     Explore methods to further smooth out the seasonal effects. Given the limited (~3 years) data span, capturing clear seasonal patterns is challenging, as many effects seem to derive from yearly repeating irregularities (e.g., holidays). Techniques such as FFT, alternative decomposition methods, or refined anomaly detection will be considered.

3. **Hypothesis Testing**
   - **Correlation Validation:**  
     Apply hypothesis testing to validate the linear correlation between:
     - Weekly sales and CPI.
     - CPI, unemployment, and fuel price.

### Forecasting To Do

1. **Incorporate Holiday Anomalies:**  
   Integrate the Darts library’s anomaly detector and corresponding forecaster to explicitly incorporate actual holiday events that boost sales into the forecasting models.
2. **Residual Analysis:**  
   Analyze the residuals of the forecasts using the Ljung-Box test.
3. **Additional Loss Metrics:**  
   Consider introducing another loss metric to complement MAE and provide a more rounded evaluation of model performance.
4. **SHAP Analysis:**  
   Use SHAP to analyze and interpret the models post training.
5. **Alternative Forecasting Techniques:**  
   Experiment with STL and MSTL forecasting methods to potentially improve seasonal decomposition and prediction accuracy.

---

*I plan to update this section as I make progress on these tasks and incorporate further enhancements into the project.*
