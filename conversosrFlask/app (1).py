from flask import Flask, redirect, render_template, request
import math


app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/static/index.html")

@app.route("/hello/")
@app.route("/hello/<user>/")
def hello (user=None):
    return render_template('hello.html', name=user)

@app.route("/retangulo/")
def form():
    return render_template('circulo.html', titulo='meu form')

@app.route("/retangulo/data/", methods=['POST'])
def form_data():
    if request.method == 'POST':
        altura = float(request.form['altura'])
        base = float(request.form['base'])
        calc = request.form['calc']
        if calc == "Área":
            area_ret = float(base * altura)
            msg = "A área é {}".format(area_ret)
        elif calc == "Perímetro":
            perim_ret = float((base * 2) + (altura * 2))
            msg = "O perímetro é {}".format(perim_ret)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg

@app.route("/trapezio/")
def form():
    return render_template('trapezio.html', titulo='meu form')

@app.route("/trapezio/data/", methods=['POST'])
def form_data():
    if request.method == 'POST':
        lado1 = float(request.form['lado1'])
        lado2 = float(request.form['lado2'])
        altura = float(request.form['altura'])
        baseMenor = float(request.form['baseMenor'])
        baseMaior = float(request.form['baseMaior'])
        calc = request.form['calc']
        if calc == "Área":
            area_trapezio = float(((baseMaior * baseMenor) * altura)/2)
            msg = "A área é {}".format(area_trapezio)
        elif calc == "Perímetro":
            perim_trap = float(baseMaior + baseMenor + lado1 + lado2)
            msg = "O perímetro é {}".format(perim_trap)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg

@app.route("/child/")
def child():
    return render_template('child.html', titulo='Sai fora gay !!!!!')

@app.route("/circulo/area_circ/<float:raio>")
def area_circ (raio):
    area = float(math.pi * math.pow(raio, 2))
    return "O valor é: " + str(area)

@app.route("/circulo/perim_circ/<float:raio>")
def perim_circ (raio):
    perim = float(math.pi * 2) * raio
    return "O valor é: " + str(perim)

@app.route("/retangulo/area_ret/<float:base>/<float:altura>")
def area_ret (base, altura):
    area_ret = float(base * altura)
    return "O valor é: " + str(area_ret)

@app.route("/retangulo/perim_ret/<float:base>/<float:altura>")
def perim_ret (base, altura):
    perim_ret = float((base * 2) + (altura * 2))
    return "O valor é: " + str(perim_ret)

@app.route("/quadrado/perim_quadrado/<float:lado>")
def perim_quadr (lado):
    perim_quadr = float(lado * 4)
    return "O valor é: " + str(perim_quadr)

@app.route("/trapezio/perim_trapezio/<float:basemaior>/<float:basemenor>/<float:lado1>/<float:lado2>")
def perim_trap (basemaior,basemenor,lado1,lado2):
    perim_trap = float(basemaior + basemenor + lado1 + lado2)
    return "O valor é: " + str(perim_trap)

@app.route("/triangulo/perim_triangulo/<float:lado1>/<float:lado2>/<float:lado3>")
def perim_triangulo (lado1,lado2,lado3):
    perim_triangulo = float(lado3 + lado1 + lado2)
    return "O valor é: " + str(perim_triangulo)

@app.route("/quadrado/area_quadrado/<float:base>/<float:altura>")
def area_quadrado (base, altura):
    area_quadrado = float(base * altura)
    return "O valor é: " + str(area_quadrado)

@app.route("/trapezio/area_trapezio/<float:basemaior>/<float:basemenor>/<float:altura>")
def area_trapezio (basemaior, basemenor, altura):
    area_trapezio = float(((basemaior * basemenor) * altura)/2)
    return "O valor é: " + str(area_trapezio)

@app.route("/triangulo/area_triangulo/<float:base>/<float:altura>")
def area_triangulo (base, altura):
    area_triangulo = float(base * altura)
    return "O valor é: " + str(area_triangulo)













