import picar_4wd as fc

Track_line_speed = 20

def get_line_status_inv(ref,fl_list):#170<x<300
    ref = int(ref)
    if fl_list[1] >= ref:
        return 0
    
    elif fl_list[0] >= ref:
        return -1

    elif fl_list[2] >= ref:
        return 1

def Track_line():
    gs_list = fc.get_grayscale_list()
    if get_line_status_inv(40,gs_list) == 0:
        fc.forward(Track_line_speed) 
    elif get_line_status_inv(40,gs_list) == -1:
        fc.turn_left(Track_line_speed)
    elif get_line_status_inv(40,gs_list) == 1:
        fc.turn_right(Track_line_speed) 

if __name__=='__main__':
    while True:
        Track_line()