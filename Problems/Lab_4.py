import ctypes

# function to show bytes in memory, from location start to start+n
def show_mem_rep(start, n):
	# create a ctypes array of unsigned bytes from the buffer
	arr = (ctypes.c_ubyte * n).from_address(ctypes.addressof(start))
	for i in range(n):
		# use hex() to convert integer to hexadecimal string and slice to remove the "0x" prefix
		# use rjust() to right-justify the string with 2 spaces
		print(hex(arr[i])[2:].rjust(2, "0"), end=" ")
	print()

# Main function to call above function for 0x01234567
if __name__ == "__main__":
	# create a 4-byte integer with value 0x01234567
	i = 0x0000cafe
	# convert integer i to a byte array in little-endian byte order
	i_bytes_le = i.to_bytes(ctypes.sizeof(ctypes.c_int), byteorder="little")
	# convert integer i to a byte array in big-endian byte order
	i_bytes_be = i.to_bytes(ctypes.sizeof(ctypes.c_int), byteorder="big")
	# create a writable buffer using ctypes.create_string_buffer() and copy the bytes into it
	buf_le = ctypes.create_string_buffer(i_bytes_le)
	buf_be = ctypes.create_string_buffer(i_bytes_be)
	# pass the buffer to show_mem_rep
	print("Little Endian: ", end="")
	show_mem_rep(buf_le, ctypes.sizeof(ctypes.c_int))
	print("Big Endian: ", end="")
	show_mem_rep(buf_be, ctypes.sizeof(ctypes.c_int))
