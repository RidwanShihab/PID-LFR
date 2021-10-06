from controller import Robot

def run_robot(robot):
    time_step=32
    max_speed=5
    base_speed=3
    kp=.5
    kd=1
    motor_1=robot.getDevice('motor1')
    motor_2=robot.getDevice('motor2')
    motor_1.setPosition(float('inf'))
    motor_2.setPosition(float('inf'))
    motor_1.setVelocity(0.0)
    motor_2.setVelocity(0.0)
    
    ir=[]
    
    ir.append(robot.getDevice('left'))
    ir[0].enable(time_step)
    
    ir.append(robot.getDevice('midL'))
    ir[1].enable(time_step)
    
    ir.append(robot.getDevice('mid'))
    ir[2].enable(time_step)
    
    ir.append(robot.getDevice('midR'))
    ir[3].enable(time_step)
    
    ir.append(robot.getDevice('right'))
    ir[4].enable(time_step)
    
    lasterror=0
    
    while robot.step(time_step) !=-1:
        irv=[]
        mul=[-1000,-300,0,300,1000]
        sum=0
        for x in ir:
            if ( x.getValue() <400 ):
                irv.append(0)
            else:
                irv.append(1)

        for i in range(5):
            sum=sum+(mul[i]*irv[i])
        
       
        
        error = sum
        motorspeed =kp*error+ kd*(error-lasterror)
        lasterror= error
        
        #print("left : {} midL:{}  midR:{} right : {}  sum : {} motorspeed : {}".format(irv[0],irv[1],irv[2],irv[3],sum,motorspeed))
        
        left_speed  = base_speed + motorspeed *(max_speed/1000)
        right_speed = base_speed - motorspeed *(max_speed/1000)  
        if(left_speed>10):
            left_speed  =10        
        if( right_speed>10): 
            right_speed  =10 
        
       
        # if(left_speed<0):
            # left_speed  =0        
        # if( right_speed<0): 
            # right_speed  =0 
        
        print("left : {} midL:{} mid:{}  midR:{} right : {}  sum : {} error : {} LMspeed : {} RMpeed : {}".format(irv[0],irv[1],irv[2],irv[3],irv[4],sum,error,left_speed,right_speed))
        #left_speed=0
        #right_speed=0       
        motor_1.setVelocity(-right_speed)
        motor_2.setVelocity(-left_speed)
        
if __name__ == "__main__":
    my_robot = Robot() 
    run_robot(my_robot) 