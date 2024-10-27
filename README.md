# pyinapp_purchase
pyinapp_purchase is an open-source Python library designed to simplify and securely validate, consume and acknowledge in-app purchase tokens server side. This library provides an efficient and straightforward way to handle token verification, consumption and acknowledgement making it easier to manage app transactions and ensure validity directly from your backend. 
> Service Account Private Key from Google Cloud is need, as json file.

## Features
- Seamless Integration: Quickly integrate the validator into existing Python applications.
- Verification: Handles token verification directly with the Google Play Store API to ensure data authenticity.
- Consumption: Handles token consumption if token wasn't consume client side.
- Acknowledgement: Handles token acknowledgement.
- Error Handling: Provides clear feedback for successful or failed token validations.
- Lightweight and Performant: Minimal dependencies and optimized for fast, reliable performance.

## Installation
~~~
pip install pyinapp-purchase
~~~

## Usage
verifying purchase
```python
from google_purchase import GooglePurchaseProduct

google_inapp = GooglePurchaseProduct("google api.json")

package_name = "com.example.app"
product_id = "first_product"
purchase_token = "token"

data = google_purchase.verify_purchase(package_name, product_id, purchase_token)

print(data)
```
consume purchase
```python
from google_purchase import GooglePurchaseProduct

google_purchase = GooglePurchaseProduct("google api.json")

package_name = "com.example.app"
product_id = "first_product"
purchase_token = "token"

data = google_purchase.consume_purchase(package_name, product_id, purchase_token)

print(data)
```
acknowledge purchase
```python
from google_purchase import GooglePurchaseProduct

google_purchase = GooglePurchaseProduct("google api.json")

package_name = "com.example.app"
product_id = "first_product"
purchase_token = "token"

data = google_purchase.acknowledge_purchase(package_name, product_id, purchase_token)

print(data)
```
## Todo