class Phone:
    def __init__(self, brand, model, price, has_5g=False):
        self.brand = brand
        self.model = model
        self.price = price
        self.has_5g = has_5g

    def __str__(self):
        g_info = "Supports 5G" if self.has_5g else "No 5G"
        return f"{self.brand} {self.model} - ${self.price} ({g_info})"

phone1 = Phone("Apple", "iPhone 14", 999, has_5g=True)
print(phone1)

class Hwawei(Phone):
    def __init__(self, model, price, has_5g=False):
        super().__init__("Huawei", model, price, has_5g)
        self.warranty_years = 2
    def __str__(self):
        return super().__str__() + f" - Warranty: {self.warranty_years} years"
    def warranty_info(self):
        return f"{self.brand} {self.model} comes with a {self.warranty_years}-year warranty."
print(Hwawei("P50 Pro", 899, has_5g=True))