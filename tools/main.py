from pye_mp import pye
import bmp, target, semihosting, dap
semihosting.init()

def repl_callback(s):
  return str(eval(s))
bmp.repl_fun(repl_callback)

import network
def wifi_on():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting...')
        wlan.connect('essid', 'passwd')
        while not wlan.isconnected():
            pass
    print(wlan.ifconfig())

if 0:
  wifi_on()
  bmp.init(tcp=3333)
  print('bmp tcp')

# not truncated
