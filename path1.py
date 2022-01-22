import picar_4wd as fc
import sys
import tty
import termios
import time, math
import asyncio

power_val = 50
key = 'status'
print("If you want to quit.Please press q")
def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)

def fwd(dur=1, power_val=50):
    fc.forward(power_val)
    time.sleep(dur)
    fc.stop()
    time.sleep(1)

def rvr(dur=1, power_val=50):
    fc.backward(power_val)
    time.sleep(dur)
    fc.stop()
    time.sleep(1)

def turnl(power_val=50):
    fc.turn_left(power_val)
    time.sleep(0.60)
    fc.stop()

def turnr(power_val=50):
    fc.turn_right(power_val)
    time.sleep(0.55)
    fc.stop()

def Path():
    while True:
        global power_val
        key=readkey()
        if key=='6':
            if power_val <=90:
                power_val += 10
                print("power_val:",power_val)
        elif key=='4':
            if power_val >=10:
                power_val -= 10
                print("power_val:",power_val)
        if key=='p':
            fwd(7, power_val)
            turnr(power_val)
            fwd(4.5, power_val)
            turnl(power_val)
            fwd(7, power_val)
            rvr(12, power_val)
        else:
            fc.stop()
        if key=='q':
            print("quit")  
            break  
if __name__ == '__main__':
    Path()






