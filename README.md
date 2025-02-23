# secure-data-hiding-in-images-using-steganography
Safely Hide Data in Pictures using Steganography (Python)
This project shows how to use Python and OpenCV to build image steganography in a straightforward manner.The program enables users to conceal (encrypt) a confidential message within an image and then decrypt (retrieve) the message. 

Features
Data Hiding (Encryption): A cover image with a secret text message embedded in it. In order to maintain data integrity, the program uses a diagonal embbedding technique to write each character's ASCII value into the image pixels. The modified photos are then saved as a lossless JPG file.

Decryption By entering the right passcode and message length, you can retrieve the concealed message from the altered image.

Requirements
Python 3.x
OpenCV
   Install via pip:
     pip install opencv-python
