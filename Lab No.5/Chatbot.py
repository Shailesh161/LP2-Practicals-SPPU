import time

class Chatbot:
    def __init__(self):
        self.user_name = None
        self.user_age = None
        self.user_job = None
        self.user_hobbies = None
    
    def greet(self):
        print("Hello, I'm your friendly Chatbot - AI-Saathi!")
        time.sleep(1)        
    
    def get_user_info(self):
        self.user_name = input("What's your name? ")
        print(f"Nice to meet you, {self.user_name}!")
        time.sleep(1)        
        self.user_age = int(input("How old are you? "))
        self.categorize_age()
        time.sleep(1)       
        self.user_job = input("What do you do for a living? ")
        self.describe_job()
        time.sleep(1)        
        self.user_hobbies = input("What are your hobbies? ")
        time.sleep(1)       
        print("Thanks for sharing! Let's move on.")
        time.sleep(1)        
    
    def categorize_age(self):
        if 18 <= self.user_age <= 25:
            print("Ah, you're in the prime of your youth!")
        elif 26 <= self.user_age <= 40:
            print("You're in the midst of your professional life!")
        elif self.user_age > 40:
            print("You've gathered a wealth of experience!")
        else:
            print("You're young and full of potential!")       
    
    def describe_job(self):
        print(f"{self.user_job} sounds like an interesting profession!")
    
    def remind_lunch_or_dinner(self):
        response = input("Have you had your lunch/dinner? (yes/no) ").lower()
        if response == "yes":
            print("Great! Make sure to stay hydrated and take breaks.")
        else:
            print("Take a break and have a nutritious meal. Your health is important!")

    def ask_favorite_movie(self):
        self.favorite_movie = input("What's your favorite movie? ")
        print(f"Interesting choice! {self.favorite_movie} is a great film.")

    def ask_favorite_food(self):
        self.favorite_food = input("What's your favorite food? ")
        print(f"{self.favorite_food} sounds delicious!")

    def ask_dream_destination(self):
        self.dream_destination = input("What's your dream travel destination? ")
        print(f"{self.dream_destination} would be an amazing place to visit!")

    def ask_pet_preference(self):
        self.pet_preference = input("Do you have any pets? If yes, what kind? ")
        if self.pet_preference.lower() == "yes":
            print("Pets are wonderful companions!")
        else:
            print("That's okay, pets aren't for everyone.")

    def ask_recent_book(self):
        self.recent_book = input("What's the last book you read? ")
        print(f"{self.recent_book} seems like an interesting read!")

def main():
    chatbot = Chatbot()
    chatbot.greet()
    chatbot.get_user_info()
    chatbot.remind_lunch_or_dinner()
    chatbot.ask_favorite_movie()
    chatbot.ask_favorite_food()
    chatbot.ask_dream_destination()
    chatbot.ask_pet_preference()
    chatbot.ask_recent_book()

if __name__ == "__main__":
    main()
