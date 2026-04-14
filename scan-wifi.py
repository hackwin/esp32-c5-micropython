import network
import time

AUTH_MODES = {
    0: "Open", 1: "WEP", 2: "WPA-PSK",
    3: "WPA2-PSK", 4: "WPA/WPA2/WPA3-PSK", 5: "WPA3-PSK"
}

def scan_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    time.sleep(1)

    print("Scanning for Wi-Fi networks...")
    networks = wlan.scan()
    networks.sort(key=lambda x: x[3], reverse=True)

    for ssid, bssid, channel, rssi, authmode, hidden in networks:                
        bssid_str = ':'.join(f'{b:02x}' for b in bssid)
        ssid_str = ssid.decode('utf-8')
        
        band = "2.4 GHz" if 1 <= channel <= 14 else "5 GHz"
        
        if rssi >= -50:
            quality = "Excellent"
        elif rssi >= -60:
            quality = "Good"
        elif rssi >= -70:
            quality = "Fair"
        elif rssi >= -90:
            quality = "Poor"
        else:
            quality = "Unusable"
        
        sec = AUTH_MODES.get(authmode, "Unknown")
        print(f"SSID: {ssid_str:<20} | MAC: {bssid_str} | Ch: {channel} | {band} | RSSI: {rssi} {quality} | Sec: {sec}")    

scan_wifi()
#wlan.active(False)
print("Scan complete.")