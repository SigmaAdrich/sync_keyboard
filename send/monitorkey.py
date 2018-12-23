from pynput import keyboard
from udp_cli import send


def on_press(key):
    try:
        for i in range(1):
            if key == keyboard.Key.esc:
                send("esc_down")
                break
            if key == keyboard.Key.up:
                send("up_down")
                break
            if key == keyboard.Key.down:
                send("down_down")
                break
            if key == keyboard.Key.left:
                send("left_down")
                break
            if key == keyboard.Key.right:
                send("right_down")
                break
            if key == keyboard.Key.space:
                send("space_down")
                break
            if key == keyboard.Key.f9:
                send("f9_down")
                break
            if key == keyboard.Key.f10:
                send("f10_down")
                break
            if key == keyboard.Key.enter:
                send("enter_down")
                break
            if key == keyboard.Key.ctrl_l:
                send("ctrl_l_down")
                break
            if key == keyboard.Key.shift_l:
                send("shift_l_down")
                break                
            if key == keyboard.Key.delete:
                send("delete_down")
                break   


            keystr = key.char + "_down"
            print(keystr)
            send(keystr)

    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    for i in range(1):
        if key == keyboard.Key.esc:
            send("esc_up")
            break
        if key == keyboard.Key.up:
            send("up_up")
            break
        if key == keyboard.Key.down:
            send("down_up")
            break
        if key == keyboard.Key.left:
            send("left_up")
            break
        if key == keyboard.Key.right:
            send("right_up")
            break
        if key == keyboard.Key.space:
            send("space_up")
            break
        if key == keyboard.Key.f9:
            send("f9_up")
            break  
        if key == keyboard.Key.f10:
            send("f10_up")
            break            
        if key == keyboard.Key.enter:
            send("f10_up")
            break      
        if key == keyboard.Key.ctrl_l:
            send("ctrl_l_up")
            break  
        if key == keyboard.Key.shift_l:
            send("shift_l_up")
            break 
        if key == keyboard.Key.delete:
            send("delete_up")
            break 



        keystr = key.char + "_up"
        print(keystr)
        send(keystr)

        #if key == keyboard.Key.esc:
            # Stop listener
            #return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()