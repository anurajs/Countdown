import time

start = time.time()
timerLength = 24 * 60 * 60
end = start + timerLength
while True:
    file = open("timer.txt",'w')
    file.write(time.strftime('%H:%M:%S',time.gmtime(end-time.time())))
    file.close()
    time.sleep(1)