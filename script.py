from time import sleep
import serial
import speech_recognition as sr

# Resetting the board
with serial.Serial('COM3', 9600) as ser:
    sleep(1)
    print("Communication with board established")

    # Send data to board
    def ring_arduino(rx):
        rx = str(rx).lower().strip()
        if "light" in rx and "on" in rx :
            tx = 1
        elif "light" in rx and "off" in rx:
            tx = 2
        elif "fan" in rx and "on" in rx:
            tx = 3
        elif "fan" in rx and "off" in rx:
            tx = 4
        else:
            print("No determined action, skipping...")
            return
        
        ser.write(str(tx).encode())

    # Speech recognizer
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)

    print("Enter anything when you want to talk, to end press ^C")
    while True:
        input()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Start speaking...")
            audio = r.listen(source)
        print("Recognizing...")
        data = r.recognize_google(audio)
        print(f"You said {data}")
        ring_arduino(data)

