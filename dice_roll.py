
import time
import random

start = int( input("Choose the minimum number that can be rolled: ") )
end = int ( input("Choose the maximum number that can be rolled: ") )
print("Waiting 10 Seconds, try to guess the number!")

time.sleep(10)
print(random.randrange(start,end,1))
