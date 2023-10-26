import socket

# Define the server address and port
SERVER_ADDRESS = '192.168.99.204'  # Use 'localhost' if the client is on the same machine
SERVER_PORT = 65002

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))

print(f"[*] Listening on {SERVER_ADDRESS}:{SERVER_PORT}")
text_file= open("/home/yassine/injectables/inectexample1.html")
data = text_file.read()
text_file.close()
# Function to fragment the data
def fragment_data(data, fragment_size):
    fragments = [data[i:i + fragment_size] for i in range(0, len(data), fragment_size)]
    return fragments

# Set up a loop to continuously listen for incoming data
while True:
#    received_data, client_address = server_socket.recvfrom(1024)
#    received_data = received_data.decode('utf-8')

    # Assuming a fixed fragment size for each packet
	fragment_size = 1200  # Adjust this based on the appropriate size for your use case

    # Fragment the data
	fragmented_data = fragment_data(data, fragment_size)

    # Send each fragment individually
	for i, fragment in enumerate(fragmented_data):
		sequence_number = str(i).zfill(3)  # Generate a sequence number with leading zeros
		data_with_sequence = sequence_number + fragment
		server_socket.sendto(data_with_sequence.encode('utf-8'), (("192.168.99.226",65002)))
	break

    # Add your custom logic here to process the received data
