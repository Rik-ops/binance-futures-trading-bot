# Binance Futures Testnet Trading Bot

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Input validation
- Logging
- Error handling

## Installation

pip install -r requirements.txt

## Setup

Create a .env file

API_KEY=your_api_key
API_SECRET=your_api_secret

## Run Market Order

python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001

## Run Limit Order

python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 150000