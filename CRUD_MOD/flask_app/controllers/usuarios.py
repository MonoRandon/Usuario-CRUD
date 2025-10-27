from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.usuario import Usuario


@app.route('/')
def index():
    usuarios = Usuario.obtener_todos()
    return render_template('dashboard.html', usuarios=usuarios)


@app.route('/crear', methods=['POST'])
def crear_usuario():
    data = {
        'nombre': request.form['nombre'],
        'email': request.form['email'],
        'edad': request.form['edad']
    }
    Usuario.guardar(data)
    return redirect('/')


@app.route('/editar/<int:id>')
def editar(id):
    usuario = Usuario.obtener_uno({'id': id})
    if not usuario:
        return redirect('/')
    return render_template('editar.html', usuario=usuario)


@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    data = {
        'id': id,
        'nombre': request.form['nombre'],
        'email': request.form['email'],
        'edad': request.form['edad']
    }
    Usuario.actualizar(data)
    return redirect('/')


@app.route('/eliminar/<int:id>')
def eliminar(id):
    Usuario.eliminar({'id': id})
    return redirect('/')
