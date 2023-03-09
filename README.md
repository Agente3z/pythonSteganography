# python-Steganography

Python program that hides a message in a .bmp image
Every last 7 byte of a row it changes the last bit to encode an ascii character
To make this decodable in the first row instead of hiding the message it hides the lenght of the message so that the decoder knows when to stop
