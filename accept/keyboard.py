import rabird.winio
import time
import atexit
import random

# KeyBoard Commands
# Command port
KBC_KEY_CMD = 0x64
# Data port
KBC_KEY_DATA = 0x60

__winio = None

def __get_winio():
    global __winio

    if __winio is None:
            __winio = rabird.winio.WinIO()
            def __clear_winio():
                    global __winio
                    __winio = None
            atexit.register(__clear_winio)

    return __winio

def wait_for_buffer_empty():
    '''
    Wait keyboard buffer empty
    '''

    winio = __get_winio()

    dwRegVal = 0x02
    while (dwRegVal & 0x02):
            dwRegVal = winio.get_port_byte(KBC_KEY_CMD)

def key_down(scancode):
    winio = __get_winio()

    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_CMD, 0xd2);
    wait_for_buffer_empty();
    winio.set_port_byte(KBC_KEY_DATA, scancode)

def key_up(scancode):
    winio = __get_winio()

    wait_for_buffer_empty();
    winio.set_port_byte( KBC_KEY_CMD, 0xd2);
    wait_for_buffer_empty();
    winio.set_port_byte( KBC_KEY_DATA, scancode | 0x80);



class mykeyboard(object):
    up = 0x48
    down = 0x50
    left = 0x4B
    right = 0x4d
    
    def __init__(self,):
        self._delay_para = 0.3

    def key_press(self, scancode, press_time = 0.1):
        rad = random.random() #0 <= n < 1.0
        rad_sleep = random.random() #0 <= n < 1.0
        key_down( scancode )
        press_time = press_time + rad*self._delay_para
        # print("mid time %f"%press_time)
        time.sleep( press_time )
        key_up( scancode )
        rad_sleep = rad*self._delay_para + rad_sleep*0.5
        time.sleep( rad_sleep )
        # print("end time %f"%rad_sleep)


    def key_double_press(self, scancode_x, scancode_y,time_x = 0.2,time_y = 0.2):
        rad = random.random() #0 <= n < 1.0
        key_down( scancode_x )
        key_down( scancode_y )
        if time_x <= time_y:
            time_x = time_x + rad*self._delay_para
            time.sleep(time_x)
            # print("time_x:%f"%time_x)
            key_up( scancode_x )
            #有时候加上随机数后x比y大了
            time.sleep(abs(time_y - time_x))
            key_up( scancode_y )
        else:
            time_y = time_y + rad*self._delay_para
            time.sleep(time_y)
            # print("time_y:%f"%time_y)
            key_up( scancode_y )
            time.sleep(abs(time_x - time_y))
            key_up( scancode_x )

def up():
    #小键盘8
    key_press(0x48)

def down():
    #小键盘2
    key_press(0x50)

def left():
    #小键盘4
    key_press(0x4B)

def right():
    #小键盘6
    key_press(0x4d)

def pre_a():
    k = mykeyboard()
    k.key_press(0x1E)

def pre_s():
    k = mykeyboard()
    k.key_press(0x1F)

def pre_d():
    k = mykeyboard()
    k.key_press(0x20)

def pre_f():
    k = mykeyboard()
    k.key_press(0x21)

def pre_g():
    k = mykeyboard()
    k.key_press(0x22)

def pre_h():
    k = mykeyboard()
    k.key_press(0x23)

def pre_q():
    key_press(0x10)

def pre_w():
    key_press(0x11)

def pre_e():
    key_press(0x12)

def pre_r():
    key_press(0x13)

def pre_t():
    key_press(0x14)

def pre_x():
    k = mykeyboard()
    k.key_press(0x2d)

def pre_esc():
    key_press(0x01)

def pre_enter():
    key_press(0x1c)

def pre_f10():
    key_press(0x44)

def pre_f9():
    #返回城镇
    key_press(0x43)

def pre_space():
    key_press(0x39)


# Press 'A' key
# Scancodes references : https://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html

if __name__ == "__main__":
    time.sleep(2)
    # up()
    pre_h()
    # left()
    # right()
    # pre_a()
    # pre_s()
    # pre_d()
    #pre_f()
    #pre_g()
    # pre_x()
    # k = mykeyboard()
    # key_up(0x48)
    # k.key_double_press(k.up,k.right,0.5,2)
    # key_double_press(0x48, 0x4d, 0.5, 2)