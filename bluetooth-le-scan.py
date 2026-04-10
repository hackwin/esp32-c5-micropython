# Scan for bluetooth Low Energy devices
import time
import bluetooth
from micropython import const
_IRQ_SCAN_RESULT = const(5)
_IRQ_SCAN_DONE = const(6)

def bt_irq(event, data):
  if event == _IRQ_SCAN_RESULT:
    # A single scan result.
    addr_type, addr, connectable, rssi, adv_data = data
    print(':'.join(['%02X' % i for i in addr]))
  elif event == _IRQ_SCAN_DONE:
    # Scan duration finished or manually stopped.
    print('scan complete')

# Scan for 10s (at 100% duty cycle)
ms_scan = 10000
bt = bluetooth.BLE()
bt.irq(bt_irq)
bt.active(True)
bt.gap_scan(ms_scan, 30000, 30000)
time.sleep_ms(ms_scan)
