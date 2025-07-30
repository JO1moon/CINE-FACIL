peliculas = ["Los juegos del hambre", "El club de la pelea", "El gran truco", 
             "Gladiador", "Tiempos violentos"]

reservas = []

print("Películas disponibles:")
for i in peliculas:
    print("-", i)

cliente = input("Ingrese el nombre del cliente: ")
pelicula = input("Ingrese el nombre de la película: ")
boletos = int(input("Ingrese la cantidad de boletos que desea comprar: "))

costo = 0

if pelicula in peliculas:
    if pelicula == "Los juegos del hambre":
        costo = boletos * 25
    elif pelicula == "El club de la pelea":
        costo = boletos * 50
    elif pelicula == "El gran truco":
        costo = boletos * 40
    elif pelicula == "Gladiador":
        costo = boletos * 80
    elif pelicula == "Tiempos violentos":
        costo = boletos * 100
    
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
