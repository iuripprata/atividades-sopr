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
base_maior_ = float(form.getvalue("base_maior"))
base_menor_ = float(form.getvalue("base_menor"))
lado1_ = float(form.getvalue("lado1"))
lado2_ = float(form.getvalue("lado2"))

# calcula perimetro
perim_trap = float(base_maior_ + base_menor_ + lado1_ + lado2_)
######## HTML
title = "Trapézio"
funcs.print_header(title)
print("<h1>Trapézio</h1><hr>")
print("<p>Base Maior: {:.1f}".format(base_maior_))
print("<p>Base Menor: {:.1f}".format(base_menor_))
print("<p>Lado 1: {:.1f}".format(lado1_))
print("<p>Lado 2: {:.1f}".format(lado2_))
print("<p>Perímetro do Trapézio: {:.1f}".format(perim_trap))
print("<br><br>Clique <a href=\'../trapezio_perim.html\'> aqui</a> para um novo cálculo")
funcs.print_footer()