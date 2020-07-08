import matplotlib.pyplot as plt
plt.bar([1,3,5,7,9],[5,2,7,6,8],label="student1",color='y')
plt.bar([1.5,6,7,5,8],[2,6,7,5,8],label="student2",color='b')

plt.legend()

plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title('Graph Title')
plt.show()
