import pyttsx3 # Importing the pyttsx3 module for text-to-speech conversion

# Main entry point of the program
if __name__ == "__main__":
    print("Hello! I'm VakyaVani, created by Charmi, and I'm ready to bring your words to life. What would you like me to read for you?")
    speaker = pyttsx3.init()    # Initialize the pyttsx3 text-to-speech engine

    speaker.say("Hello! I'm VakyaVani, created by Charmee, and I'm ready to bring your words to life. What would you like me to read for you?")
    speaker.runAndWait()   # Run the speech engine to actually speak the queued text

    # Start an infinite loop to keep prompting the user for input
    while True:
        x = input("Enter what do you want me to speak (or type 'q' to quit) :")
        if x.lower() == "q":
            speaker.say("Goodbye! Have a great day.Words are resting now. Talk to you later!")
            speaker.runAndWait()
            break
        speaker.say(" ")
        speaker.say(x) # Use the speaker to say the user's input
        speaker.runAndWait()  #Run the speech engine to speak the user's input
