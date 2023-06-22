import board
import digitalio


def all_off():
# LED off
    l1 = digitalio.DigitalInOut(board.GP9)  # l1
    l1.switch_to_output()
    l1.value = False
    l2 = digitalio.DigitalInOut(board.GP10)  # l2
    l2.switch_to_output()
    l2.value = False
    l3 = digitalio.DigitalInOut(board.GP11)  # l3
    l3.switch_to_output()
    l3.value = False
    l4 = digitalio.DigitalInOut(board.GP12)  # l4
    l4.switch_to_output()
    l4.value = False
    l5 = digitalio.DigitalInOut(board.GP13)  # l5
    l5.switch_to_output()
    l5.value = False

def on(id):
    if id == 1:
        l1 = digitalio.DigitalInOut(board.GP9)  # l1
        l1.switch_to_output()
        l1.value = True
    elif id == 2:
        l2 = digitalio.DigitalInOut(board.GP10)  # l2
        l2.switch_to_output()
        l2.value = True
    elif id == 3:
        l3 = digitalio.DigitalInOut(board.GP11)  # l3
        l3.switch_to_output()
        l3.value = True
    elif id == 4:
        l4 = digitalio.DigitalInOut(board.GP12)  # l4
        l4.switch_to_output()
        l4.value = True
    elif id == 5:
        l5 = digitalio.DigitalInOut(board.GP13)  # l5
        l5.switch_to_output()
        l5.value = True