def sos():
    import pywhatkit
    import speak
    # speak.speak("enter the number")
    # x=int(input("ENTER THE NUMBER :"))
    # speak.speak("enter the message what you need to send")
    # y=input("ENTER THE DATA NEED TO SEND :")
    speak.speak("enter the time to send the information")
    speak.speak("enter the time in hours")
    a=int(input("ENTER THE TIME IN HOURS :"))
    speak.speak("enter the time in minutes")
    b=int(input("ENTER THE TIME IN MINUTES :"))
    try:
        pywhatkit.sendwhatmsg("+916374912478","help me i am problem",a,b)
        speak.speak("message send sucessfully")
        print("success")
        speak.speak("message successfully send to police")
    except:
        speak.speak("failed to send the message")
        print("mission fail")