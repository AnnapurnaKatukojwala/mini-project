import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the pin connected to the relay
relay_pin = 17  # GPIO pin 17 (you can change it to any other pin)

# Set up the GPIO pin as an output pin
GPIO.setup(relay_pin, GPIO.OUT)

def turn_light_on():
    GPIO.output(relay_pin, GPIO.HIGH)  # Turn the light on
    print("Light is ON")

def turn_light_off():
    GPIO.output(relay_pin, GPIO.LOW)  # Turn the light off
    print("Light is OFF")

def main():
    try:
        while True:
            command = input("Enter 'on' to turn the light on or 'off' to turn it off: ").strip().lower()
            
            if command == 'on':
                turn_light_on()
            elif command == 'off':
                turn_light_off()
            else:
                print("Invalid input. Please enter 'on' or 'off'.")
                
            time.sleep(1)  # Wait before taking the next input
    except KeyboardInterrupt:
        print("Program terminated.")
    finally:
        GPIO.cleanup()  # Clean up GPIO settings before exiting

if __name__ == '__main__':
    main()
