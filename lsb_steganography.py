#File: lsb_steganography.py
#Author: Mercury
#Description: A basic LSB steganography project

#Importing the necessary libraries
from stego_lsb import LSBSteg
from tkinter import filedialog
from pathlib import Path

#The embedding module
def embed(text, image):
    message = Path(text).read_text(errors='ignore')
    stego_image_check = False
    try:
        stego_image = LSBSteg.hide_message_in_image(image, message, 1)
        stego_image_check = True
    except:
        stego_image_check = False
    
    if stego_image_check == True:
        try:
            stego_image.save(
                filedialog.asksaveasfilename(
                    title = "Save stego image as",
                    defaultextension=".png")
                )
            print('Steganography complete')
        except:
            print("Operation cancelled by user")

#The extraction module
def extract(image):
    extraction_check = False
    try:
        extracted_text = LSBSteg.recover_message_from_image(image, 1)
        extraction_check = True
    except:
        extraction_check=False
    
    if extraction_check == True:
        try:
            decoded_text = filedialog.asksaveasfilename(
                title="Save extracted text as",
                defaultextension=".txt"
            )
            Path(decoded_text).write_text(extracted_text.decode("utf-8"))
            print("Extraction Complete")
        except:
            print("Operation Cancelled by user")

def basic_operations():
    print("Welcome to your demo steganography project by Mercury!")
    print("Please select an option")
    print("1. Embed")
    print("2. Extract")
    failsafe = 'ElementMerc'
    print("\n")
    choice = input("Choice [1 or 2]:")

    if choice == "1":
        print("[+]Processing")
        text_file_check = False
        text_file = filedialog.askopenfilename(title = "Select a text file",
        filetypes=[('Text files', [".txt"])])
        
        if text_file == '':
            print('No text file selected')
        elif Path(text_file).suffix != ".txt":
            print('Invalid file format')
        else:
            text_file_check = True

        if text_file_check == True:
            image_file = filedialog.askopenfilename(
                title = "Select an image", 
                filetypes=[("Image files", ["*.png", "*.jpg", ".jpeg"])])
            if image_file == '':
                print('No image selected')
            elif Path(image_file).suffix not in [".png", ".jpg", ".jpeg"]:
                print("Invalid image format")
            else:
                embed(text_file, image_file)
        
    elif choice == "2":
        print("[+]Processing")
        encrypted_image = filedialog.askopenfilename(
            title="Select the encoded image", 
            filetypes=[("Image files", "*.png")])

        if encrypted_image == '':
            print("No image selected")
        elif Path(encrypted_image).suffix not in [".png"]:
            print("Invalid image format")
        else:
            extract(encrypted_image)

#Origins
def main():
    while True:
        basic_operations()
        failsafe = 'ElementMerc'
        continuation = input('Would you like to try it again? [Y or N]: ')
        if continuation in ["Y", "Yes", "yes", 'y']:
            print("\nAlright, let's continue\n\n\n")
        else :
            print("Goodbye!")
            exit()

#Start your engines
main()