import matplotlib.pyplot as plt
savings = [25, 46, 37, 86, 29, 67]
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
plt.bar(week, savings, color='lavender', width=0.7)
plt.title("My savings of the week")
plt.xlabel("Days")
plt.ylabel("Savings")
plt.ylim(0, 90)
plt.show()