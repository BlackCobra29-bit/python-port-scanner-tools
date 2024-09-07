# Python Port Scanner Tools

Welcome to the Python Port Scanner Tools repository! This project includes two efficient port scanner implementations using Python: a synchronous port scanner and an asynchronous port scanner. These tools are designed to help you assess network security and connectivity quickly and effectively.

## Introduction

In this repository, we provide two port scanner implementations:

1. Synchronous Port Scanner: A straightforward, blocking approach to scanning ports one at a time.

2. Asynchronous Port Scanner: A more advanced approach using Python’s asyncio library to scan multiple ports concurrently, improving performance and efficiency.


## Synchronous Port Scanner

The synchronous port scanner uses Python's socket library to scan specified ports on a target host sequentially. This method is easy to understand and implement but may be slower for scanning a large number of ports.

#### Code Example:

```python
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
```

## Asynchronous Port Scanner

The asynchronous port scanner uses Python’s asyncio library to scan ports concurrently. This method significantly speeds up the scanning process, especially useful for scanning a large range of ports.

#### Code Example:

```python
import asyncio
import socket

async def scan_port(host, port):
    """Asynchronously scan a single port on a given host."""
    loop = asyncio.get_event_loop()
    connector = asyncio.open_connection(host, port)
    try:
        reader, writer = await asyncio.wait_for(connector, timeout=1)
        writer.close()
        await writer.wait_closed()
        return True
    except (asyncio.TimeoutError, ConnectionRefusedError):
        return False

async def scan_ports(host, start_port, end_port):
    """Asynchronously scan a range of ports on a given host."""
    ports = range(start_port, end_port + 1)
    tasks = [scan_port(host, port) for port in ports]
    results = await asyncio.gather(*tasks)
    open_ports = [port for port, open in zip(ports, results) if open]
    for port in ports:
        if port in open_ports:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
    return open_ports

```

## Requirements

- Python 3.x
- No additional libraries are required for the synchronous scanner.
- asyncio is included with Python 3.7 and later for the asynchronous scanner.
