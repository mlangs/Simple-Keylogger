import os
import logging
from pynput import mouse, keyboard
from image_grab import grab_screenshot


def on_move(x, y):
    if not moving:
        pass
    else:
        logging.info('Mouse moved to ({0}, {1})'.format(x, y))


def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        if screenshot:
            global count
            grab_screenshot(count)
            count += 1


def on_scroll(x, y, dx, dy):
    if not scrolling:
        logging.info('Mouse scrolled at ({0}, {1}) ({2}, {3})'.format(x, y, dx, dy))


def on_press(key):
    logging.info('pressed:  '+ str(key))


def on_release(key):
    if release:
        logging.info('released: ' + str(key))



if __name__ == '__main__':
    moving = False
    scrolling = False
    screenshot = True
    release = False

    count = 0

    # generate log folder
    if not os.path.exists('./logs'):
        os.makedirs('./logs')

    log_dir = './logs/'
    logging.basicConfig(filename=log_dir+'log.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')


    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        	listener.join()
