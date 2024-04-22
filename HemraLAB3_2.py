import matplotlib.pyplot as plt
import numpy as np

def clip(subjectPolygon, clipPolygon):
    def inside(p):
        return (cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])

    def computeIntersection():
        dc = [cp1[0] - cp2[0], cp1[1] - cp2[1]]
        dp = [s[0] - e[0], s[1] - e[1]]
        n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
        n2 = s[0] * e[1] - s[1] * e[0] 
        n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
        return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3]

    outputList = subjectPolygon
    cp1 = clipPolygon[-1]

    for clipVertex in clipPolygon:
        cp2 = clipVertex
        inputList = outputList
        outputList = []
        s = inputList[-1]

        for subjectVertex in inputList:
            e = subjectVertex
            if inside(e):
                if not inside(s):
                    outputList.append(computeIntersection())
                outputList.append(e)
            elif inside(s):
                outputList.append(computeIntersection())
            s = e
        cp1 = cp2
    return outputList

# Определяем полигон и отрезок
polygon = [(0,0), (1,0), (2,1), (1,2), (0,1)]
segment = [(-1,-2), (3,3)]

# Отсечение отрезка полигоном
clipped_segment = clip(segment, polygon)

# Визуализация
plt.fill(*zip(*polygon), alpha=0.5, color='grey', label='Polygon')
plt.plot(*zip(*(segment + [segment[0]])), color='red', label='Segment')
if clipped_segment:
    plt.plot(*zip(*(clipped_segment + [clipped_segment[0]])), color='blue', label='Clipped Segment')
plt.legend()
plt.show()
