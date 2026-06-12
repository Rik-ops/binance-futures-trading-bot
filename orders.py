import logging

def create_order(client,
                 symbol,
                 side,
                 order_type,
                 quantity,
                 price=None):

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    logging.info(f"Request: {params}")

    response = client.place_order(**params)

    logging.info(f"Response: {response}")

    return response