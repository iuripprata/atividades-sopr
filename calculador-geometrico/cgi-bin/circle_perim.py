#C:\Users\Alunos\PycharmProjects\Projeto6\venv
import cgitb, cgi
import math
import funcs
#Habilita a visualização de erro
cgitb.enable(display=0, logdir="./")
# instancia um form para receber dados do navegador
form = cgi.FieldStorage()
################ logica do script
# recebe o valor do raio do usuário
raio_ = float(form.getvalue('raio'))
# calcula perimetro
perim_circ = float(math.pi * 2) * raio_
######## HTML
title = "Círculo"
funcs.print_header(title)
print("<h1>Círculo</h1><hr>")
print("<p>Raio: {:.1f}".format(raio_))
print("<p>Perímetro do círculo: {:.1f}".format(perim_circ))
print("<br><br>Clique <a href=\'../circulo_perim.html\'>aqui</a> para um novo cálculo")
funcs.print_footer()
