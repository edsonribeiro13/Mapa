import matplotlib.pyplot as plt
import re
#import xmltoadj
import xml_to_points

file_name = "./map.osm"
x = list()
y = list()
with open(file_name) as fp:
    for line in fp:
        points = re.findall(r'[-+]?\d+.\d+', line)
        x.append(float(points[1]))
        y.append(float(points[2]))
print(points)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([min(x),max(x)])
ax.set_ylim([max(y),min(y)])

control = 0

def onclick(event):
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))
    if(control > 0):      
        plt.plot(event.xdata, event.ydata, ',')
        fig.canvas.draw()

plt.plot(x, y, 'ro')
cid = fig.canvas.mpl_connect('button_press_event', onclick)
control += 1
plt.show()

'''plt.clf() - Limpa tudo da tela, tu pode replotar pra aparecer os pontos sem ligações
plt.draw() - Serve pra "Pintar" as ligações, tipo o repaint do java'''