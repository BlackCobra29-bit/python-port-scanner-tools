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

if __name__ == "__main__":
    target_host = "109.70.148.130"  # Replace with the target host IP
    start_port = 20
    end_port = 1024  # Replace with the desired range of ports
    open_ports = asyncio.run(scan_ports(target_host, start_port, end_port))
    print(f"Open ports: {open_ports}")
