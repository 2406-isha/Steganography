from PIL import Image

def encode_image(image_path, message, output_path):
   
    img = Image.open(image_path)
    img = img.convert('RGB')  

    
    encoded = img.copy()

    
    data = img.getdata()

    
    message += '\0'  
    binary_message = ''.join(format(ord(char), '08b') for char in message)  

   
    data_list = list(data)
    binary_index = 0

   
    for i in range(len(data_list)):
        if binary_index < len(binary_message):  
            pixel = list(data_list[i])  
            
            pixel[0] = (pixel[0] & ~1) | int(binary_message[binary_index])
            data_list[i] = tuple(pixel)  
            binary_index += 1  
    
    encoded.putdata(data_list)
    encoded.save(output_path)

def decode_image(image_path):
   
    img = Image.open(image_path)
    data = img.getdata()

   
    binary_message = ''
    for pixel in data:
        binary_message += str(pixel[0] & 1) 
        if binary_message[-8:] == '00000000':  
            break

   
    message = ''.join(chr(int(binary_message[i:i + 8], 2)) for i in range(0, len(binary_message) - 8, 8))
    return message


if __name__ == "__main__":
    
    encode_image('C:/steganography_project/input_image.png.png', 'Hello, World!', 'encoded_image.png')

    
    decoded_message = decode_image('encoded_image.png')
    print(f'Decoded message: {decoded_message}')
