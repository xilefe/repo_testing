# repo_testing
Script en Python creado en colaboración con el compañero del Master en desarrollo Blockchain IberoFVP.

Este código es un script en Python que ayuda a determinar los ingresos y gastos de una persona que trabaja ya sea por cuenta ajena o como autónomo. A continuación, se detallan los pasos que sigue el código:

Se importan dos módulos: "time" para utilizar una función de temporizador y "termcolor" para imprimir texto en colores en la terminal.
Se define una función llamada "claseTrabajo" que utiliza un bucle "while" para pedir al usuario si trabaja por cuenta ajena o como autónomo. La función devuelve la respuesta del usuario en forma de cadena (string).
Se define otra función llamada "tipo_jornada" que recibe como parámetro la respuesta de la función anterior. Esta función utiliza un bucle "while" para pedir al usuario si trabaja a tiempo parcial o a jornada completa. Al igual que la función anterior, devuelve la respuesta del usuario en forma de cadena (string).
Se define otra función llamada "ingresos" que recibe como parámetros la respuesta de las dos funciones anteriores ("tipotrabajo" y "jornada"). En esta función, se pide al usuario que ingrese información sobre sus ingresos dependiendo de si trabaja por cuenta ajena o como autónomo. La función devuelve tres valores: "facturacion_mensual" (en caso de ser autónomo), "EU_semana" (en caso de ser por cuenta ajena) y "num_pagas".
Se define otra función llamada "gastos" que no recibe parámetros. En esta función, se pide al usuario que ingrese información sobre sus gastos mensuales en distintas categorías (alquiler o hipoteca, agua, luz, gas, comida y móvil). La función devuelve seis valores correspondientes a cada categoría de gastos.
En el cuerpo principal del programa, se llaman a las funciones definidas anteriormente para obtener la información de ingresos y gastos del usuario. Luego, se realizan cálculos para determinar la renta disponible y se imprime el resultado en la terminal.
