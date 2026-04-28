from textblob import TextBlob

print("Welcome!")
name = input("What's your name?: ")
print(f"Hello, {name}! ")
print("Type exit to quit.\n")

while True:
    sentence = input("Your sentence: ")
    if sentence.lower() == "exit":
        print(f"\nGoodbye, {name}!")
        break
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        print("Positive sentiment detected!\n")
    elif sentiment<0:
        print("Negative sentiment detected!\n")
    else:
        print("Neutral sentiment detected!\n")
        