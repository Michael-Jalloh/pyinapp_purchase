class GoggleResponse(object):
    def __init__(self, data) -> None:
        self.data = data
    
    def __str__(self) -> str:
        return f"GoogleResponse -> {self.data}"

class GogglePurrchaseResponse(object):
    def __init__(self, data: dict) -> None:
        self.data = data
        self.kind = data.get("kind","")
        self.purchaseTimeMillis = data.get("purchaseTimeMillis","")
        self.purchaseState = data.get("purchaseState")
        self.consumptionState = data.get("consumptionState")
        self.developerPayload = data.get("developerPayload")
        self.orderId = data.get("orderId")
        self.purchaseType = data.get("purchaseType")
        self.acknowledgementState = data.get("acknowledgementState")
        self.purchaseToken = data.get("purchaseToken","")
        self.productId = data.get("productId", "")
        self.quantity = data.get("quantity", 1)
        self.obfuscatedExternalAccountId = data.get("obfuscatedExternalAccountId")
        self.obfuscatedExternalProfileId = data.get("obfuscatedExternalProfileId")
        self.regionCode = data.get("regionCode")
        self.refundableQuantity = data.get("refundableQuantity")
    
    def __str__(self) -> str:
        return f"GooglePurchaseResponse -> {self.data}"
    
class GoogleVerificationError(Exception):
    def __init__(self, data) -> None:
        self.data = data
        super().__init__(str(self.data))