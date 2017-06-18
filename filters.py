# ---------------------------------------------------------------------------------------
                                        #AUTHORS
# ---------------------------------------------------------------------------------------
#Sergio Araya Z
#Jeison Saborio R
#Kevin Zamora A
#Last Update: 16 / 06 / 17
# ---------------------------------------------------------------------------------------
                                        #IMPORTS
# ---------------------------------------------------------------------------------------
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go
from scipy import misc
import numpy as np
import plotly.offline as offline
import plotly.dashboard_objs as dashboard
import IPython.display
from IPython.display import Image
# ---------------------------------------------------------------------------------------
                                        #VARIABLES
# ---------------------------------------------------------------------------------------

imageOne = misc.imread('images/panelUno.png', flatten=True)
imageTwo = misc.imread('images/panelDos.png', flatten=True)

X1, Y1 = np.mgrid[0: imageOne.shape[0], 0: imageOne.shape[1]]
X2, Y2 = np.mgrid[0: imageTwo.shape[0], 0: imageTwo.shape[1]]

# ---------------------------------------------------------------------------------------
#Objeto para almacenar las listas para el scatter 3d

class ScatterValue:

    def __init__(self, listX, listY, listZ):

        self.listX = listX
        self.listY = listY
        self.listZ = listZ

# ---------------------------------------------------------------------------------------
#                                       METHODS
# ---------------------------------------------------------------------------------------
#Crea un arreglo de la imagen para crear los metodos
def convertImageArray(matriz):

    array = []

    for i in range(len(matriz)):

        for j in range(len(matriz[i])):

            array.append(matriz[i][j])

    return array

# ---------------------------------------------------------------------------------------
#Crea una matriz con los puntos de interes segun el valor definido para el rgb
def selectPoints(matriz, value):

    temporalX = []
    temporalY = []
    temporalZ = []

    for i in range(len(matriz)):

       for j in range(len(matriz[i])):

           if matriz[i][j] > value:
                temporalZ.append(matriz[i][j])
                temporalX.append(i)
                temporalY.append(j)

    scatterValue = ScatterValue(temporalX, temporalY, temporalZ)

    return scatterValue

# ---------------------------------------------------------------------------------------
#crea los mesh3d de las imagenes a analizar
data = [
    go.Mesh3d(
        x = convertImageArray(X1),
        y = convertImageArray(Y1),
        z = convertImageArray(imageOne),
        opacity=0.5,
        color='orange'
    )
]

layout = go.Layout(
    title='Mesh3D Img 1',
    autosize=False,
    width=1000,
    height=650,
)

figure = go.Figure(data=data, layout=layout)
offline.plot(figure, filename='Mesh3Ds.html', auto_open=False)

# ---------------------------------------------------------------------------------------
#crea los surfaces de las imagenes a analizar
data = [
    go.Surface(
        z = imageOne
    )
]

layout = go.Layout(
    title='Surface Img 1',
    autosize=False,
    width=1000,
    height=650,
)

figure = go.Figure(data=data, layout=layout)
offline.plot(figure, filename='Surfaces.html', auto_open=False)

# ---------------------------------------------------------------------------------------
#crea una comparacion de los histogramas de las imagenes
traceHistogramOne = go.Histogram(

    x = convertImageArray(imageOne),
    histnorm='Img 1',
    name='Img 1',
    opacity=0.75,
)

traceHistogramTwo = go.Histogram(
    x = convertImageArray(imageTwo),
    histnorm='Img 2',
    name='Img 2',
    opacity=0.75,
)

data = [traceHistogramOne, traceHistogramTwo]

layout = go.Layout(
    title='Histogram comparation',
    xaxis=dict(
        title='Pixel color'
    ),
    yaxis=dict(
        title='Pixel cuantity'
    ))

figure = go.Figure(data=data, layout=layout)
offline.plot(figure, filename='Histograms.html', auto_open=False)

# ---------------------------------------------------------------------------------------
#crea el diagrama de contour segun el rgb de la imagen
data = [
    go.Contour(
        z = imageOne,
        colorscale='Jet',
    )
]

layout = go.Layout(
    title='Contour Img 1',
    autosize=True,
)

figure = go.Figure(data=data, layout=layout)
offline.plot(figure, filename='Contours.html', auto_open=False)

# ---------------------------------------------------------------------------------------
"""
scene = dict(
    xaxis=dict(
        gridcolor='rgb(255, 255, 255)',
        zerolinecolor='rgb(255, 255, 255)',
        showbackground=True,
        backgroundcolor='rgb(230, 230,230)'
    ),
    yaxis=dict(
        gridcolor='rgb(255, 255, 255)',
        zerolinecolor='rgb(255, 255, 255)',
        showbackground=True,
        backgroundcolor='rgb(230, 230,230)'
    ),
    zaxis=dict(
        gridcolor='rgb(255, 255, 255)',
        zerolinecolor='rgb(255, 255, 255)',
        showbackground=True,
        backgroundcolor='rgb(230, 230,230)'
    )
)

selectPointsImageOne = selectPoints(imageOne, 245)
selectPointsImageTwo = selectPoints(imageTwo, 245)


figureAnalysis = tools.make_subplots(rows=2, cols=2,
                          specs=[[{'is_3d': True}, {'is_3d': True}],
                                 [{'is_3d': True}, {'is_3d': True}]])

figureAnalysis.append_trace(dict(type='surface', x=X1, y=Y1, z=imageOne, colorscale='RdBu', name='Image 1',
                      scene='Image 1', showscale=False), 1, 1)
figureAnalysis.append_trace(dict(type='surface', x=X2, y=Y2, z=imageTwo, colorscale='RdBu', name='Image 2',
                      scene='Image 2', showscale=False), 1, 2)
figureAnalysis.append_trace(dict(type='scatter3d', x=selectPointsImageOne.listX, y=selectPointsImageOne.listY,
                      z=selectPointsImageOne.listZ, name='Image 1',
                      scene='Image 1', opacity=0.5, showlegend=False), 2, 1)
figureAnalysis.append_trace(dict(type='scatter3d', x=selectPointsImageTwo.listX, y=selectPointsImageTwo.listY,
                      z=selectPointsImageTwo.listZ, opacity=0.5,
                      scene='Image 2', name='Image 2', showlegend=False), 2, 2)

figureAnalysis['layout'].update(title='Image Analysis',
                     height='1400', width='1333')
figureAnalysis['layout']['scene1'].update(scene)
figureAnalysis['layout']['scene2'].update(scene)
figureAnalysis['layout']['scene3'].update(scene)
figureAnalysis['layout']['scene4'].update(scene)

offline.plot(figureAnalysis, filename='Image Analysis.html')
"""
# ---------------------------------------------------------------------------------------
