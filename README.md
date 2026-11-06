# Cajero ATM por consola

Simulador de un cajero automático hecho en Python que se ejecuta en la terminal. Lo desarrollé para practicar los fundamentos del lenguaje: variables, condicionales, ciclos y validaciones.

## Funcionalidades

- Acceso con PIN, con un máximo de 4 intentos. Si todos fallan, la tarjeta se retiene y el programa termina.
- Menú interactivo con cuatro opciones:
  1. Consultar saldo
  2. Depositar
  3. Retirar
  4. Salir

## Reglas del cajero

- Saldo inicial: $10,000.
- Retiro máximo por operación: $7,000.
- No permite retirar más que el saldo disponible ni montos menores o iguales a cero.
- PIN de prueba: `7777`.

## Lo que practiqué

- Ciclos `for` y `while`, y uso de `break`.
- Condicionales (`if`, `elif`, `else`) para validar operaciones.
- Constantes, variables y formato de texto con f-strings.
- Entrada de datos con `input()` y conversión de tipos.


## Autor

Uriel
