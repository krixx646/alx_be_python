# Weather advice

advice = input("What's the weather like today? (sunny/rainy/cold): ").lower().strip()

if advice == "sunny":
    result = f"Wear a t-shirt and sunglasses."
elif advice == "rainy":
    result = f"Don't forget your umbrella and a raincoat."
elif advice == "cold":
    result = f"Make sure to wear a warm coat and a scarf."
else:
    result = f"Sorry, I don't have recommendations for this weather."
    
print(result)