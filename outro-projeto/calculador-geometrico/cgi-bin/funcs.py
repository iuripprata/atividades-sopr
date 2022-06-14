#C:\Users\Alunos\PycharmProjects\Projeto6\venv

def print_header(title):
    print("Content-type:text/html\r\n\r\n")
    print("""<html>
                <head>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
                    <title>{}</title>
                </head>
                <body>""".format(title))
    print("""<h1 class="display-1">{}</h1><hr>""".format(titulo))


def print_footer():
    print("</body></html>")

def titulo(titulo):
    print("""Content-type:text/html\r\n\r\n""")
    print("""<h1 class="display-1">{}</h1><hr>""".format(titulo))