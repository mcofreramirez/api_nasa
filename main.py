from pydoc import describe
from html_module import create_html_earth, create_html_pic
from apod import pull_fotos
from planet import pull_planetas
from show import show_pics
from validar import validate
from planet import pull_planetas
from earth import pull_earth


opcion = input(""" Bienvenido al Museo visual de la Nasa, creado para Amparo Cofré: ¿Listo para aprender?
    ¿Qué desea ver?
    1. Foto del Día
    2. Fotos de Planetas
    3. Ver la rotacion de la tierra en un día.
    0. Salir
    """)

opcion = int(validate(['0','1','2','3'], opcion))

while True:
    if  opcion == 1:
        n = int(input("""En este modulo podras ver la foto del día, esta es una foto emblematica tomada por la NASA. 
                Por favor indica cuantas fotos quieres ver
                >"""))
        id_foto = pull_fotos(n)
        html = create_html_pic(id_foto)
        with open('apod.html' , 'w') as f:
            f.write(html)
    if  opcion == 2:
        planeta = int(input("""En este modulo podras ver fotos emblematicas de la NASA.
                        Por favor escoge un planeta:
                        1. Mercurio
                        2. Venus
                        3. Tierra
                        4. Marte
                        5. Jupiter
                        6. Saturno
                        7. Urano
                        8. Neptuno
                        """))
        planeta = int (validate(['1','2','3','4','5','6','7','8'], planeta))    
        n = int(input("Cuantas fotos quieres ver?"))
        titulos, descripcion, fotos = pull_planetas(planeta, n)            
    if  opcion == 3:
        fecha = input(""" En este modulo podras ver la rotacion de la Tierra.
                       Escoje una fecha que deseas ver la tierra (no se puede la de hoy)
                    Formato : YYYY-MM-DD:""")
        fotos, horas = pull_earth(fecha)
        html = create_html_earth(fotos,horas)
        show_pics(html, 'tierra')
    else:
        exit()