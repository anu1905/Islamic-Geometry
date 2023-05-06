import time
import board
import neopixel


pixel_pin = board.GP11
num_pixels = 250



pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0, auto_write=False)

moons = [
    [0,     1,   2,   3,   4,   5,   6,   7,   8,   9],
    [10,    6,   7,  11,  12,  13,  14,  15,  16,  17],
    [18,   14,  15,  19,  20,  21,  22,  23,  24,  25],
    [26,   22,  23,  27,  28,  29,  30,  31,  32,  33],
    [34,   30,  31,  35,  36,  37,  38,  39,  40,  41],
    [42,   38,  39,  43,  44,  45,  46,  47,  48,  49],
    [50,   51,  52,  53,  54,  55,  56,  57,  58,  59],
    [60,   56,  57,  61,  62,  63,  64,  65,  66,  67],
    [68,   64,  65,  69,  70,  71,  72,  73,  74,  75],
    [76,   72,  73,  77,  78,  79,  80,  81,  82,  83],
    [84,   80,  81,  85,  86,  87,  88,  89,  90,  91],
    [92,   88,  89,  93,  94,  95,  96,  97,  98,  99],
    [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
    [110, 106, 107, 111, 112, 113, 114, 115, 116, 117],
    [118, 114, 115, 119, 120, 121, 122, 123, 124, 125],
    [126, 122, 123, 127, 128, 129, 130, 131, 132, 133],
    [134, 130, 131, 135, 136, 137, 138, 139, 140, 141],
    [142, 138, 139, 143, 144, 145, 146, 147, 148, 149],
    [150, 151, 152, 153, 154, 155, 156, 157, 158, 159],
    [160, 156, 157, 161, 162, 163, 164, 165, 166, 167],
    [168, 164, 165, 169, 170, 171, 172, 173, 174, 175],
    [176, 172, 173, 177, 178, 179, 180, 181, 182, 183],
    [184, 180, 181, 185, 186, 187, 188, 189, 190, 191],
    [192, 188, 189, 193, 194, 195, 196, 197, 198, 199],
    [200, 201, 202, 203, 204, 205, 206, 207, 208, 209],
    [210, 196, 197, 211, 212, 213, 214, 215, 216, 217],
    [218, 214, 215, 219, 220, 221, 222, 223, 224, 225],
    [226, 222, 223, 227, 228, 229, 230, 231, 232, 233],
    [234, 230, 231, 235, 236, 237, 238, 239, 240, 241],
    [242, 238, 239, 243, 244, 245, 246, 247, 248, 249]
]


def show_fullmoon(moon, color):
    for i in range(10):
        pixels[moons[moon][i]] = color
        
def show_firstquarter(moon, color):
    for i in range(5):
        pixels[moons[moon][i]] = color
        
    pixels[moons[moon][9]] = color
        
def show_thirdquarter(moon, color):
    for i in range(4, 10):
        pixels[moons[moon][i]] = color

def show_newmoon(moon, color):
    for i in range(10):
        pixels[moons[moon][i]] = color

def period(moon, color):
    for i in range(10):
        pixels[moons[moon][i]] = color


period(2, 0x330019)
period(3, 0x330019)
period(4, 0x330019)
period(5, 0x330019)
period(6, 0x330019)
show_fullmoon(7, 0x190033)
show_firstquarter(15, 0x190033)
show_newmoon(22, 0x0F000F)
show_thirdquarter(29, 0x190033)


#pulsing the LEDs

#d = 0.1
#x = 0.01
#i = 0

#while pixels.brightness < 0.2:
#    pixels.brightness += x
#    pixels.show()
#    time.sleep(0.05)

while True:
    pass
