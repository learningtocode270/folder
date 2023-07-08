## Ask for greeting
greeting = input("Greeting: ")
greeting = greeting.lower()

if "hello" in greeting:
    print("$0")

elif greeting[0] == "h":
    print ("$20")

else:
    print ("$100")