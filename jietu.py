

# 方法①
from mss import mss
with mss() as screenshot:
    screenshot.shot(output='F:/scr.png')


# 方法②
import PIL.ImageGrab
scr = PIL.ImageGrab.grab()
scr.save("F:/scr2.png")
