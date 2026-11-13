# Solicitudes de cambio

## INC-014: El subtotal devuelve el precio unitario
- **Descripción:** calcular_subtotal() devuelve el precio sin multiplicar por la cantidad.
- **Tipo de cambio:** corrección de incidencia.
- **Justificación:** para precio 80 y cantidad 3 el sistema muestra 80 en lugar de 240.
- **Requisito afectado:** RN-01.
- **Archivos afectados:** codigo/pedidos.py.
- **Riesgo:** alto, todos los totales de pedidos serían incorrectos.
- **Criterio de aceptación:** para precio 80 y cantidad 3, el subtotal es 240.
- **Decisión:** aprobada (simulada).
