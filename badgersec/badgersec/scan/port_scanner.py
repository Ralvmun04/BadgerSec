import socket
from concurrent.futures import ThreadPoolExecutor
from ..colors import ROSA, RESET, AMARILLO, ROJO
from ..logger import logger

SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 111: "RPCBind", 135: "Microsoft RPC",
    139: "SMB", 143: "IMAP", 179: "BGP", 389: "LDAP", 443: "HTTPS",
    445: "SMB", 515: "LPD Printer", 993: "IMAPS", 995: "POP3S",
    1025: "RPC", 1433: "MSSQL", 1521: "Oracle DB", 3306: "MySQL",
    3389: "RDP", 5432: "PostgreSQL", 5900: "VNC", 8080: "HTTP Proxy",
    10000: "Webmin"
}

def grab_banner(port, sock):
    try:
        if port == 21:
            sock.send(b"FEAT\r\n")
        elif port == 25:
            sock.send(b"EHLO test\r\n")
        elif port == 110:
            sock.send(b"QUIT\r\n")
        elif port == 143:
            sock.send(b"a1 CAPABILITY\r\n")
        elif port == 80:
            sock.send(b"GET / HTTP/1.1\r\nHost: test\r\n\r\n")
        else:
            return None

        banner = sock.recv(1024).decode(errors='ignore').strip()
        logger.info(f"Banner grabbed from port {port}: {banner[:80]}")
        return banner

    except Exception as e:
        logger.error(f"Error getting banner on port {port}: {e}")
        return None


def scan_single_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.05)

    try:
        if s.connect_ex((target, port)) != 0:
            return None
        
        service = SERVICES.get(port, "unknown")
        print(f"{ROSA}[OPEN]{RESET}-> {port} ({service})" )


        banner = grab_banner(port, s)

        if banner:
            limite = 250
            banner_out = banner[:limite] + ("... [clipped]" if len(banner) > limite else "")
            print(f"   └─ banner: {AMARILLO}{banner_out}{RESET}")
        else:
            print(f"   └─ {ROJO}banner not found{RESET}")
            logger.warning(f"Banner not found on port {port}")

        return port
    
    except Exception as e:
        logger.error(f"Error scanning port {port}: {e}")
        return None

    finally:
        s.close()


def scan_tcp_ports(target):
    puertos_comunes = [
        21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 389,
        443, 445, 515, 993, 995, 1025, 1433, 1521, 3306,
        3389, 5432, 5900, 8080, 10000
    ]

    print(f"Scanning {ROSA}{target}{RESET} for open TCP ports...\n")
    logger.info(f"Scanning {target} for open TCP ports...")

    with ThreadPoolExecutor(max_workers=20) as executor:
        resultados = executor.map(lambda p: scan_single_port(target, p), puertos_comunes)

    open_ports = [p for p in resultados if p is not None]

    print(f"\nOpen ports found: {open_ports}")
    logger.info(f"Open ports found in {target}: {open_ports}")
    return open_ports
