import click
import os

from dotenv import load_dotenv
from bot.client import BinanceClient
from bot.orders import create_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logger

load_dotenv()
setup_logger()

@click.command()
@click.option('--symbol', required=True)
@click.option('--side', required=True)
@click.option('--order_type', required=True)
@click.option('--quantity', required=True, type=float)
@click.option('--price', type=float)

def run(symbol, side, order_type, quantity, price):

    try:
        side = validate_side(side)
        order_type = validate_order_type(order_type)

        if order_type == "LIMIT" and price is None:
            raise ValueError("Price is required for LIMIT order")

        client = BinanceClient(
            os.getenv("API_KEY"),
            os.getenv("API_SECRET")
        )

        response = create_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print("\nORDER PLACED SUCCESSFULLY")
        print("Order ID:", response["orderId"])
        print("Status:", response["status"])
        print("Executed Qty:", response["executedQty"])

    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    run()