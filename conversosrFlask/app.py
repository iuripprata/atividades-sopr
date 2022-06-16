from flask import Flask, redirect, render_template, request, flash, Markup, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, CSRFProtect
from wtforms.validators import DataRequired, Length, Regexp
from wtforms.fields import *
from flask_bootstrap import Bootstrap5, SwitchField


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
    return render_template('calculo.html',
                           link='/tempo/segundo/data/',
                           titulo='Conversor de Segundos',
                           unit='segundo',
                           name='temp',
                           value1='Minutos',
                           value2='Horas',
                           id1='min',
                           id2='hr',)

@app.route("/tempo/segundo/data/", methods=['POST'])
def seg_data():
    if request.method == 'POST':
        segundo = float(request.form['segundo'])
        temp = request.form['temp']
        if temp == "Minutos":
            seg_minuto = float(segundo / 60)
            msg = "{} in hours is {}".format(segundo, seg_minuto)
        elif temp == "Horas":
            seg_hora = float(segundo / 3600)
            msg = "{} in hours is {}".format(segundo, seg_hora)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return render_template('resultados.html', titulo='meu form', msg=msg, voltar='/tempo/segundo/')

@app.route("/tempo/hora/")
def hora():
    return render_template('calculo.html',
                           link='/tempo/hora/data/',
                           titulo='Conversor de Horas',
                           unit='hora',
                           name='temp',
                           value1='Minutos',
                           value2='Segundos',
                           id1='min',
                           id2='seg',)

@app.route("/tempo/hora/data/", methods=['POST'])
def hora_data():
    if request.method == 'POST':
        hora = float(request.form['hora'])
        temp = request.form['temp']
        if temp == "Minutos":
            hora_minuto = float(hora * 60)
            msg = "{} in hours is {}".format(hora, hora_minuto)
        elif temp == "Segundos":
            hora_segundo = float(hora * 3600)
            msg = "{} in hours is {}".format(hora, hora_segundo)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return render_template('resultados.html', titulo='meu form', msg=msg, voltar='/tempo/hora/')

@app.route("/tempo/minuto/")
def min():
    return render_template('calculo.html',
                           link='/tempo/minuto/data/',
                           titulo='Conversor de Minutos',
                           unit='minuto',
                           name='temp',
                           value1='Horas',
                           value2='Segundos',
                           id1='hr',
                           id2='seg',)

@app.route("/tempo/minuto/data/", methods=['POST'])
def min_data():
    if request.method == 'POST':
        minuto = float(request.form['minuto'])
        temp = request.form['temp']
        if temp == "Horas":
            minuto_hora = float(minuto / 60)
            msg = "{} in hours is {}".format(minuto, minuto_hora)
        elif temp == "Segundos":
            minuto_segundo = float(minuto * 60)
            msg = "{} in hours is {}".format(minuto, minuto_segundo)
        else:
            msg = "no data received"
    else:
        msg = "no data received"
    return render_template('resultados.html', titulo='meu form', msg=msg, voltar='/tempo/minuto/')

@app.route("/temperatura/celsius/")
def celsius():
    return render_template('calculo.html',
                           link='/temperatura/celsius/data/',
                           titulo='Conversor de',
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
    return render_template('resultados.html', titulo='meu form', msg=msg, voltar='/temperatura/celsius/')

@app.route("/temperatura/fahr/")
def fahr():
    return render_template('calculo.html',
                           link='/temperatura/fahr/data/',
                           titulo='Conversor de Fahrenheits',
                           unit='grau',
                           name='tempe',
                           value1='Celsius',
                           value2='Kelvin',
                           id1='celsiu',
                           id2='kelv',)

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
    return render_template('resultados.html', titulo='meu form', msg=msg, voltar='/temperatura/fahr/')

@app.route("/temperatura/kelvin/")
def kelv():
    return render_template('calculo.html',
                           link='/temperatura/kelvin/data/',
                           titulo='Conversor de Kelvin',
                           unit='grau',
                           name='tempe',
                           value1='Fahrenheits',
                           value2='Celsius',
                           id1='fahr',
                           id2='celsiu',)

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
    return render_template('resultados.html', titulo='meu form', msg=msg, voltar='/temperatura/kelvin/')

@app.route("/comp/metro/")
def metro():
    return render_template('calculo.html',
                           link='/comp/metro/data/',
                           titulo='Conversor de metros',
                           unit='comp',
                           name='opc',
                           value1='Centímetros',
                           value2='Quilômetros',
                           id1='cm',
                           id2='km',)

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
    return render_template('resultados.html', titulo='meu form', msg=msg, voltar='/comp/metro/')

@app.route("/comp/km/")
def km():
    return render_template('calculo.html',
                           link='/comp/km/data/',
                           titulo='Conversor de Quilômetros',
                           unit='comp',
                           name='opc',
                           value1='Centímetros',
                           value2='Metros',
                           id1='cm',
                           id2='m',)

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
    return render_template('resultados.html', titulo='meu form', msg=msg, voltar='/comp/km/')

@app.route("/comp/cm/")
def cm():
    return render_template('calculo.html',
                           link='/comp/cm/data/',
                           titulo='Conversor de Centímetros',
                           unit='comp',
                           name='opc',
                           value1='Quilômetros',
                           value2='Metros',
                           id1='km',
                           id2='m',)

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
    return render_template('resultados.html', titulo='meu form', msg=msg, voltar='/comp/cm/')