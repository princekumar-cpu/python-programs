import time
def countdown(t=5):
    while t:
        mins, sec = divmod(t,60)
        hour, mins = divmod(mins,60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hour,mins,sec)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print("WakeUp Dude")
#t = int(input('Enter time for sleep'))
countdown(3700)# pass the value in second
