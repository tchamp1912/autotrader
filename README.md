# The Autotrader

## API Used

	Brokerage API: tdameritrade Python Wrapper
	Historical Data API: Alpha Vantage / Polygon.io
	Technical Indicators: Alpha Vantage / Custom
	Python Package Manager: Poetry


## Development Plan

	1. Create data aggregation system for current and historical stock data.
	2. Develop basic quantitative trading strategy from technical indicators.
	3. Implement trading strategy programatically, outputting buy or sell orders within pre-determined stocks.
	4. Backtest and tune strategy to achieve optimal "dumb" predictive model from aggregated historical data.
	5. Using backtest results, train RNN (recurrent nueral network) from labeled results and dumb predictive model decisions.
	6. Experiment with RNN parameters to maximize gain over testing data.
	7. Integrate dumb model and RNN.
	8. Test aggregated model.
	9. Scrape Wall Street Journal for historical news articles for desired stocks.
	10. Create sentiment analysis LSTM (long short-term memory) model from scraped data.
	11. Retrain RNN with sentiment analysis input.

## Technical Indicators

	* 50 Day Weighted Average
	* 200 Day Weighted Average

## Trading Strategy


## Variables

	* Capital
	* Portfolio
	* Volatilty


