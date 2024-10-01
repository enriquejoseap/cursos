# Estructura

En la version 3.0 de Dataform el archivo de configuracion se presenta con el nombre  **workflow_settings.yaml** file de la siguiente forma:

```
<!-- Your BigQuery Google Cloud project ID -->
defaultProject: my-gcp-project-id

<!-- El dataset de bigquery el cual Dataform creará assets, se llama dataform por defecto -->
defaultDataset: dataform

<!-- La region por defecto del dataset -->
defaultLocation: us-east1

<!-- El dataset de bigquery el cual crea vistas con resultados de aserción, se llama dataform_assertions por defecto -->
defaultAssertionDataset: dataform_assertions
```

# Contenido definido del archivo de configuración

<table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Type</th>
      <th>Label</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>dataformCoreVersion</td>
      <td><a href="#string">string</a></td>
      <td>&nbsp;</td>
      <td>The desired dataform core version to compile against.</td>
    </tr>
    <tr>
      <td>defaultProject</td>
      <td><a href="#string">string</a></td>
      <td>&nbsp;</td>
      <td>Required. The default Google Cloud project (database).</td>
    </tr>
    <tr>
      <td>defaultDataset</td>
      <td><a href="#string">string</a></td>
      <td>&nbsp;</td>
      <td>Required. The default dataset (schema).</td>
    </tr>
    <tr>
      <td>defaultLocation</td>
      <td><a href="#string">string</a></td>
      <td>&nbsp;</td>
      <td>Required. The default BigQuery location to use. For more information on BigQuery locations, see https://cloud.google.com/bigquery/docs/locations.</td>
    </tr>
    <tr>
      <td>defaultAssertionDataset</td>
      <td><a href="#string">string</a></td>
      <td>&nbsp;</td>
      <td>Required. The default dataset (schema) for assertions.</td>
    </tr>
    <tr>
      <td>vars</td>
      <td><a href="#dataform-WorkflowSettings-VarsEntry">WorkflowSettings.VarsEntry</a></td>
      <td>repeated</td>
      <td>Optional. User-defined variables that are made available to project code during compilation. An object containing a list of "key": value pairs.</td>
    </tr>
    <tr>
      <td>projectSuffix</td>
      <td><a href="#string">string</a></td>
      <td>&nbsp;</td>
      <td>Optional. The suffix to append to all Google Cloud project references.</td>
    </tr>
    <tr>
      <td>datasetSuffix</td>
      <td><a href="#string">string</a></td>
      <td>&nbsp;</td>
      <td>Optional. The suffix to append to all dataset references.</td>
    </tr>
    <tr>
      <td>namePrefix</td>
      <td><a href="#string">string</a></td>
      <td>&nbsp;</td>
      <td>Optional. The prefix to append to all action names.</td>
    </tr>
    <tr>
      <td>defaultNotebookRuntimeOptions</td>
      <td><a href="#dataform-NotebookRuntimeOptionsConfig">NotebookRuntimeOptionsConfig</a></td>
      <td>&nbsp;</td>
      <td>Optional. Default runtime options for Notebook actions.</td>
    </tr>
  </tbody>
</table>