from address import Address
from mailing import Mailing

to_addr = Address("123456", "Москва", "Ленинский проспект", "10", "15")
from_addr = Address("654321", "Санкт-Петербург", "Невский проспект", "20", "30")
mail = Mailing(to_addr, from_addr, 250.0, "TRACK123456")

print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
      f"в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. "
      f"Стоимость {mail.cost} рублей.")