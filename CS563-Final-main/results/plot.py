import matplotlib.pyplot as pyplot

# APC
xdata = [
1.1939,
1.2499,
1.2742,
1.2872,
1.2951,
1.3002,
1.3038,
1.3064,
1.3084,
1.3099,
]

# Nested loops
# xdata = list(range(1, 11))

ydata = [
6.92E-16,
4.06E-16,
3.22E-16,
3.23E-16,
5.70E-16,
2.95E-16,
9.05E-16,
7.15E-16,
9.91E-16,
9.25E-16,
]

pyplot.scatter(xdata, ydata)
pyplot.plot(xdata, ydata)
# pyplot.xscale('log')
pyplot.grid(True)

pyplot.title("Synthetic Data APC vs Error")
pyplot.xlabel("Asymptotic Path Complexity")
pyplot.ylabel("Maximum Relative Error")

pyplot.show()