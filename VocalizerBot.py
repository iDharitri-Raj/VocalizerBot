import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    print("Welcome to Lexiloq 1.1 Created by Dharitri Raj")
    engine.say("Welcome to Lexiloq 1.1 Created by Dharitri Raj")
    engine.runAndWait()

    while True:
        x = input("Enter command to say: ")
        if x.lower == "bye":
            engine.say(x)
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
