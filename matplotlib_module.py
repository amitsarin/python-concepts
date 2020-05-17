import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[1000,1500,1200,1600]
plt.plot(x,y)
plt.show()
legend=["jan","feb","march","apr"]
plt.xticks(x,legend)
plt.plot(x,y)
plt.show()
plt.bar(x,y)
plt.ylabel("sales in US$")
legend=["jan","feb","march","apr"]
plt.title("monthly sales")
plt.show()
