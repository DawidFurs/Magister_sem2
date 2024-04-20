class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Area: {self.area} sq. meters\nRooms: {self.rooms}\nPrice: {self.price} USD\nAddress: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return super().__str__() + f"\nPlot: {self.plot} sq. meters"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return super().__str__() + f"\nFloor: {self.floor}"


# Tworzenie instancji obiektów
house = House(area=200, rooms=5, price=300000, address="123 Main St, City1", plot=500)
flat = Flat(area=80, rooms=3, price=150000, address="456 Elm St, City2", floor=3)

# Wyświetlenie obiektów
print("House:")
print(house)
print("\nFlat:")
print(flat)