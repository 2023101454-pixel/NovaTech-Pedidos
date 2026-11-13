UMBRAL_ENVIO_GRATIS = 300   # RN-02 y RN-03
COSTO_ENVIO = 20            # RN-03

def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_envio(subtotal):
    if subtotal >= UMBRAL_ENVIO_GRATIS:
        return 0
    return COSTO_ENVIO

def calcular_total(subtotal):
    return subtotal + calcular_envio(subtotal)

if __name__ == "__main__":
    precio = 80
    cantidad = 3
    subtotal = calcular_subtotal(precio, cantidad)
    envio = calcular_envio(subtotal)
    total = calcular_total(subtotal)
    print("Subtotal: S/", subtotal)
    print("Costo de envío: S/", envio)
    print("Total: S/", total)
