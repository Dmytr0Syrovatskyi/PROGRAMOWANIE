class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Nieruchomość pod adresem {self.address} ({self.area} m2, {self.rooms} pokoje, cena: {self.price} zł)"

class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"Dom przy {self.address} | Powierzchnia: {self.area} m2 | Pokoje: {self.rooms} | Działka: {self.plot} m2 | Cena: {self.price} zł"

class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Mieszkanie przy {self.address} | Piętro: {self.floor} | Powierzchnia: {self.area} m2 | Pokoje: {self.rooms} | Cena: {self.price} zł"

if __name__ == '__main__':
    moj_dom = House(area=150.5, rooms=5, price=1200000.0, address="Kwiatowa 12, Poznań", plot=800)
    moje_mieszkanie = Flat(area=55.0, rooms=2, price=650000.0, address="Długa 5/10, Gdańsk", floor=3)

    print(moj_dom)
    print(moje_mieszkanie)