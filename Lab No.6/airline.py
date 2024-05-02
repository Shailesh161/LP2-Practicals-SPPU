class AirlineExpertSystem:
    def __init__(self):
        self.current_city = None
        self.destination_city = None
        self.travel_date = None
        self.flexible_dates = None
        self.preferred_class = None

    def set_travel_details(self):
        self.current_city = input("Enter your current city: ")
        self.destination_city = input("Enter your destination city: ")
        self.travel_date = input("Enter your travel date (YYYY-MM-DD): ")
        flexible_input = input("Are you flexible with dates? (Yes/No): ")
        self.flexible_dates = flexible_input.lower() == "yes"
        self.preferred_class = input("Enter your preferred class (Economy/Business/First): ")

    def recommend_flights(self):
        print("Recommendation for your travel:")
        print(f"From: {self.current_city}  To: {self.destination_city}")
        print(f"Travel Date: {self.travel_date}")
        print(f"Flexible Dates: {'Yes' if self.flexible_dates else 'No'}")
        print(f"Preferred Class: {self.preferred_class}")

        # Your decision-making logic based on the provided details
        if self.current_city.lower() == "delhi" and self.destination_city.lower() == "mumbai":
            print("Recommended flights from Delhi to Mumbai:")
            if self.flexible_dates:
                print("1. IndiGo - 7:00 AM (Flexi Fare)")
                print("2. Air India - 9:30 AM (Standard Fare)")
            else:
                print("1. Air India - 9:30 AM (Standard Fare)")
        elif self.current_city.lower() == "mumbai" and self.destination_city.lower() == "delhi":
            print("Recommended flights from Mumbai to Delhi:")
            if self.flexible_dates:
                print("1. SpiceJet - 8:00 AM (Flexi Fare)")
                print("2. Vistara - 10:30 AM (Standard Fare)")
            else:
                print("1. SpiceJet - 8:00 AM (Standard Fare)")
        else:
            print("Sorry, we currently don't have recommendations for this route.")

# Example usage:
expert_system = AirlineExpertSystem()
expert_system.set_travel_details()
expert_system.recommend_flights()
