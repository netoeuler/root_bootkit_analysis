PATH = ""

f = open(PATH+"infected_mbr.bin","wb")
binfile = f.read(512)

start_ea = 0x7C
encr_size = 0xCF

for ix in xrange(encr_size):
	start_ea_toint = int(str(start_ea),0)
	#print start_ea_toint,ix,start_ea_toint + ix
	byte_to_decr = binfile[start_ea_toint + ix]
	byte_to_decr_int = ord(binfile[start_ea_toint + ix])
	#print hex(ord(byte_to_decr))
	to_rotate = (0xCF - ix) % 8
	byte_decr = (byte_to_decr_int >> to_rotate) | (byte_to_decr_int << (8 - to_rotate))
	#print str(hex(byte_decr))
	f.seek(byte_decr,0)
	#f.write(str(start_ea + ix))
	break

f.close()