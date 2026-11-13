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

## CR-015: Cálculo automático del envío y del total
- **Descripción:** calcular el costo de envío y el total del pedido.
- **Tipo de cambio:** nueva funcionalidad.
- **Justificación:** solicitud de la gerencia comercial.
- **Requisitos afectados:** RN-02, RN-03 y RN-04.
- **Archivos afectados:** codigo/pedidos.py, documentos/requisitos.md, cambios/solicitudes.md.
- **Riesgo:** medio, cambia el cálculo de los pedidos.
- **Criterio de aceptación:** los casos 80×3, 100×3 y 150×3 dan los totales 260, 300 y 450.
- **Decisión:** aprobada (simulada).
