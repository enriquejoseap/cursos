# Dificultades

Segun Fred Brooks en su libro No Silver Bullet los problemas se dividen en dos, **esenciales**, que son aquellos problemas especificados desde un inicio, el entendimiento del concepto de lo que vamos a solucionar, comprender el diseño y de comprobación del concepto. En cambio los problemas **accidentales** son aquellos detalles de la implementación y producción actual.

## Problemas esenciales

Los problemas esencial los podemos dividir en 4:

### Complejidad

Es cuando lo que tenemos que resolver es complejo en si mismo, aquellos que requieren mucho cálculo y análisis.

### Conformidad

Se refiere al contexto que estará la solución final, como se debe adaptar a las adversidades, por ejemplo, sin el software va a requerir internet en todo momento.

### Tolerancia al cambio

Son aquellos problemas que surgen despues de haber finalizado el software. Si un software deberá de cambiarse y si es muy complejo cambiarlo, tiene que ver mucho con el cambio que pueda tener el problema en el tiempo y cuanto podemos adaptarnos al cambio.

### Invisibilidad

Lo difícil de trabajar con sofware es que es intangible e invisible por lo que puede ser complicado a la hora de entender lo que está pasando por detrás cuando lo estamos usando.

## Problemas accidentales

Es la dificultad de la implementacion en si misma

### Lenguajes de alto nivel

Se considera un problema accidental pues existe una barrera entre las máquina y los humanos para ser programadas y los lenguajes de alto nivel son el puente para cerrar un poco la brecha

### Multi-procesamiento

Se refiere al feedback de los procesos múltiples que realizamos durante la implemetación y evaluación, el tiempo de espera o la respuesta misma.

### Entornos de programación

Se requiere tener la capacidad de manejar las librerias, APIs, IDEs.

## Cómo resolver las dificultades esenciales?

### No desarrollar: Comprar - OSS

Si tenemos un problema muy complejo quizás la solución no sea desarrollar un sistema, es posible que ya alguien más haya pasado por lo mismo y se pueda adquirir a través de una compra u reutilizádolo

Otra forma de aprovechar el no comprar es utilizando soluciones open source, quizás utilizando bibliotecas que a lo mejor no nos resuelve el problema por completo pero nos lo reduce o soluciona una parte del problema.

### Prototipado rápido

Este concepto utiliza el paradigma de las metodologías agiles. La idea es obtener feedback lo antes posible para saber si estamos resolviendo el usario de forma correcta.

### Desarrollo evolutivo

Plantea que trates de obtener resultados más pequeños y evolucionarlos hasta dar con la solución. Tiene que ver también con las metodologías ágiles.

### Grandes diseñadores

Fred Brooks decía que necesitamos grandes diseñadores, no solo son programadores que conocen tecnología, sino aquellos que resuelvan los problemas de la forma más elegantes y simples con altos estándares de calidad.