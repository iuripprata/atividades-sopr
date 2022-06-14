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
lado_ = float(form.getvalue("lado"))
# calcula perimetro
perim_quad = float(lado_ * 4)
######## HTML
title = "Quadrado"
funcs.print_header(title)
print("<h1>Quadrado</h1><hr>")
print("<p>Lado: {:.1f}".format(lado_))
print("<p>Perímetro do Quadrado: {:.1f}".format(perim_quad))
print("<br><br>Clique <a href=\'../quadrado_perim.html\'> aqui</a> para um novo cálculo")
print("<body></html>")
funcs.print_footer()