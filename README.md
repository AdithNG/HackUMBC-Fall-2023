# The DIY Radio Transmitter and Receiver Station

## The Purpose
The purpose of this project is to create a practical way to learn about radio waves, encryption, decryption, error correction, and other data transmission techniques through an inexpensive reproducible means. 

Transmitters and Receivers are really expensive. So we thought, why not take them from cheap RC cars. 

## General Information
An RC car has both a transmitter and a receiver, allowing it to transmit data from the controller, to trigger movements in the car. We took both the transmitter and receiver out of the RC car and planted them onto breadboards, powering them with Arduino Nanos, and sending commands using the arduinos as controllers along with translating between binary and ASCII. 

## Why should you build it?
It’s a cheap, easy way to get started with receiver and transmitter tech. It’s also a great hands on practical when dealing with transferring data, since it’s such a fundamental transfer, binary over radio. 

## Step by Step

Materials:
- RC car
- 2 Arduino Nanos
- 2 Breadboards
- 2 Micro B cables
- 6 Jumper Wires
- Lead Solder
- Soldering iron
- Screwdriver

Disassemble RC Car and controller
Desolder wires from transmitter(inside controller), and receiver(inside car)
Solder wires to jumper wires
Place arduino nanos on breadboards
Place power and ground jumpers
Place wires from transmitter and receiver on respective nanos
Utilize code for nanos respectively to convert data into binary and transmit, and decrypt data into ASCII on receive.
Connect LCD panel to nano
Enjoy and customize.

Final ability: Input message on transmitter nano’s connected computer. Data is transmitted as binary. Data is converted to ASCII. Data is displayed on LCD.

## Troubleshooting

Transmitter and Receiver are on and powered.
Wires do not have contacts crossing
Use RGB instead of 

WIP.

Refer to visuals on [Devpost](https://devpost.com/software/the-stolen-car-radio)

