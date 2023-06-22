from  oled import text, display, group
import displayio

cat1 = [ 
        "|\---/|", 
        "| o_o |", 
        " \_^_/ "
    ]

cat2 = [
        " /\_/\ ",
        "( o.o )",
        " > ^ < "
    ]

cat3 = [
        " /\_/\ ",
        "( o o )",
        "==_Y_==",
        "  `-'  "
    ]

def printAscii(x, y, obj, color=0xFFFFFF):
    c = 0
    for l in obj:
        print(l)
        # print(x, counter * 10 + y, l, color)
        text(x, c * 10 + y, l, color)
        c = c+1

def Mario(x, y, isMario = True):
    # Create a bitmap with two colors
    bitmap = displayio.Bitmap(12, 16, 7)

    mainColor = 0xff0000 if isMario else 0x0a7700

    # Create a two color palette
    palette = displayio.Palette(7)
    palette[0] =  mainColor       #C Hat & Shirt
    palette[1] =  0x643200        #B Brown Hair & Boots
    palette[2] =  0xffc896        #S Skin Tone
    palette[3] =  0x0000ff        #O Blue Overalls
    palette[4] =  0xffff00        #Y Yellow Buckles       
    palette[5] =  0xffffff        #W White Gloves
    palette[6] =  0x000000        #_ Transparent (RGBA Format)

    # Create a TileGrid using the Bitmap and Palette
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette, x=x, y=y, tile_width=12, tile_height=16)

    # Create a Group
    # group = displayio.Group()

    # Add the TileGrid to the Group
    group.pop()
    group.append(tile_grid)

    pic =  [[6, 6, 6, 0, 0, 0, 0, 0, 6, 6, 6, 6],
            [6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
            [6, 6, 1, 1, 1, 2, 2, 1, 2, 6, 6, 6], 
            [6, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 6],
            [6, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 1],
            [6, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 6],
            [6, 6, 6, 2, 2, 2, 2, 2, 2, 2, 6, 6],
            [6, 6, 0, 0, 3, 0, 0, 0, 0, 6, 6, 6],
            [6, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 6],
            [0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0],
            [5, 5, 0, 3, 4, 3, 3, 4, 3, 0, 5, 5],
            [5, 5, 5, 3, 3, 3, 3, 3, 3, 5, 5, 5],
            [5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5],
            [6, 6, 3, 3, 3, 6, 6, 3, 3, 3, 6, 6],
            [6, 1, 1, 1, 6, 6, 6, 6, 1, 1, 1, 6],
            [1, 1, 1, 1, 6, 6, 6, 6, 1, 1, 1, 1]]

    px = 0
    py = 0
    for row in pic:
        for pixel in row:
            # display.pixel(x+px, y+py, pixel)
            bitmap[px, py] = pixel
            px = px + 1
        py = py + 1
        px = 0

    # display.show(group)
