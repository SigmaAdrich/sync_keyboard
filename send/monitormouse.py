from pynput import mouse
from udp_cli import send
import json
def on_move(x, y):
#     print('Pointer moved to {0}'.format((x, y)))
    send("move,%s,%s"%(str(x),str(y)))

def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    send("%s,%s,%s,%s"%(str(button), str(pressed),str(x),str(y)))
    # if not pressed:
        # Stop listener
        # return Falsec

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        # on_scroll=on_scroll
        ) as listener:
    listener.join()