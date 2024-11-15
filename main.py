import os
import time
import fade
from datetime import datetime
from colorama import init, Fore
from pystyle import Center

init()

Red = Fore.LIGHTRED_EX
Esmeralda = "\033[38;2;152;251;152m"
Reset = Fore.RESET
White = Fore.LIGHTWHITE_EX
Black = Fore.LIGHTBLACK_EX

os.system('cls & title "Token Formatter | discord.gg/moonlygg"')

def obtener_hora_actual():
    return datetime.now().strftime('%I:%M %p')

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def separar_elementos(opcion, entrada):
    elementos = entrada.split("\n")
    resultado = []

    for elemento in elementos:
        partes = elemento.split(":")
        hora_actual = obtener_hora_actual()
        
        if opcion == 1:  # Solo Token
            if len(partes) == 3:
                resultado.append(partes[2])
            else:
                print(f"{Esmeralda}{hora_actual}{Reset} {Red}(-){Reset} Formato inválido para: {Black}{elemento}{Reset}")
        
        elif opcion == 2:  # Email:Pass
            if len(partes) >= 2:
                resultado.append(f"{partes[0]}:{partes[1]}")
            else:
                print(f"{Esmeralda}{hora_actual}{Reset} {Red}(-){Reset} Formato inválido para: {Black}{elemento}{Reset}")
        
        elif opcion == 3:  # Email:Pass:Token
            if len(partes) == 3:
                resultado.append(f"{partes[0]}:{partes[1]}:{partes[2]}")
            else:
                print(f"{Esmeralda}{hora_actual}{Reset} {Red}(-){Reset} Formato inválido para: {Black}{elemento}{Reset}")
        
        else:
            print(f"{Esmeralda}{hora_actual}{Reset} {Red}(-){Reset} Opción no válida.")
            return []

    return resultado

def guardar_resultados(resultado, tokens):
    # Crear carpeta output con el formato de timestamp
    timestamp = time.strftime("%d-%m-%y %H-%M-%S")
    ruta_carpeta = os.path.join("output", timestamp)
    os.makedirs(ruta_carpeta, exist_ok=True)

    # Guardar resultados en un archivo separado
    archivo_resultado = os.path.join(ruta_carpeta, "tokens.txt")
    with open(archivo_resultado, "w") as archivo:
        archivo.write("\n".join(resultado))
    hora_actual = obtener_hora_actual()
    print(f"\n{Esmeralda}{hora_actual}{Reset} {Esmeralda}(+){Reset} Resultados guardados en: {Black}{archivo_resultado}{Reset}")

Logo_GUI = """
  __  __                   _          _____  _____ 
 |  \/  |                 | |        / ____|/ ____|
 | \  / | ___   ___  _ __ | |_   _  | |  __| |  __ 
 | |\/| |/ _ \ / _ \| '_ \| | | | | | | |_ | | |_ |
 | |  | | (_) | (_) | | | | | |_| | | |__| | |__| |
 |_|  |_|\___/ \___/|_| |_|_|\__, |  \_____|\_____| 
                              __/ |                
                             |___/ 
"""

# Aplicamos el efecto de color a la GUI utilizando la función CenterXcenter de la librería fade
Logo = fade.purplepink(Center.XCenter(Logo_GUI))

def mostrar_menu():
    print(Logo)
    print(f" Elige una opción:")
    print(f"    1. Solo Token")
    print(f"    2. Email:Pass")
    print(f"    3. Email:Pass:Token")
    print(f"    4. Salir")

def main():
    try:
        while True:
            limpiar_consola()  # Limpia la consola antes de mostrar el menú
            mostrar_menu()
            hora_actual = obtener_hora_actual()
            
            try:
                opcion = int(input(f"\n{Esmeralda}{hora_actual}{Reset} {White}(?){Reset} Ingresa el número de la opción: {Black}"))
            except ValueError:
                print(f"{Esmeralda}{hora_actual}{Reset} {Red}(-){Reset} Por favor, ingresa un número válido.\n")
                time.sleep(3)
                continue

            if opcion == 4:
                print(f"\n{Esmeralda}{hora_actual}{Reset} {Esmeralda}(+){Reset} Saliendo del programa. ¡Adiós!")
                break

            if opcion not in [1, 2, 3]:
                print(f"{Esmeralda}{hora_actual}{Reset} {Fore.RED}(-){Reset} Opción no válida. Intenta de nuevo.")
                continue

            # Leer los datos desde el archivo tokens.txt
            try:
                with open("tokens.txt", "r") as archivo:
                    entrada = archivo.read().strip()
            except FileNotFoundError:
                print(f"{Esmeralda}{hora_actual}{Reset} {Fore.RED}(-) Error: {Reset}El archivo 'tokens.txt' no existe. Por favor, créalo con los datos necesarios.\n")
                continue

            # Extraer todos los tokens originales del archivo
            tokens = [line.split(":")[2] for line in entrada.split("\n") if len(line.split(":")) == 3]

            # Procesar según la opción elegida
            resultado = separar_elementos(opcion, entrada)
            if resultado:
                guardar_resultados(resultado, tokens)
            else:
                print(f"{Esmeralda}{hora_actual}{Reset} {Fore.RED}(-){Reset} No se generaron resultados válidos.\n")

            # Pausar para regresar al menú principal y limpiar consola
            hora_actual = obtener_hora_actual()
            input(f"\n{Esmeralda}{hora_actual}{Reset} {Esmeralda}(+){Reset} Presiona la tecla Enter para regresar al menú principal...\n")
            limpiar_consola()

    except KeyboardInterrupt:
        hora_actual = obtener_hora_actual()
        print("\n")
        print(f"{Esmeralda}{hora_actual}{Reset} {Red}(-){Reset} Interrupción detectada. Saliendo del programa. ¡Hasta luego!")


if __name__ == "__main__":
    main()
