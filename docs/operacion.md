# Operación

## Validación básica

Get from database

## Checklist operativo mínimo

- Validar que el servicio esté desplegado.
- Revisar logs de aplicación.
- Validar health check si aplica.
- Revisar últimas ejecuciones del pipeline.
- Confirmar si existen alertas activas.

## Troubleshooting inicial

### El servicio no responde

1. Revisar si el servicio está arriba.
2. Validar configuración de red.
3. Revisar logs recientes.
4. Revisar cambios recientes en el repositorio.

### El pipeline falla

1. Revisar el job fallido.
2. Validar dependencias.
3. Revisar cambios recientes en configuración.