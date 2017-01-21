import matplotlib.pyplot as plt
import module1 as m

m.drawGrid()
m.plotPoints(m.readfile('input.txt'))
plt.axis('equal')
plt.show()
