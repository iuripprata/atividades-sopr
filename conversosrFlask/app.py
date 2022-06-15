from flask import Flask, redirect, render_template, request
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route("/")
def index():
    return redirect("/static/index.html")

@app.route("/hello/")
@app.route("/hello/<user>/")
def hello (user=None):
    return render_template('hello.html', name=user)

@app.route("/tempo/segundo/")
def seg():
    return render_template('tempo_segundo.html', titulo='meu form')

@app.route("/tempo/segundo/data/", methods=['POST'])
def seg_data():
    if request.method == 'POST':
        segundo = float(request.form['segundo'])
        temp = request.form['temp']
        if temp == "Minuto":
            seg_minuto = float(segundo / 60)
            msg = "{} in hours is {}".format(segundo, seg_minuto)
        elif temp == "Hora":
            seg_hora = float(segundo / 3600)
            msg = "{} in hours is {}".format(segundo, seg_hora)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg

@app.route("/tempo/hora/")
def hora():
    return render_template('tempo_hora.html', titulo='meu form')

@app.route("/tempo/hora/data/", methods=['POST'])
def hora_data():
    if request.method == 'POST':
        hora = float(request.form['hora'])
        temp = request.form['temp']
        if temp == "Minuto":
            hora_minuto = float(hora * 60)
            msg = "{} in hours is {}".format(hora, hora_minuto)
        elif temp == "Segundo":
            hora_segundo = float(hora * 3600)
            msg = "{} in hours is {}".format(hora, hora_segundo)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return render_template('tempo_hora.html', titulo='meu form', msg=msg)

@app.route("/tempo/minuto/")
def min():
    return render_template('tempo_minuto.html', titulo='meu form')

@app.route("/tempo/minuto/data/", methods=['POST'])
def min_data():
    if request.method == 'POST':
        minuto = float(request.form['minuto'])
        temp = request.form['temp']
        if temp == "Hora":
            minuto_hora = float(minuto / 60)
            msg = "{} in hours is {}".format(minuto, minuto_hora)
        elif temp == "Segundo":
            minuto_segundo = float(minuto * 60)
            msg = "{} in hours is {}".format(minuto, minuto_segundo)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg

@app.route("/temperatura/celsius/")
def celsius():
    return render_template('calculo.html',
                           link='/temperatura/celsius/data/',
                           titulo='meu form',
                           unit='grau',
                           name='tempe',
                           value1='Fahrenheits',
                           value2='Kelvin',
                           id1='fahr',
                           id2='kelv',)

@app.route("/temperatura/celsius/data/", methods=['POST'])
def celsius_data():
    if request.method == 'POST':
        grau = float(request.form['grau'])
        tempe = request.form['tempe']
        if tempe == "Fahrenheits":
            celsius_fahr = float(grau * 1.8 + 32)
            msg = "{} in fahrenheits is {}".format(grau, celsius_fahr)
        elif tempe == "Kelvin":
            celsius_kelv = float(grau + 273)
            msg = "{} in kelvin is {}".format(grau, celsius_kelv)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return render_template('resultados.html', titulo='meu form', msg= msg)

@app.route("/temperatura/fahr/")
def fahr():
    return render_template('temp_fahr.html', titulo='meu form')

@app.route("/temperatura/fahr/data/", methods=['POST'])
def fahr_data():
    if request.method == 'POST':
        grau = float(request.form['grau'])
        tempe = request.form['tempe']
        if tempe == "Celsius":
            fahr_celsius = float((grau - 32) * (5/9))
            msg = "{} in celsius is {}".format(grau, fahr_celsius)
        elif tempe == "Kelvin":
            fahr_kelv = float((grau - 32) * (5/9) + 273)
            msg = "{} in kelvin is {}".format(grau, fahr_kelv)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg

@app.route("/temperatura/kelvin/")
def kelv():
    return render_template('temp_kelv.html', titulo='meu form')

@app.route("/temperatura/kelvin/data/", methods=['POST'])
def kelv_data():
    if request.method == 'POST':
        grau = float(request.form['grau'])
        tempe = request.form['tempe']
        if tempe == "Fahrenheits":
            kelv_fahr = float((grau - 273) * (9/5) + 32)
            msg = "{} in fahrenheits is {}".format(grau, kelv_fahr)
        elif tempe == "Celsius":
            kelv_celsius = float(grau - 273)
            msg = "{} in kelvin is {}".format(grau, kelv_celsius)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg

@app.route("/comp/metro/")
def metro():
    return render_template('comp_metro.html', titulo='meu form')

@app.route("/comp/metro/data/", methods=['POST'])
def metro_data():
    if request.method == 'POST':
        comp = float(request.form['comp'])
        opc = request.form['opc']
        if opc == "Centímetros":
            met_cm = float(comp  * 100)
            msg = "{}m in cm is {}".format(comp, met_cm)
        elif opc == "Quilômetros":
            met_km = float(comp / 1000)
            msg = "{}m in km is {}".format(comp, met_km)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg

@app.route("/comp/km/")
def km():
    return render_template('comp_km.html', titulo='meu form')

@app.route("/comp/km/data/", methods=['POST'])
def km_data():
    if request.method == 'POST':
        comp = float(request.form['comp'])
        opc = request.form['opc']
        if opc == "Centímetros":
            km_cm = float(comp * 100000)
            msg = "{}m in cm is {}".format(comp, km_cm)
        elif opc == "Metros":
            km_m = float(comp * 1000)
            msg = "{}m in m is {}".format(comp, km_m)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return msg

@app.route("/comp/cm/")
def cm():
    return render_template('comp_cm.html', titulo='meu form')

@app.route("/comp/cm/data/", methods=['POST'])
def cm_data():
    if request.method == 'POST':
        comp = float(request.form['comp'])
        opc = request.form['opc']
        if opc == "Quilômetros":
            cm_km = float(comp / 100000)
            msg = "{}m in cm is {}".format(comp, cm_km)
        elif opc == "Metros":
            cm_m = float(comp / 1000)
            msg = "{}m in m is {}".format(comp, cm_m)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return render_template('resultados.html', titulo='meu form', msg= msg)