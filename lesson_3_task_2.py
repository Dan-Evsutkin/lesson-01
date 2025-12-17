from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79999999999"),
    Smartphone("Samsung", "Galaxy S21", "+79999999999"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79999999999"),
    Smartphone("Huawei", "P40", "+79999999999"),
    Smartphone("Google", "Pixel 6", "+79999999999"),
]

for phone in catalog:
    print(phone.brand, phone.model, phone.number)