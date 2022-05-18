import matplotlib.pyplot as plt
import re
import xmltoadj
import xml_to_points
from haversine import haversine
import grafo as grf
import vertex as vrt
import popup

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
    
    global clique, x, y, fig, ax, start

    if(control > 0):
        global clique
        if (clique == 0):
            vert = grf.Graph.get_vertices(grf.g)
            start = closestPoint(event.xdata, event.ydata, vert)
            clique += 1
        elif (clique == 1):
            vert = grf.Graph.get_vertices(grf.g)
            end = closestPoint(event.xdata, event.ydata, vert)
            self = grf.g  
            valor,caminho = grf.Graph.min_path(self = self, start = start,end = end)
            if caminho != None:
                for i in caminho:
                    aux = grf.Graph.get_vertex(grf.g, i)
                    xPlot, yPlot = vrt.Vertex.get_lat_lon(aux)
                    plt.plot(yPlot, xPlot,'H-k')
                popup.msgDistancia(f"{round(valor,2)} KM's")    
                plt.draw()
                fig.canvas.draw()
            clique += 1
            popup.msgLimpar()
        elif (clique == 2):
            plotar()
            clique = int(0)


def closestPoint(nodeX, nodeY, vert):
    difAtual = float(0)
    difPos = float(0)
    for i in vert:
        vertAux2 = i
        vertAux = grf.Graph.get_vertex(grf.g, i)
        latV,lonV = vrt.Vertex.get_lat_lon(vertAux)
        latlon = latV,lonV
        eventNodes = nodeY,nodeX
        difAtual = haversine(eventNodes,latlon)
        if(difAtual < difPos or difPos == 0):
            ponto = vertAux2
            difPos = difAtual
    return ponto

def plotar():
    plt.clf()
    plt.plot(x, y, 'or')
    plt.draw()

plotar()
cid = fig.canvas.mpl_connect('button_press_event', onclick)
control = int(0)
clique = int(0)
x_aux = float(0)
y_aux = float(0) 
x_aux1 = float(0)
y_aux1 = float(0) 
control += 1
plt.show()