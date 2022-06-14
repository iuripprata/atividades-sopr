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
base_ = float(form.getvalue("base"))
altura_ = float(form.getvalue("altura"))
# calcula perimetro
perim_ret = float((base_ * 2) + (altura_ * 2))
######## HTML
title = "Retângulo"
funcs.print_header(title)
print("<h1>Retângulo</h1><hr>")
print("<p>Base: {:.1f}".format(base_))
print("<p>Altura: {:.1f}".format(altura_))
print("<p>Perímetro do Retângulo: {:.1f}".format(perim_ret))
print("<br><br>Clique <a href=\'../"
      "retangulo_perim.html\'> aqui</a> para um novo cálculo")
funcs.print_footer()
