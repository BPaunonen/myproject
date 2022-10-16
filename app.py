# from flask import Flask, request
# from markupsafe import escape
# app = Flask(__name__)

# @app.post("/DeliveryfeeCalc")
# def del_fee():
#     request_data = request.json
#     cart_value = request_data['cart_value']
#     delivery_distance = request_data['delivery_distance']
#     number_of_items = request_data['number_of_items']
#     time = request_data['time']
#     delivery_fee = calculate_delivery_fee(cart_value, delivery_distance, number_of_items, time)
#     return {"delivery_fee": delivery_fee}2

# @app.post("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

# def calculate_delivery_fee(cart_value, delivery_distance, number_of_items, time):
#     return 200
# If the cart value is less than 10€, a small order surcharge is added to the delivery price. The surcharge is the difference between the cart value and 10€. For example if the cart value is 8.90€, the surcharge will be 1.10€.
def main():
    print("Shipping Calculator")
    cart_value = surcharge(10, 8.9)
    return cart_value

  def surcharge(threshold, cart_value):
        if cart_value < threshold:
            return cart_value + (threshold - cart_value)
        else:
            return cart_value



if __name__ == "__main__":
    main()
  

print(cart_value)
# A delivery fee for the first 1000 meters (=1km) is 2€. If the delivery distance is longer than that, 1€ is added for every additional 500 meters that the courier needs to travel before reaching the destination. Even if the distance would be shorter than 500 meters, the minimum fee is always 1€.
# Example 1: If the delivery distance is 1499 meters, the delivery fee is: 2€ base fee + 1€ for the additional 500 m => 3€
# Example 2: If the delivery distance is 1500 meters, the delivery fee is: 2€ base fee + 1€ for the additional 500 m => 3€
# Example 3: If the delivery distance is 1501 meters, the delivery fee is: 2€ base fee + 1€ for the first 500 m + 1€ for the second 500 m => 4€
# If the number of items is five or more, an additional 50 cent surcharge is added for each item above four
# Example 1: If the number of items is 4, no extra surcharge
# Example 2: If the number of items is 5, 50 cents surcharge is added
# Example 3: If the number of items is 10, 3€ surcharge (6 x 50 cents) is added
# The delivery fee can never be more than 15€, including possible surcharges.
# The delivery is free (0€) when the cart value is equal or more than 100€.
# During the Friday rush (3 - 7 PM UTC), the delivery fee (the total fee including possible surcharges) will be multiplied by 1.1x. However, the fee still cannot be more than the max (15€).
