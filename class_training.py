class Restaurant:
    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restauracja nazywa sie {self.restaurant_name}")
        print(f"Oferuje kuchnie {self.cuisine_type}")

    def open_restaurant(self):
        print("Restauracja jest otwarta od 12 do 22")

my_restaurant = Restaurant("DaGrasso", "Italian")
my_restaurant1 = Restaurant("LeBurger", "American")
my_restaurant2 = Restaurant("Tutti_santi", "Italian")
my_restaurant3 = Restaurant("Zarelko", "Fast_food")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant1.describe_restaurant()
my_restaurant2.describe_restaurant()
my_restaurant3.describe_restaurant()
