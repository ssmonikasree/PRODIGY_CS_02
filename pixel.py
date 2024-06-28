from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Open the image
    img = Image.open(image_path)
    img = img.convert('RGB')
    
    # Convert the image to a numpy array
    data = np.array(img)
    
    # Encrypt the image by swapping pixels and applying a mathematical operation
    encrypted_data = np.copy(data)
    rows, cols, _ = data.shape
    for i in range(rows):
        for j in range(cols):
            r, g, b = data[i, j]
            encrypted_data[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    
    # Create a new encrypted image
    encrypted_img = Image.fromarray(encrypted_data.astype('uint8'), 'RGB')
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    img = img.convert('RGB')
    
    # Convert the image to a numpy array
    data = np.array(img)
    
    # Decrypt the image by reversing the mathematical operation
    decrypted_data = np.copy(data)
    rows, cols, _ = data.shape
    for i in range(rows):
        for j in range(cols):
            r, g, b = data[i, j]
            decrypted_data[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    
    # Create a new decrypted image
    decrypted_img = Image.fromarray(decrypted_data.astype('uint8'), 'RGB')
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("Simple Image Encryption Tool")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice not in ['1', '2']:
        print("Invalid choice. Exiting.")
        return

    image_path = input("Enter the path of the image: ").strip()
    output_path = input("Enter the path to save the output image: ").strip()
    key = int(input("Enter the encryption/decryption key (an integer): ").strip())

    if choice == '1':
        encrypt_image(image_path, output_path, key)
    elif choice == '2':
        decrypt_image(image_path, output_path, key)

if __name__ == "__main__":
    main()
