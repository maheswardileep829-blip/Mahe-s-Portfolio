import matplotlib.pyplot as plt
m = float(input("What is m or the coefficient of x in your linear equation?"))
b = float(input("What is b in your linear equation?"))
y_intercept = b
x_intercept = None if m == 0 else -b/m
print("Your equation is y =", m, "x +", b) 
print("The y-intercept is", (0, y_intercept))
print("The x-intercept is", (x_intercept, 0))
x_values = range (-5, 6)
y_values = [m * x + b for x in x_values]
plt.plot(x_values, y_values, label=f'y = {m}x + {b}')
plt.axhline(y=0, color='black', linewidth=0.5)  # x-axis
plt.axvline(x=0, color='black', linewidth=0.5)  # y-axis
plt.grid(True, alpha=0.3)
plt.scatter([0, x_intercept], [y_intercept, 0], color='red', s=100)  # Mark intercepts
plt.legend()
plt.title('Linear Equation Graph')
plt.xlabel('x')
plt.ylabel('y')
plt.show()