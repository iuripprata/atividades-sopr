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
lado1tri_ = float(form.getvalue("lado1tri"))
lado2tri_ = float(form.getvalue("lado2tri"))
base_tri_ = float(form.getvalue("base_tri"))
# calcula perimetro
perim_tri = float(lado1tri_ + lado2tri_ + base_tri_)
######## HTML
title = "Triângulo"
funcs.print_header(title)
print("<h1>Triângulo</h1><hr>")
print("<p>Base: {:.1f}".format(base_tri_))
print("<p>Lado 1: {:.1f}".format(lado1tri_))
print("<p>Lado 2: {:.1f}".format(lado2tri_))
print("<p>Perímetro do Triângulo: {:.1f}".format(perim_tri))
print("<br><br>Clique <a href=\'../triangulo_perim.html\'> aqui</a> para um novo cálculo")
funcs.print_footer()