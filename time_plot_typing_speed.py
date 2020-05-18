import time as t
import matplotlib.pyplot as plt

times=[]
mistake=0
print("--- This prog helps to analyze your typing speed and accuracy---")
print("---- type the word 'programming 5 times-----")
input("press enter to continue.")
while len(times)<5:
    start_time=t.time()
    word= input(" type the word: ")
    end_time=t.time()
    time_taken=end_time-start_time
    times.append(time_taken)
    if (word.lower()!='programming'):
        mistake=mistake+1
print("you made " +str(mistake)+ "mistake.")
print("now lets see your evolution")
print(times)
t.sleep(3)
x=[1,2,3,4,5]
y=times
plt.plot(x,y)
legend=["1","2","3","4","5"]
plt.xticks(x,legend)
plt.ylabel("time in seconds")
plt.xlabel("attempts")
plt.title("evolution of typing ")
plt.show()
