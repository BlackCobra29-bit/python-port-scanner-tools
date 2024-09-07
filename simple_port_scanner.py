import socket

def scan_port(host, port):
    """Scan a single port on a given host."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  # Set a timeout for the connection attempt
        result = s.connect_ex((host, port))
        return result == 0  # Return True if port is open, else False
    
def scan_ports(host, ports):
    """Scan multiple ports on a given host."""
    open_ports = []
    for port in ports:
        if scan_port(host, port):
            open_ports.append(port)
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
    return open_ports

if __name__ == "__main__":
    target_host = "127.0.0.1"  # Replace with the target host IP
    ports_to_scan = [22, 80, 443, 8080]  # Replace with the ports you want to scan
    open_ports = scan_ports(target_host, ports_to_scan)
    print(f"Open ports: {open_ports}")
