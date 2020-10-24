# connect a small 128x64 ssd1306 i2c oled display to
# devebox stm32h7xx: i2c clk = pb10, i2c dta = pb11

import ssd1306

class oled:

  def init():
    global _oled
    oled_i2c=machine.I2C(-1, machine.Pin.board.PB10, machine.Pin.board.PB11)
    _oled = ssd1306.SSD1306_I2C(128, 32, oled_i2c)
    _oled.init_display()

  def display(s):
    global _oled
    _oled.fill(0)
    _oled.text(s, 0, 0)
    _oled.show()

oled.init()
oled.display('Hello, world')
bmp.disp_fun(oled.display)
