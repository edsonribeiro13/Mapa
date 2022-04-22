from dis import dis
import matplotlib.pyplot as plt
import re
import xmltoadj
import xml_to_points
import haversine as harv
import grafo as grf

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

def onclick(event):
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))
    
    global clique, x, y, x_aux, y_aux, x_aux1, y_aux1

    if(control > 0):
        global clique
        if (clique == 0):
            x_aux = closestPoint(event.xdata, x)
            y_aux = closestPoint(event.ydata, y)
            clique += 1
        elif (clique == 1):
            x_aux1 = closestPoint(event.xdata, x)
            y_aux1 = closestPoint(event.ydata, y)
            plt.plot(x[int(x_aux):int(x_aux1)], y[int(y_aux):int(y_aux1)], 'ro')
            fig.canvas.draw()
            clique += 1
            print("TESTE 1")
        elif (clique == 2):
            plt.clf()
            fig.canvas.draw()
            clique = int(0)
            print("TESTE 2")

def closestPoint(node, nodes):
    ponto = nodes[0]
    difAtual = int(0)
    if((nodes[0] - node) < 0):
        difPos = (nodes[0] - node) * (-1)
    else:
        difPos = nodes[0] - node
    for dist in nodes:
        difAtual = dist - node
        if(difAtual < 0):
            difAtual *= -1
        if(difAtual < difPos):
            ponto = dist
            difPos = difAtual
    return ponto

#plt.plot(x, y, 'ro')
cid = fig.canvas.mpl_connect('button_press_event', onclick)
control = int(0)
clique = int(0)
x_aux = int(0)
y_aux = int(0) 
x_aux1 = int(0)
y_aux1 = int(0) 
control += 1
plt.show()

'''plt.clf() - Limpa tudo da tela, tu pode replotar pra aparecer os pontos sem ligações
plt.draw() - Serve pra "Pintar" as ligações, tipo o repaint do java'''