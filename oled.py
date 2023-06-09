import board
import busio
import displayio
import gc
import terminalio
from adafruit_display_text import label
# from driver import oDriver
from adafruit_ssd1331 import SSD1331

# def init():
displayio.release_displays()

spi = busio.SPI(board.GP14, MOSI=board.GP15)
tft_cs = board.GP26
tft_dc = board.GP27
tft_reset = board.GP28

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_reset)
display = SSD1331(display_bus, width=96, height=64)
display.root_group.hidden = True
display.rotation=180

# Make the display context
group = displayio.Group()
display.show(group)

color_bitmap = displayio.Bitmap(96, 64, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000  
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
group.append(bg_sprite)

# Draw a smaller inner rectangle
# inner_bitmap = displayio.Bitmap(86, 54, 1)
# inner_palette = displayio.Palette(1)
# inner_palette[0] = 0xAA0088  # Purple
# inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=5)
# group.append(inner_sprite)
    
# def display(): 
# Draw a label
# text = "YooKBpi v1.0"
# text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=5, y=5)
# group = displayio.Group()
# group.append(text_area)

def text(x, y, text, color):
    # remove previous text from group
    group.pop()
    # global group
    text_area = label.Label(terminalio.FONT, text=text, color=color, x=x, y=y)
    # group = displayio.Group()
    group.append(text_area)
    gc.collect()
    
# def clear():
#     color_bitmap = displayio.Bitmap(96, 64, 1)
#     color_palette = displayio.Palette(1)
#     color_palette[0] = 0x000000  
#     bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
#     group.append(bg_sprite)