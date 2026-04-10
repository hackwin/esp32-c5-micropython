# Scan WiFI and print to Serial console
import network
import time

def scan_wifi():
    # Activate station mode
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    print("Scanning for Wi-Fi networks...")
    # Scan for networks
    networks = wlan.scan()
    
    # Sort by signal strength (optional)
    # networks.sort(key=lambda x: x[3], reverse=True)

    print(f"{'SSID':<20} | {'RSSI (dBm)':<10} | {'Channel':<7} | {'Security'}")
    print("-" * 60)
    
    for ssid, bssid, channel, rssi, authmode, hidden in networks:
        # Convert security mode to human readable
        sec = "Unknown"
        if authmode == 0: sec = "Open"
        elif authmode == 1: sec = "WEP"
        elif authmode == 2: sec = "WPA-PSK"
        elif authmode == 3: sec = "WPA2-PSK"
        elif authmode == 4: sec = "WPA/WPA2/WPA3-PSK"
        elif authmode == 5: sec = "WPA3-PSK"
        
        # Print results: SSID, RSSI, Channel, Security
        print(f"{ssid.decode('utf-8'):<20} | {rssi:<10} | {channel:<7} | {sec}")

# Run the scan
scan_wifi()
print("completed scan_wifi")