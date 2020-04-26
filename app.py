# En el siguiente programa realizado en python vamos a trabajar sobre un fichero .json y con flask para generar paginas dinamicas.

from flask import Flask, render_template, abort
import json
import os


app=Flask(__name__)

#Creamos la variables global libros, que usaremos en nuestras paginas dinamicas para mostrar la informacion de los libros.

with open("books.json") as libros:
    datos=json.load(libros)

#Creamos nuestra primera ruta que nos dirigira a la pagina principal en la que podremos ver todos los enlaces de los libros para ver su informacion.

@app.route('/')
def inicio():
    nombre='Francisco Javier Martín Núñez'
    return render_template('inicio.html', libros=datos, nombre=nombre)

#Creamos nuestra segunda ruta en nuestro programa que nos ayudara a obtener la informacion de los libros

@app.route('/libro/<isbn>')
def libro(isbn):
    for l in datos:

        #Aqui debemos hacer una comprobacion doble ya que hay algunos libros que no tienen isbn, por lo que eso se debe comprobar y ademas
            
        if "isbn" in l.keys() and isbn == l["isbn"]:
            return render_template('libros.html', libro=l) 

    return abort(404)

@app.route('/categoria/<categoria>')
def categoria(categoria):
            return render_template('categoria.html', libros=datos, categoria=categoria)

port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)
