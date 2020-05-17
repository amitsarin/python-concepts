import time as t
print(t.localtime())
time_now= t.localtime()
print("transaction completed at" , str(time_now.tm_hour) + " hour")
print(t.time())
time_now=t.time()
t.sleep(7)
delivery_time=time_now+(86400*30)
print(t.localtime(delivery_time))
