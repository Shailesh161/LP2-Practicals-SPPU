class StockTradingExpertSystem:
    def __init__(self):
        self.stock_symbol = None
        self.buying_power = None
        self.investment_duration = None
        self.trading_experience = None

    def set_trading_details(self):
        self.stock_symbol = input("Enter the stock symbol you want to trade: ")
        self.buying_power = float(input("Enter your buying power (in USD): "))
        self.investment_duration = input("Enter your investment duration (short-term/long-term): ")
        self.trading_experience = input("Enter your trading experience level (beginner/intermediate/advanced): ")

    def recommend_trades(self):
        print("Recommendation for stock trading:")
        print(f"Stock Symbol: {self.stock_symbol}")
        print(f"Buying Power: {self.buying_power} USD")
        print(f"Investment Duration: {self.investment_duration}")
        print(f"Trading Experience: {self.trading_experience}")

        # Your decision-making logic based on the provided details
        if self.trading_experience.lower() == "beginner":
            print("As a beginner, it's recommended to focus on long-term investments.")
            if self.investment_duration.lower() == "long-term":
                print("Consider buying and holding blue-chip stocks or index funds.")
            else:
                print("Short-term trading involves higher risk, consider paper trading or ETFs.")
        elif self.trading_experience.lower() == "intermediate":
            print("As an intermediate trader, diversify your portfolio and consider both short-term and long-term investments.")
            if self.buying_power >= 5000:
                print("You can consider individual stocks or ETFs.")
            else:
                print("ETFs or mutual funds may be suitable for your budget.")
        elif self.trading_experience.lower() == "advanced":
            print("As an advanced trader, you can explore options trading, margin trading, and more sophisticated strategies.")
            if self.buying_power >= 10000:
                print("Consider options trading for leverage and risk management.")
            else:
                print("Continue building your portfolio with a focus on risk management.")
        else:
            print("Invalid trading experience level provided.")

# Example usage:
expert_system = StockTradingExpertSystem()
expert_system.set_trading_details()
expert_system.recommend_trades()
