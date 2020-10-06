# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

import machine, pyb, time, bmp, dap
pyb.country('US') # ISO 3166-1 Alpha-2 code, eg US, GB, DE, AU
#pyb.main('main.py') # main script to run after this one

if 0:
  pyb.usb_mode('VCP+HID', vid=0x1d50, pid=0x6018, hid=dap.hid_info)
  time.sleep(1)
  dap.init()
  print('dap')

if 0:
  pyb.usb_mode('VCP+VCP', vid=0x1d50, pid=0x6018)
  bmp.init(stream=pyb.USB_VCP(1))
  print('bmp usb')

# not truncated
