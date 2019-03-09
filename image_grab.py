import os, platform
from ctypes import windll
import PIL.ImageGrab
import pyscreenshot


def grab_screenshot(n):

    if not os.path.exists('./img'):
        os.makedirs('./img')

    # i needed this part, so it captures the whole screen
    if platform.system() == 'Windows':
        user32 = windll.user32
        user32.SetProcessDPIAware()

        im = PIL.ImageGrab.grab()
        im.save('./img/screenshot_{0}.jpg'.format(n))

    else:
        im = pyscreenshot.grab()
        im.save('./img/screenshot_{0}.jpg'.format(n))


if __name__ == '__main__':
    grab_screenshot(0)
