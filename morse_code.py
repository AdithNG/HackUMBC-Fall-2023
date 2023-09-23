import serial
import time

# Replace with the correct serial port for your Arduino
serial_port = "/dev/ttyUSB0"  # Linux example, use COMX for Windows

def text_to_binary(text):
    binary_message = ' '.join(format(ord(char), '08b') for char in text)
    return binary_message

def send_binary_to_arduino(binary_message):
    try:
        arduino = serial.Serial(serial_port, 9600, timeout=1)
        time.sleep(2)  # Allow time for Arduino to reset
        arduino.write(binary_message.encode())
        arduino.close()
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    user_input = input("Enter the text to send as binary: ")
    binary_message = text_to_binary(user_input)
    print("Binary Message: " + binary_message)
    send_binary_to_arduino(binary_message)