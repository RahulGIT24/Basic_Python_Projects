from geopy.geocoders import Nominatim
import time

# * Using Nominatim API
geolocator = Nominatim(user_agent="geoapiExcercises")

while True:
    # * Taking Zipcode input from user
    try:
        zipcode = input("Enter the Zipcode: ")
        # * Using geocode
        location = geolocator.geocode(zipcode)

        # * Displaying address details
        print(f"Zipcode: {zipcode}")
        print("Details of the zipcode")
        print(location)
    except Exception:
        print("Zipcode not found!!!")
        print("Make sure you are connected to the internet")
        time.sleep(3)
