import numpy as np
import matplotlib.pyplot as plt
import math


def getCoords (r, s, t):
    rn = r/np.sqrt(r**2+s**2+t**2)
    sn = s/np.sqrt(r**2+s**2+t**2)
    tn = t/np.sqrt(r**2+s**2+t**2)
    if float(tn) < 0:
        tn *= (-1)
        side = 0
    else:
        side = 1
    x = -((-tn*rn)/(-1-tn))+rn
    y = -((-tn*sn)/(-1-tn))+sn
    return [x,y,side]

def readfile(str):
	file = open(str)
	lines = []
	for line in file:
		line=line.strip('\n')
		lines.append(line)
	for i in range(len(lines)):
		lines[i] = lines[i].split()
		for j in range(3):
			lines[i][j] = float(lines[i][j])
	return(lines)

def plotPoints(matrix):
	for i in range(len(matrix)):
		coords = getCoords(matrix[i][0], matrix[i][1], matrix[i][2],)
		plt.plot(coords[0],coords[1],matrix[i][3])

def meridian(angle,col):
    if not((angle == 0)or(angle%np.pi < 0.005)):
        theta = np.linspace(0, math.pi, 50)
        rho = 1
        coords = []
        coordsX = []
        coordsY = []
        for i in range(len(theta)):
            Z = rho * np.sin(theta[i]) * np.sin(angle)
            X = rho * np.sin(theta[i]) * np.cos(angle)
            Y = rho * np.cos(theta[i])
            coords.append([X, Y, Z])
        for i in range(len(coords)):
            coordsX.append(getCoords(coords[i][0], coords[i][1], coords[i][2])[0])
            coordsY.append(getCoords(coords[i][0], coords[i][1], coords[i][2])[1])
        plt.plot(coordsX, coordsY, color=col)

def parallel(angle,col):
    angles = [angle]                              
    t2 = np.linspace(0, math.pi, 50)
    coords = []
    coordsX = []
    coordsY = []
    for i in range(len(angles)):
        y2 = math.tan(angles[i])
        for t in t2:
            z2 = np.sin(t)
            x2 = np.cos(t)
            coords.append(getCoords(x2, y2, z2))
        for i in range(len(coords)):
            coordsX.append(coords[i][0])
            coordsY.append(coords[i][1])
        plt.plot(coordsX, coordsY ,color=col)

def drawGrid(radius=1):
    #parallels with 5 deg spacing
    for i in np.linspace(0, math.pi, 21):
        parallel(i, '0.75')

    #meridians with 5 deg spacing
    for i in np.linspace(0, math.pi, 21):
        meridian(i, '0.75')

    #draw circle
    t = np.linspace(0, 2 * math.pi, 500)
    x = radius * np.cos(t)
    y = radius * np.sin(t)
    plt.plot(x, y, color='k')
