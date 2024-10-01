# Sobre los assertions

Un assertion o aserción es un test de calidad de la data que encuentra las filas que violan una o más reglas especificadas en el query. Si el query devuelve filas, la aserción falla. Dataform ejectuta las aserciones cada vez que se actualiza el workflow sql y alerta si una aserción falla.

Dataform crea automáticamente vistas en Bigquery que contienen los resultados de la consulta de la aserción 

```
config {
  type: "table",
  assertions: {
    nonNull: ["user_id", "customer_id", "email"]
  }
}
SELECT ...
```