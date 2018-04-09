from sys import argv

def convertDecToBinary(number):
    bin_array = []
    while number != 0:
        bin_array.insert(0,number % 2)
        number /= 2
    for i in range(0,8 - len(bin_array)):
        bin_array.insert(0,0)
    return bin_array 

def convertMessageToBinary(msg):
    byte_msg = bytearray(msg)
    bin_msg = []
    for byte in byte_msg:
        bin_msg += convertDecToBinary(byte)
    return bin_msg

def encryptImage(img,bin_msg):
    byte = bytearray(img)    
    header_offset = 0
    if "BM" in byte[:20]:
        header_offset = 54
    else:
        print ("Can't encrypt not BMP file")
        return None
    for b in bin_msg:
        byte[header_offset] += byte[header_offset]%2 + b
        header_offset += 1
    for b in [0]*8:
        byte[header_offset] += byte[header_offset]%2 + b
        header_offset += 1
    return byte


if __name__ == "__main__":
    data = open(argv[1], 'rb').read()
    msg = argv[2]
    bin_msg = convertMessageToBinary(msg)
    encrypted_img = encryptImage(data,bin_msg)
    if encrypted_img is not None:
        output = open('output.bmp',"wb")
        print ("Encrypted Image")
        output.write(str(encrypted_img))
        print ("Saved New Image As 'output.bmp' ")
    else:
        print("Failed to encrypt")


