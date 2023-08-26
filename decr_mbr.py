encr_code = [0x44, 0x85, 0x1D, 0xC7, 0x1C, 0xB8, 0x26, 0x04, 0x08, 0x68, 0x62, 0x40, 0x0E, 0x83, 0x0C, 0xA3, 0xB1, 0x1F, 
0x96, 0x84, 0xF5, 0xE7, 0xF8, 0xC7, 0x03, 0x7E, 0x8F, 0xE1, 0x00, 0x37, 0x26, 0xBF, 0xF1, 0x1F, 0x37, 0x50, 0x00, 0xA3, 
0xD0, 0x00, 0x33, 0xE2, 0x88, 0x01, 0xFF, 0xD8, 0xC6, 0x7C, 0x83, 0x4C, 0xFF, 0x8E, 0xB0, 0x00, 0x7D, 0x1D, 0xBE, 0xE2, 
0xC1, 0xB1, 0xEB, 0xCF, 0x49, 0xA1, 0x8C, 0x5F, 0xB0, 0x0C, 0xAB, 0xB7, 0xC2, 0xEA, 0x00, 0x00, 0x00, 0x00, 0x03, 0x1B, 
0x0C, 0xE9, 0x3E, 0x04, 0xD8, 0x60, 0x5F, 0xF1, 0x02, 0x0E, 0xC7, 0x81, 0xFD, 0xC7, 0x3E, 0x18, 0xDB, 0x7C, 0x8B, 0x5F, 
0xCC, 0xFF, 0xB1, 0x24, 0xFA, 0x66, 0xC7, 0x81, 0x3E, 0xC7, 0x33, 0xFF, 0x6C, 0x0D, 0xBE, 0x99, 0xF1, 0x60, 0xAF, 0xF1, 
0xCC, 0x40, 0x33, 0x4A, 0xC0, 0x1F, 0xE3, 0x99, 0x07, 0x1E, 0xFA, 0x1F, 0x00, 0x4B, 0x12, 0xFA, 0xD3, 0x7C, 0x45, 0x85, 
0x1D, 0xC7, 0x6E, 0x4C, 0xC2, 0xC3, 0x33, 0x4C, 0x18, 0x8E, 0xB5, 0xFF, 0x03, 0x3E, 0x8B, 0x5F, 0x6A, 0x44, 0xA3, 0x34, 
0xCC, 0xFF, 0x07, 0x42, 0xAF, 0x66, 0x1C, 0x78, 0x1A, 0x7D, 0x00, 0xFA, 0xBC, 0x98, 0x6E, 0xEE, 0x20, 0x00, 0x5F, 0x47, 
0xAF, 0x3F, 0x35, 0xA4, 0xDD, 0x85, 0xE4, 0x1D, 0xC1, 0x10, 0x76, 0x0E, 0x8D, 0x10, 0x94, 0x7A, 0x20, 0xFC, 0x4C, 0xA7, 
0x96, 0x75, 0x75, 0xF0, 0x0E, 0x86, 0x63, 0x91, 0x00]
decr_code = []

encr_size = len(encr_code) #0xCF
#print('encr_size:',hex(encr_size))

for ix in range(encr_size):
	byte_to_decr = encr_code[ix]
	to_rotate = (encr_size - ix) % 8
	byte_decr = (byte_to_decr >> to_rotate) | (byte_to_decr << (8 - to_rotate))
	decr_code.append(byte_decr)

#print(decr_code)
somebytes = bytes(decr_code)

file = open('out.bin','wb')
file.write(somebytes)
file.close()