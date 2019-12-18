from drive.msg import drive_msg
def string_to_motor_command(master_str):
    
    drivex=drive_msg()

    pub = rospy.Publisher('rover_drive', drive_msg ,queue_size=10)
    rospy.init_node('command_motor_from_string', anonymous=True)
    rate = rospy.Rate(10)
    movement = int(master_str[0])
    pwm = int(master_str[1:4])
    intr = int(master_str[4])
    drivex.ldir = bool(0)
    drivex.rdir = bool(0)
    if(movement != 0):
        drivex.lpwm = pwm 
        drivex.rpwm = pwm
        if(movement > 1):
            if(movement < 4):
                drivex.rpwm = 1
        if(movement == 2):
            drivex.lpwm = 1
        if(movement == 4):
            drivex.lpwm = 1

        
    else:
        drivex.lpwm = 0 
        drivex.rpwm = 0
        drivex.ldir = bool(0)
        drivex.rdir = bool(0)
    
    pub.publish(drivex)
    rate.sleep()
