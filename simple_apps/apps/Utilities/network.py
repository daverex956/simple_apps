import subprocess
from scapy.all import ARP, Ether, srp
import psutil

def scan_network(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    return clients

def get_network_usage():
    net_io = psutil.net_io_counters()
    bytes_sent = f"{net_io.bytes_sent / (1024*1024):.2f} MB"
    bytes_recv = f"{net_io.bytes_recv / (1024*1024):.2f} MB"
    return bytes_sent, bytes_recv

def run_speedtest():
    try:
        result = subprocess.run(["speedtest", "--simple"], capture_output=True, text=True)
        return result.stdout
    except FileNotFoundError:
        return "Speedtest CLI is not installed. Please install it to run speed tests."

def main():
    network = "192.168.1.1/24"
    print("Scanning network...")
    devices = scan_network(network)
    print("Devices found:")
    for device in devices:
        print(f"IP Address: {device['ip']}, MAC Address: {device['mac']}")

    print("\nMonitoring network usage...")
    sent, received = get_network_usage()
    print(f"Bytes Sent: {sent}, Bytes Received: {received}")

    print("\nRunning speedtest...")
    speedtest_result = run_speedtest()
    print(speedtest_result)

if __name__ == "__main__":
    main()
