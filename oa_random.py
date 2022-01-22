import picar_4wd as fc
from random import random

speed = 10

def random_turn(speed, direction):
    if direction > 0.5:
        fc.turn_left(speed)
    else:
        fc.turn_right(speed)

def main():
    direction = 0
    while True:
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        if tmp != [2,2,2,2]:
            random_turn(speed/2, direction)
        else:
            # get a new direction
            direction = random()
            fc.forward(speed)

if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()
