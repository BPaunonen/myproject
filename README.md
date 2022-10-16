# Delivery fee calculator

## How to run the project

Activate Python virtual environment with the following command:

```sh
. venv/bin/activate
```

Run http server with the following command:

```sh
flask --app app run  
```

## How to send a request

Send POST http request to the http://127.0.0.1:5000/DeliveryfeeCalc

With Content-Type: application/json HEADER and an example payload

```json
{
    "cart_value": 790, 
    "delivery_distance": 2235, 
    "number_of_items": 4,
    "time": "2021-10-12T13:00:00Z"
}
```
