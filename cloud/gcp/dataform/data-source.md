# Declarar un data source

Solo de puede declarar un data source en una declaración de archivo sqlx. Para declarar un data source en el bloque de configuración se debe establecer el **type** a "declaration"

```
config {
    type: "declaration",
    database: "bigquery-public-data",
    schema: "samples",
    name: "shakespeare",
}
```