import cwiid
import time

print ' Press 1+2 on your Wiimote now...'
wm = None
i=2
while not wm:
    #try to connect to wiimote
    try:
        wm=cwiid.Wiimote()
    # if runtime error try again
    except RuntimeError:
        if (i>5):
            print "Cannot Create Connection"
            print "Error opening wiimote connection"
            print "Attempt" + str(i)
            i += 1
#sets wiimote to report mode            
wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
#enables led 1 on wiimote
wm.led = 1
print "Connection Established"
#Uncomment bottom to lines to report button pressed
#while wm:
    #print wm.state['buttons']
#while connected
while wm:
    # if B is pressed print forward
    if wm.state['buttons']== 4:
        print "Forward"
    #if A is pressed print backward
    elif wm.state['buttons'] == 8:
        print "Backwards"
    #if no buttons are pressed print stop
    elif wm.state['buttons']== False:
        print "Stopped"
    # if right d-pad is pressed print right
    elif wm.state['buttons'] == 512:
        print "Right"
    #if left d-pad is pressed print left
    elif wm.state['buttons'] == 256:
        print "Left"

        
       
    	  
 
