import time
import json
import requests
import jwt
from google_purchase.responses import GoogleResponse, GooglePurchaseResponse, GoogleVerificationError


class GooglePurchaseProduct(object):

    def __init__(self, google_api_file_path: str) -> None:
        with open(google_api_file_path) as fh:
            json_data = json.load(fh)
            self.key = json_data.get("private_key")
            
            self.claims = {
            "iss": json_data.get("client_email"),
            "scope": "https://www.googleapis.com/auth/androidpublisher",
            "aud": json_data.get("token_uri"),
            }
        self.header = {"alg":"RS256", "typ":"JWT"}

    def verify_purchase(self, package_name: str, product_id: str, purchase_token: str, expiration: int =120) -> GooglePurchaseResponse:
        claim_start = time.time()
        self.claims["exp"] = claim_start + expiration
        self.claims["iat"] = claim_start

        token = jwt.encode(self.claims, self.key, headers=self.header, algorithm="RS256")
        params = {
            "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
            "assertion": token
        }

        r = requests.post("https://www.googleapis.com/oauth2/v4/token", data=params)
        r.raise_for_status()
        access_token = r.json()["access_token"]

        headers = {
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json"
        }

        url = f"https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{package_name}/purchases/products/{product_id}/tokens/{purchase_token}" #"{google_verify_purchase_endpoint}/{product_id}/tokens/{subscription_token}"
        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            return GooglePurchaseResponse(response.json())
        
        raise GoogleVerificationError(response.json())

    def consume_purchase(self, package_name: str, product_id: str, purchase_token: str, expiration: int = 120) -> GoogleResponse:
        claim_start = time.time()
        self.claims["exp"] = claim_start + expiration
        self.claims["iat"] = claim_start

        token = jwt.encode(self.claims, self.key, headers=self.header, algorithm="RS256")
        params = {
            "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
            "assertion": token
        }

        r = requests.post("https://www.googleapis.com/oauth2/v4/token", data=params)
        r.raise_for_status()
        access_token = r.json()["access_token"]

        headers = {
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json"
        }

        url = f"https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{package_name}/purchases/products/{product_id}/tokens/{purchase_token}:consume"
        response = requests.post(url=url, headers=headers)

        if response.status_code == 200:
            return GoogleResponse({"message":"purchase consumed"})
        
        raise GoogleVerificationError(response.json())
    
    def acknowledge_purchase(self, package_name: str, product_id: str, purchase_token: str, payload: str = "", expiration: int = 120) -> GoogleResponse:
        claim_start = time.time()
        self.claims["exp"] = claim_start + expiration
        self.claims["iat"] = claim_start

        token = jwt.encode(self.claims, self.key, headers=self.header, algorithm="RS256")
        params = {
            "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
            "assertion": token
        }

        r = requests.post("https://www.googleapis.com/oauth2/v4/token", data=params)
        r.raise_for_status()
        access_token = r.json()["access_token"]

        headers = {
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json"
        }

        url = f"https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{package_name}/purchases/products/{product_id}/tokens/{purchase_token}:acknowledge"
        response = requests.post(url=url, headers=headers, data=json.dumps({"developerPayload":payload}))

        if response.status_code == 200:
            return GoogleResponse({"message":"purchase acknowledge"})
        
        raise GoogleVerificationError(response.json())
