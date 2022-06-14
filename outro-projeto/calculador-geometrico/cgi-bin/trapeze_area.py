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
alturaT_ = float(form.getvalue("alturaT"))
# calcula área
area_trap = float(((base_maior_ * base_menor_) * alturaT_)/2)
######## HTML
title = "Trapézio"
funcs.print_header(title)
print("<h1>Trapézio</h1><hr>")
print("<p>Base Maior: {:.1f}".format(base_maior_))
print("<p>Base Menor: {:.1f}".format(base_menor_))
print("<p>Altura: {:.1f}".format(alturaT_))
print("<p>Área do Trapézio: {:.1f}".format(area_trap))
print("<br><br>Clique <a href=\'../trapezio_area.html\'> aqui</a> para um novo cálculo")
funcs.print_footer()