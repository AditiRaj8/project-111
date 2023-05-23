import time
print(dir(time))
def counter(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)
        timer = f'{mins}:{secs}'
        print(timer)
        time.sleep(1)
        seconds-=1

seconds=int(input("Enter the timing seconds:"))
counter(seconds)
