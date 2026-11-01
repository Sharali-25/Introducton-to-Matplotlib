import matplotlib.pyplot as plt
scores = [52,89,97,70,82]
days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
plt.plot(days,scores,color = "lightpink", marker = 'o',linestyle = "dashed",linewidth = 2 )
plt.title("My Weeky Scores")
plt.xlabel("Days")
plt.ylabel("Scores")
plt.grid(True)
plt.ylim(0,100)
plt.show()