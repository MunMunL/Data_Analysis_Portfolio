# Google Trends and Data Visualisation

Code: https://github.com/MunMunL/Data_Analysis_Portfolio/blob/main/Google_Trends/Google%20Trends%20and%20Data%20Visualisation.ipynb

## Goal

Google Trends gives an estimate of search volume. I look to explore if there are patterns in Google's search volume on these datasets with these different datasets:

* How search volume for "Bitcoin" relates to the price of "Bitcoin"
* How search volume for a hot stock like Tesla relates to that stock price
* How seaches for "Unemployment Benefits" vary with the actual unemployment rate in the United States?

## Description

Data Sources:

* [Unemployment Rate from FRED](https://fred.stlouisfed.org/series/UNRATE/)
* [Google Trends](https://trends.google.com/trends/explore)
* [Yahoo Finance for Tesla Stock Price](https://finance.yahoo.com/quote/TSLA/history?p=TSLA&guccounter=1&guce_referrer=aHR0cDovL2xvY2FsaG9zdDo4ODg4Lw&guce_referrer_sig=AQAAAKJMDFKZB-sPpzyK0tFAV9_EDUmSy30FjH30IfcsG1q01IDgyivAmaZ3XS3NAciPV0ooBGndSAv0lAm7jojnXm-2MXV643Zx93EkMt9F4DUzD_qe4_82g4UiR9OK-xIT3TuKZ5dL0LvfG-GjVd20CPcPJCGtJw7W82Xl8u2x7qTA)
* [Yahoo Finance for Bitcoin Stock Price](https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD)

The project focused on analysing Google's search volume against the stock price for Bitcoin and Tesla and the unemplyment rate in the United States. The dataset included:

* Monthly number of web searches on Tesla and Tesla monthly closing stock prices
* Monthly number of web searches on Bitcoin and Bitcoin daily closing stock prices
* Monthly number of web searches on benefits and monthly reported unemployment rates in the US

The project involved loading the data, cleaning and preprocessing it, performing exporatory data analysis, analysing the correlation against the above datasets.
  
## Technology used

Technology: Python, Pandas, Matpltlib

Skills: data cleaning, data analysis, data manipulation, data visualisation with Matplotlib (time series data across two axis)
