import picar_4wd as fc
from picamera import PiCamera
from time import sleep
import time

# speed = 10
# # state = 0
# dist = 0
# pos = 0
# direction = 0
# turn = 0

class State:
    direction = 0
    state = 0
    speed = 10
    turn = 0
    dist = 0
    pos = time.time()

def take_picture(state):
    state.camera.start_preview()
    # sleep(0.1)
    # print("camera state: ", state)
    state.camera.capture('/home/pi/picar-4wd/logs/picture' + str(state.state) + '.jpg')
    state.camera.stop_preview()
    return

def log_data(state):
    print('state: ', state.state, ' dist: ', state.dist, 'direction: ', state.direction)
    return

def collect_data(state):
    # dist = pos - time
    take_picture(state)
    log_data(state)
    return

def heuristic_turn(state):
    print("turn: ", state.turn)
    if state.turn == 0:
        turnr(state)
        state.turn += 1
    elif state.turn == 1:
        turnaround(state)
        state.turn += 1
    elif state.turn == 2:
        turnl(state)
        state. turn = 0
    return state.turn

def process_obstacle(turn, state):
    collect_data(state)
    direction = turn
    turn = heuristic_turn(state)
    return direction

def fwd(state, dur=1, power_val=50):
    fc.forward(power_val)
    sleep(dur)
    fc.stop()
    sleep(0.1)

def rvr(state, dur=1, power_val=50):
    fc.backward(power_val)
    sleep(dur)
    fc.stop()
    sleep(1)

def turnl(state, power_val=50):
    fc.turn_left(power_val)
    sleep(0.62)
    fc.stop()
    if state.direction == 0:
        state.direction = 3
    else:
        state.direction -= 1


def turnr(state, power_val=50):
    fc.turn_right(power_val)
    sleep(0.60)
    fc.stop()
    if state.direction == 3:
        state.direction = 0
    else:
        state.direction += 1


def turnaround(state, power_val=50):
    fc.turn_left(power_val)
    sleep(1.20)
    fc.stop()
    if state.direction <= 1:
        state.direction += 2
    else:
        state.direction -= 2

def main():
    direction = 0
    # state = 0
    speed = 10
    turn = 0
    # camera = PiCamera()
    # pos = time.time()
    state = State()
    state.speed = 10
    state.camera = PiCamera()

    fc.forward(speed)
    while True:
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        if tmp != [2,2,2,2]:
            # print("obstacle detected. State: ", state)
            # process obstacle and continue
            process_obstacle(turn, state)
            if state.state < 9:
                state.state += 1
            else:
                state.state = 0
            state.dist = time.time() - state.pos
            state.pos = time.time()     
        else:
            # continue
            # print("Moving forward with state: ", state.state)
            fc.forward(speed)

if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()
