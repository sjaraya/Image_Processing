# ---------------------------------------------------------------------------------------
                                        #AUTHOR
# ---------------------------------------------------------------------------------------
#Sergio Araya Z
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
# ---------------------------------------------------------------------------------------
                                        #VARIABLES
# ---------------------------------------------------------------------------------------

imageOne = misc.imread('images/panelUno.png', flatten=True)
imageTwo = misc.imread('images/panelDos.png', flatten=True)

X1, Y1 = np.mgrid[0: imageOne.shape[0], 0: imageOne.shape[1]]
X2, Y2 = np.mgrid[0: imageTwo.shape[0], 0: imageTwo.shape[1]]

# ---------------------------------------------------------------------------------------
#                                       METHODS
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
offline.plot(figure, filename='Surfaces.html')

# ---------------------------------------------------------------------------------------
#Crea un arreglo numpy de la imagen para crear los histogramas
def newImageArray(image):

    array = []

    for i in range(len(image)):

        for j in range(len(image[i])):

            array.append(image[i][j])

    return array

# ---------------------------------------------------------------------------------------

traceHistogramOne = go.Histogram(

    x = newImageArray(imageOne),
    histnorm='Img 1',
    name='Img 1',
    opacity=0.75,
)

traceHistogramTwo = go.Histogram(
    x = newImageArray(imageTwo),
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
offline.plot(figure, filename='Histograms.html')

# ---------------------------------------------------------------------------------------