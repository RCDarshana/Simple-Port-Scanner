import socket
from datetime import datetime

# Define the target
target = input("Enter the IP address to scan: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

# Function to scan a single port
def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Timeout of 1 second
    result = sock.connect_ex((target, port))  # Attempt to connect
    sock.close()
    return result == 0  # Return True if the port is open

# Start the scan
print(f"\nStarting scan on {target} from port {start_port} to {end_port}")
start_time = datetime.now()

# Loop through the specified range
for port in range(start_port, end_port + 1):
    if scan_port(port):
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")

end_time = datetime.now()
print(f"\nScan completed in {end_time - start_time} thanks_specter_cyper")
