peliculas = ["Los juegos del hambre", "El club de la pelea", "El gran truco", 
             "Gladiador", "Tiempos violentos"]

precios = {
    "Los juegos del hambre": 25,
    "El club de la pelea": 50,
    "El gran truco": 40,
    "Gladiador": 80,
    "Tiempos violentos": 100
}

reservas = []

def cambiar_precio():
    print("\n--- Cambiar precio de una película ---")
    for peli in peliculas:
        print(f"{peli}: Q{precios[peli]}")
    nombre = input("Ingrese el nombre de la película cuyo precio desea cambiar: ")
    if nombre in peliculas:
        nuevo_precio = int(input(f"Ingrese el nuevo precio para '{nombre}': "))
        precios[nombre] = nuevo_precio
        print(f"Precio actualizado. Nuevo precio de '{nombre}': Q{nuevo_precio}")
    else:
        print("La película no está en la lista.")


pregunta=input("Deseas cambiar el precio de una pelicula (s/n)")
if pregunta == "s":
    cambiar_precio()
elif pregunta == "n":
    print()
print("Películas disponibles:")
for i in peliculas:
    print("-", i)

cliente = input("Ingrese el nombre del cliente: ")
pelicula = input("Ingrese el nombre de la película: ")
boletos = int(input("Ingrese la cantidad de boletos que desea comprar: "))

costo = 0

if pelicula in peliculas:
    if pelicula == "Los juegos del hambre":
        costo = boletos * precios["Los juegos del hambre"]
    elif pelicula == "El club de la pelea":
        costo = boletos * precios["El club de la pelea"]
    elif pelicula == "El gran truco":
        costo = boletos * precios["El gran truco"]
    elif pelicula == "Gladiador":
        costo = boletos * precios["Gladiador"]
    elif pelicula == "Tiempos violentos":
        costo = boletos * precios["Tiempos violentos"]
    
    print("Total a pagar:", costo)

    reserva = {
        "cliente": cliente,
        "pelicula": pelicula,
        "boletos": boletos,
        "total": costo
    }
    reservas.append(reserva)

    print("-----Resumen de la reservación------")
    print("Cliente:", cliente)
    print("Película:", pelicula)
    print("Boletos comprados:", boletos)
    print("Total a pagar:", costo)

else:
    print("La película no está disponible.")
