import socket 
#Importing socket module, which provides the essential functions and classes for creating and managing network connections in Python.
import sys 
#importingsys module, which provides access to some variables and functions that interact with the Python runtime environment. 

def scan_port(target, ports):
    try:
        # Function to scan a list of ports on a target IP address
        for port in ports: 
            print(f"Scanning Port {port}...")
            # Creating new socket using the IPv4 address family and TCP protocol
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)  #Default timeout for the socket to handle unresponsive ports, can be modified for better response handling

            result = sock.connect_ex((target, port)) #Establishing Connection to targeted IP address and Port 
            
            #Check result of connection, If the result is 0, the port is open; otherwise, it is closed
            if result == 0:
                print(f"Port {port}: is Open")
            else:
                print(f"Port {port}: is Closed")  # Optional: Print closed ports for detailed output
            sock.close()
    
    # Handle user interrupt
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
    
    #Handle Hostname error
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

    #handle socket error
    except socket.error as e:
        print(f"Socket error: {e}")
        sys.exit()

#Main Block to run the Port scanner to find Open ports 
if __name__ == "__main__":
    target = input("Target IP: ")
    ports_input = input("Target Port (comma-separated): ")
    ports = [int(port.strip()) for port in ports_input.split(',')]
    print(f"Starting scan on target: {target} for ports: {ports}")  # Debug print statement
    scan_port(target, ports)
    print("Scan complete.")  # Debug print statement