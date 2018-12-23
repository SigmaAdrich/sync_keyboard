from socketserver import BaseRequestHandler, UDPServer
import time
from keyboard import *
import win32api
import win32con
import win32gui
import logging
import logging.config
logging.config.fileConfig('../logging.conf')
logger = logging.getLogger('test')


class TimeHandler(BaseRequestHandler):
    def handle(self):
        # logger.debug('Got connection from', self.client_address)
        # Get message and client socket
        msg, sock = self.request
        msgstr = str(msg, encoding = "utf-8")
        logger.debug(msg)
        logger.debug(msgstr)
        select_keyboard(msgstr)
        # resp = "success"
        # sock.sendto(resp.encode("utf-8"), self.client_address)

def select_keyboard(msg):
    up = 0x48
    down = 0x50
    left = 0x4B
    right = 0x4d
    a= 0x1E
    s = 0x1F
    d = 0x20
    f = 0x21
    g = 0x22
    h = 0x23
    j = 0x24
    k = 0x25
    l = 0x26

    q = 0x10
    w = 0x11
    e = 0x12
    r = 0x13
    t = 0x14
    y = 0x15
    u = 0x16
    i = 0x17
    o = 0x18
    p = 0x19

    r1 = 0x02
    r2 = 0x03
    r3 = 0x04
    r4 = 0x05
    r5 = 0x06
    r6 = 0x07
    r7 = 0x08
    r8 = 0x09
    r9 = 0x0A
    r0 = 0x0B

    ctrl_l = 0x1D
    shift_l = 0x2A

    z = 0x2C
    x = 0x2d
    c = 0x2E
    v = 0x2F
    b = 0x30
    n = 0x31
    m = 0x32

    delete = 0x53
    esc = 0x01
    f10 = 0x44
    f9 = 0x43
    space = 0x39
    enter = 0x1c

    for ii in range(1):



        if msg == "left_down":
            key_down(left)
            break
        if msg == "left_up":
            key_up(left)
            break
        if msg == "right_down":
            key_down(right)
            break
        if msg == "right_up":
            key_up(right)
            break
        if msg == "up_down":
            key_down(up)
            break
        if msg == "up_up":
            key_up(up)
            break
        if msg == "down_down":
            key_down(down)
            break
        if msg == "down_up":
            key_up(down)
            break

        if msg == "down_down":
            key_down(up)
            break
        if msg == "down_up":
            key_up(up)
            break

        if msg == "a_down":
            key_down(a)
            break
        if msg == "a_up":
            key_up(a)
            break

        if msg == "s_down":
            key_down(s)
            break
        if msg == "s_up":
            key_up(s)
            break

        if msg == "d_down":
            key_down(d)
            break
        if msg == "d_up":
            key_up(d)
            break

        if msg == "f_down":
            key_down(f)
            break
        if msg == "f_up":
            key_up(f)
            break

        if msg == "g_down":
            key_down(g)
            break
        if msg == "g_up":
            key_up(g)
            break

        if msg == "h_down":
            key_down(h)
            break
        if msg == "h_up":
            key_up(h)
            break
        if msg == "j_down":
            key_down(j)
            break
        if msg == "j_up":
            key_up(j)
            break
        if msg == "k_down":
            key_down(k)
            break
        if msg == "k_up":
            key_up(k)
            break
        if msg == "l_down":
            key_down(l)
            break
        if msg == "l_up":
            key_up(l)
            break





        if msg == "q_down":
            key_down(q)
            break
        if msg == "q_up":
            key_up(q)
            break

        if msg == "w_down":
            key_down(w)
            break
        if msg == "w_up":
            key_up(w)
            break

        if msg == "e_down":
            key_down(e)
            break
        if msg == "e_up":
            key_up(e)
            break

        if msg == "r_down":
            key_down(r)
            break
        if msg == "r_up":
            key_up(r)
            break
        if msg == "t_down":
            key_down(t)
            break
        if msg == "t_up":
            key_up(t)
            break
        if msg == "y_down":
            key_down(y)
            break
        if msg == "y_up":
            key_up(y)
            break
        if msg == "u_down":
            key_down(u)
            break
        if msg == "u_up":
            key_up(u)
            break
        if msg == "i_down":
            key_down(i)
            break
        if msg == "i_up":
            key_up(i)
            break
        if msg == "o_down":
            key_down(o)
            break
        if msg == "o_up":
            key_up(o)
            break
        if msg == "p_down":
            key_down(p)
            break
        if msg == "p_up":
            key_up(p)
            break



        if msg == "z_down":
            key_down(z)
            break
        if msg == "z_up":
            key_up(z)
            break
        if msg == "x_down":
            key_down(x)
            break
        if msg == "x_up":
            key_up(x)
            break
        if msg == "c_down":
            key_down(c)
            break
        if msg == "c_up":
            key_up(c)
            break
        if msg == "v_down":
            key_down(v)
            break
        if msg == "v_up":
            key_up(v)
            break
        if msg == "b_down":
            key_down(b)
            break
        if msg == "b_up":
            key_up(b)
            break
        if msg == "n_down":
            key_down(n)
            break
        if msg == "n_up":
            key_up(n)
            break
        if msg == "m_down":
            key_down(m)
            break
        if msg == "m_up":
            key_up(m)
            break

        if msg == "1_down":
            key_down(r1)
            break
        if msg == "1_up":
            key_up(r1)
            break
        if msg == "2_down":
            key_down(r2)
            break
        if msg == "2_up":
            key_up(r2)
            break
        if msg == "3_down":
            key_down(r3)
            break
        if msg == "3_up":
            key_up(r3)
            break
        if msg == "4_down":
            key_down(r4)
            break
        if msg == "4_up":
            key_up(r4)
            break
        if msg == "5_down":
            key_down(r5)
            break
        if msg == "5_up":
            key_up(r5)
            break
        if msg == "6_down":
            key_down(r6)
            break
        if msg == "6_up":
            key_up(r6)
            break
        if msg == "7_down":
            key_down(r7)
            break
        if msg == "7_up":
            key_up(r7)
            break
        if msg == "8_down":
            key_down(r8)
            break
        if msg == "8_up":
            key_up(r8)
            break
        if msg == "9_down":
            key_down(r9)
            break
        if msg == "9_up":
            key_up(r9)
            break
        if msg == "0_down":
            key_down(r0)
            break
        if msg == "0_up":
            key_up(r0)
            break


        if msg == "ctrl_l_down":
            key_down(ctrl_l)
            break
        if msg == "ctrl_l_up":
            key_up(ctrl_l)
            break
        if msg == "delete_down":
            key_down(delete)
            break
        if msg == "delete_up":
            key_up(delete)
            break
        if msg == "shift_l_down":
            key_down(shift_l)
            break
        if msg == "shift_l_up":
            key_up(shift_l)
            break




        if msg == "esc_down":
            key_down(esc)
            break
        if msg == "esc_up":
            key_up(esc)
            break

        if msg == "f10_down":
            key_down(f10)
            break
        if msg == "f10_up":
            key_up(f10)
            break

        if msg == "f9_down":
            key_down(f9)
            break
        if msg == "f9_up":
            key_up(f9)
            break
            
        if msg == "space_down":
            key_down(space)
            break
        if msg == "space_up":
            key_up(space)
            break

        if msg == "enter_down":
            key_down(enter)
            break
        if msg == "enter_up":
            key_up(enter)
            break
        try:
            msg = msg.split(",")
            but = msg[0]
            if but == "move":
                x ,y = int(msg[1]), int(msg[2])
                print(x,y)
                win32api.SetCursorPos((x, y))
                break

            press = msg[1]
            x ,y = int(msg[2]), int(msg[3])
            if but == "Button.left" and press == "True":
                win32api.SetCursorPos((x, y))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                break
            if but == "Button.left" and press == "False":
                win32api.SetCursorPos((x, y))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                break
            if but == "Button.right" and press == "True":
                win32api.SetCursorPos((x, y))
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                break
            if but == "Button.right" and press == "False":
                win32api.SetCursorPos((x, y))
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                break

        except Exception as e:
            print(e)


if __name__ == '__main__':
    serv = UDPServer(('0.0.0.0', 20000), TimeHandler)
    serv.serve_forever()