# Open Port Scanner

Welcome to my Open Port Scanner project! This is my first cybersecurity project. This project is a simple yet effective port scanner written in Python. It demonstrates basic concepts in cybersecurity, such as port scanning, socket programming, and network communication and Network Security.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Code Explanation](#Explanation)
- [Usage](#usage)
  

## Introduction

Port scanning is a technique used to identify open ports and services available on a networked device. This tool can help you understand which services are running on your network and identify potential vulnerabilities and prevent further attack.
When a port is open, it means that an application or service on the host system is listening for and can respond to incoming requests or data sent to that port. This is in contrast to closed ports, which are not listening for any incoming connections, and filtered ports, which may be blocked by a firewall or other network security devices.

**Note:** Please use this tool responsibly. Only scan networks and devices you own or have explicit permission to scan.

## Features

- Scan a range of ports on a specified host.
- Identify open ports on the target host.
- Simple and easy-to-understand code, great for learning purposes.


## Code Explanation
Importing the socket Module:

1.import socket
-This module is essential for creating and managing network connections.
 Defining the scan_port Function:

2.Attempts to connect to a specified port on the target host.
-Uses socket.socket to create a new socket.
-sock.settimeout(1) sets a timeout for the connection attempt.
-sock.connect_ex((host, port)) tries to connect to the port and returns an error indicator.
-Prints if the port is open if the connection is successful.

3.Defining the scan_ports Function:
-Iterates over a range of ports from start_port to end_port.
-Calls scan_port for each port to check if it's open.

4.Main Execution Block:
-Sets the target host and port range.
-Calls scan_ports to start the scanning process.

Summary
-The script scans a range of ports on a specified host to identify which ports are open.
-It uses the socket module to create network connections and check port statuses.
-The scanning process is handled by iterating over a range of ports and attempting to connect to each one.

## Usage

To use the open port scanner, simply run the script with the target host and port range.

1. **Edit the script:**

    Open the `scanner.py` file and modify the `host`, `start_port`, and `end_port` variables as needed.

2. **Run the script:**

    ```bash
    python scanner.py
    ```

3. **Example output:**

    ```
    Scanning host: example.com
    Port 22 is open
    Port 80 is open
    Port 443 is open
    ```
