import matplotlib.pyplot as plt
import numpy as np

# x axis values
x = [1, 2, 3, 4, 5]
# corresponding y axis values
y = [14.93180187, 17.12867191, 17.75147929, 22.74618585, 22.28412256]
y4 = [36.83241252,36.58949746,36.5,36.10755442,43.42857143]
x2 = np.linspace(1,100,10000)
y2 = np.exp(2.67516) * (x2 ** 0.26594)

y3 = (x2 ** 0.06150  ) * np.exp(3.57333 )
plt.xlim(1, 100)
plt.ylim(10, 70)
plt.scatter(x, y, label = 'exp_dev')
plt.scatter(x, y4, label = 'exp_qwerty')
plt.plot(x2, y2, label = "dev_keyboard")
plt.plot(x2, y3, label = "qwerty")
plt.legend()
plt.show()