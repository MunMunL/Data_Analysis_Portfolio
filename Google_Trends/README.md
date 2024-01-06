# Google Trends and Data Visualisation

Code: https://github.com/MunMunL/Data_Analysis_Portfolio/blob/main/Google_Trends/Google%20Trends%20and%20Data%20Visualisation.ipynb

## Goal

Google Trends gives an estimate of search volume. I look to explore if there are patterns in Google's search volume on these datasets with these different datasets:

* How search volume for "Bitcoin" relates to the price of "Bitcoin"
* How search volume for a hot stock like Tesla relates to that stock price
* How seaches for "Unemployment Benefits" vary with the actual unemployment rate in the United States?

Data Sources:

* [Unemployment Rate from FRED](https://fred.stlouisfed.org/series/UNRATE/)
* [Google Trends](https://trends.google.com/trends/explore)
* [Yahoo Finance for Tesla Stock Price](https://finance.yahoo.com/quote/TSLA/history?p=TSLA&guccounter=1&guce_referrer=aHR0cDovL2xvY2FsaG9zdDo4ODg4Lw&guce_referrer_sig=AQAAAKJMDFKZB-sPpzyK0tFAV9_EDUmSy30FjH30IfcsG1q01IDgyivAmaZ3XS3NAciPV0ooBGndSAv0lAm7jojnXm-2MXV643Zx93EkMt9F4DUzD_qe4_82g4UiR9OK-xIT3TuKZ5dL0LvfG-GjVd20CPcPJCGtJw7W82Xl8u2x7qTA)
* [Yahoo Finance for Bitcoin Stock Price](https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD)

## Results

* How search volume for "Bitcoin" relates to the price of "Bitcoin"

  Big increases in searches were closely accompanied by big increases in Bitcoin prices till it reached an all time high in 2018. Bitcoin was a hot topic during 2017 and early 2017, so matched the high search volumes. However during the next spike in price in 2019, the search trend didn't peak at the same rate as the price, likely due to Bitcoin being a fairly well known item/topic.
  
* How search volume for a hot stock like Tesla relates to that stock price

  Tesla's increase in search trend follows the increase in stock prices with the spike in Mar 2016 coincides with when the Tesla Model 3 was released.
  
* How seaches for "Unemployment Benefits" vary with the actual unemployment rate in the United States?

  The spikes in searches for 'Unemployment benefit' generally happens at year end which shows potential seasonality in the job market.
The financial crisis in 2008 caused a massive spike in unemployment.
Between 2008 and 2014, the there were big spikes in searches not linked to increase in unemployment rates so there is likely another factor impacting the search trend. The search volumes fluctuates month on month, a rolling average can help smooth it out to help identify other trends.

  The chart for a 6 month rolling average indicates that the searches for 'Unemployment Benefit' happens before the unemployment rate goes up. Similarly, the searched for 'Unemployment Benefit' goes down first before the unemplyment rate goes down.
  The US unemployment rate spiked dramatically in 2020 during COVID, significantly higher than the unemployment rate during the financial crisis in 2008.
  
## Technology used

Technology: Python, Pandas, Matpltlib

Skills: data cleaning, data analysis, data manipulation, data visualisation with Matplotlib (time series data across two axis, scatter plots)
