import cv2
import os
import numpy as np

def encrypt_image(image_path, output_path="encryptedImage.png"):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    secret_message = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    # Convert message into ASCII values
    ascii_values = [ord(char) for char in secret_message]

    n, m, z = 0, 0, 0
    for value in ascii_values:
        img[n, m, z] = np.uint8(value)  # Store exact ASCII values
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite(output_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # Save as lossless PNG
    print("Encryption successful!")

    # Save passcode and message length
    with open("encryption_data.txt", "w") as file:
        file.write(f"{password}\n{len(secret_message)}")

if __name__ == "__main__":
    image_path = "bird.jpg"  # Use your image path
    encrypt_image(image_path)
