# Creación de particiones de tablas

Para crear una partición de tabla , se debe añadir una expresion de partición de Bigquery en el bloque de **bigquery**, esto se especifica en la definción del archivo sqlx

Dentro del bloque de bigquery se agrega la variable de **partitionBy** considerando los tipos de particiones posibles, fecha o entero

Además se puede establecer el filtro de partición para que en caso de que se realice una consulta a la tabla siempre de deba agregar el filtro de partición

```
config {
  type: "table",
  bigquery: {
    partitionBy: "DATE(ts)",
    requirePartitionFilter : true
  }
}
SELECT CURRENT_TIMESTAMP() AS ts
```

## Establecer la retención de particiones

Dentro del bloque de **bigquery** se agrega la variable **partitionExpirationDays**

```
config {
  type: "table",
  bigquery: {
    partitionBy: "DATE(ts)",
    partitionExpirationDays: 14,
  }
}
SELECT CURRENT_TIMESTAMP() AS ts
```

# Creación de clusters de tablas

Para crear un cluster de tabla se debe añadir un Bigquery clustering_column_list en el bloque de **bigquery** en la dificion del archivo sqlx

```
config {
  type: "table",
  bigquery: {
    partitionBy: "DATE(ts)",
    clusterBy: ["name", "revenue"]
  }
}
SELECT CURRENT_TIMESTAMP() as ts, name, revenue
```