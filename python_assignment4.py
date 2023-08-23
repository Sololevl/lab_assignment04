class FT:
    def __init__(self):
        self.data = [
            {"Flight ID": "AI161E90", "From": "BLR", "To": "BOM", "Price": 5600},
            {"Flight ID": "BR161F91", "From": "BOM", "To": "BBI", "Price": 6750},
            {"Flight ID": "AI161F99", "From": "BBI", "To": "BLR", "Price": 8210},
            {"Flight ID": "VS171E20", "From": "JLR", "To": "BBI", "Price": 5500},
            {"Flight ID": "AS171G30", "From": "HYD", "To": "JLR", "Price": 4400},
            {"Flight ID": "AI131F49", "From": "HYD", "To": "BOM", "Price": 3499},
        ]

    def search_by_city(self, city):
        f_f = []
        for flight in self.data:
            if flight["From"] == city or flight["To"] == city:
                f_f.append(flight)
        return f_f

    def search_flights_from_city(self, city):
        f_f = []
        for flight in self.data:
            if flight["From"] == city:
                f_f.append(flight)
        return f_f

    def search_flights_between_cities(self, city1, city2):
        f_f = []
        for flight in self.data:
            if flight["From"] == city1 and flight["To"] == city2:
                f_f.append(flight)
        return f_f

    def print_fli(self, flights):
        if not flights:
            print(" flights not found.")
        else:
            print("Flight ID\tFrom\tTo\tPrice")
            for flight in flights:
                print(
                    flight["Flight ID"] + "\t" + flight["From"] + "\t" + flight["To"] + "\t" + str(flight["Price"]))

def main():
    f_t = FT()
    print("MRIDUL MADHAV JINDAL")
    print("E22CSEU1116")
    print("\nSearch:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        city = input("Enter the city: ")
        f_f = f_t.search_by_city(city)
        f_t.print_fli(f_f)
    elif choice == '2':
        city = input("Enter the city: ")
        f_f = f_t.search_flights_from_city(city)
        f_t.print_fli(f_f)
    elif choice == '3':
        city1 = input("Enter the source city: ")
        city2 = input("Enter the destination city: ")
        f_f = f_t.search_flights_between_cities(city1, city2)
        f_t.print_fli(f_f)
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
