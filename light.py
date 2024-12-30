from flask import Flask, render_template, request
import RPi.GPIO as GPIO

# GPIO Setup
GPIO.setmode(GPIO.BCM)  # Set to BCM pin numbering
LIGHT_PIN = 17          # Pin connected to the relay module
GPIO.setup(LIGHT_PIN, GPIO.OUT)
GPIO.output(LIGHT_PIN, GPIO.LOW)  # Start with the light OFF

app = Flask(_name_)

# Web interface
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    action = request.form.get('action')
    if action == "ON":
        GPIO.output(LIGHT_PIN, GPIO.HIGH)  # Turn ON the light
    elif action == "OFF":
        GPIO.output(LIGHT_PIN, GPIO.LOW)  # Turn OFF the light
    return "Success"

if _name_ == '_main_':
    try:
        app.run(host='0.0.0.0', port=5000)  # Run the server
    except KeyboardInterrupt:
        GPIO.cleanup()  # Cleanup GPIO on exit