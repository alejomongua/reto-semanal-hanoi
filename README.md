# reto-semanal-hanoi

Reto semanal de FaztWeb:

_Cuenta la leyenda que en el gran templo de Benares existe una base de bronce de la que sobresalen tres varillas de diamante. En el momento de la creación, Dios coloco 64 discos de oro ensartados en la primera varilla, colocados de abajo arriba en orden de tamaño decreciente; esta es la torre de Brahma. Los sacerdotes están tratando de pasar la pila de la primera varilla a la segunda, sometidos a las leyes de Brahma que indican que solo se puede mover un disco a la vez, y que en ningún momento se puede colocar un disco mas grande sobre uno mas pequeño. Se cuenta con la tercera varilla para colocar los discos temporalmente. Cuando todos los discos hayan sido transferidos, la torre, los sacerdotes, el templo, y todo el mundo desaparecerá con un estruendo (Enunciado original del hoy conocido como problema de las torres de Hanoi)._

## Desarrollo del reto

Lo primero que hice fue hacer manualmente los casos mas sencillos para intentar encontrar un patrón:

```
# Caso con un solo disco
1- - -
- - 1-


# Caso con dos discos
12- - -
2- 1- -
- 1- 2-
- - 12-


# Caso con tres discos
123- - -
23- - 1-
3- 2- 1-
3- 12- -
- 12- 3-
1- 2- 3-
1- - 23-
- - 123-


# Caso con cuatro discos
1234- - -
234- 1- -
34- 1- 2-
34- - 12-
4- 3- 12-
14- 3- 2-
14- 23- -
4- 123- -
- 123- 4-
- 23- 14-
2- 3- 14-
12- 3- 4-
12- - 34-
2- 1- 34-
- 1- 234-
- - 1234-


# Caso con cinco discos
12345- - -
2345- - 1-
345- 2- 1-
345- 12- -
45- 12- 3-
145- 2- 3-
145- - 23-
45- - 123-
5- 4- 123-
5- 14- 23-
25- 14- 3-
125- 4- 3-
125- 34- -
25- 34- 1-
5- 234- 1-
5- 1234- -
- 1234- 5-
1- 234- 5-
1- 34- 25-
- 34- 125-
3- 4- 125-
3- 14- 25-
23- 14- 5-
... Aqui ya me aburrí
```

Noté dos cosas:

* La cantidad de movimientos es 2^n - 1 donde n es la cantidad de discos
* El patrón que encontré es que toca resolver primero el nivel anterior en la columna auxiliar, luego mover el disco más grande a la varilla de destino y luego volver a ejecutar el algoritmo, pero esta vez partiendo de la varilla auxiliar

La primera afirmación la usé como validación de mi algoritmo, y la segunda me sirvió para idear la función recursiva
