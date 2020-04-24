# En el siguiente programa realizado en python vamos a trabajar sobre un fichero .json y con flask para generar paginas dinamicas.

from flask import Flask, render_template, abort
import json


app=Flask(__name__)

#Creamos la variables global libros, que usaremos en nuestras paginas dinamicas para mostrar la informacion de los libros.

with open("books.json") as libros:
    datos=json.load(libros)

@app.route('/')
def inicio():
    nombre='Francisco Javier Martín Núñez'
    return render_template('inicio.html', libros=datos, nombre=nombre)


#port=os.environ["PORT"]
app.run('0.0.0.0', debug=True)