provider "google" {
  project = "your-project-id"
  region  = "us-central1"
}

resource "google_cloudfunctions_function" "dataflow_trigger_function" {
  name        = "dataflow-trigger-function"
  project     = "your-project-id"
  region      = "us-central1"
  runtime     = "python37"
  entry_point = "trigger_df_job"

  source_archive_bucket = "your-cloud-function-source-bucket"
  source_archive_object = "path/to/your/cloud-function/source.zip"

  trigger_http = true

  environment_variables = {
    ENVIRONMENT_VARIABLE_NAME = "value"
  }
}

resource "google_project_iam_binding" "dataflow_trigger_function_iam_binding" {
  project = "your-project-id"
  role    = "roles/cloudfunctions.invoker"

  members = [
    "serviceAccount:${google_cloudfunctions_function.dataflow_trigger_function.service_account_email}"
  ]
}

resource "google_dataflow_job" "dataflow_job" {
  name     = "dataflow-csv-to-bigquery"
  project  = "your-project-id"
  region   = "us-central1"

  template_gcs_path = "gs://dataflow-templates/latest/GCS_Text_to_BigQuery"
  parameters = {
    "inputFilePattern"                    = "gs://your-bucket/your-file.csv",
    "outputTable"                         = "your-project-id:your_dataset.your_table",
    "bigQueryLoadingTemporaryDirectory"   = "gs://your-temporary-directory",
    "javascriptTextTransformGcsPath"      = "gs://your-bucket/udf.js",
    "javascriptTextTransformFunctionName" = "transform",
    "JSONPath"                            = "gs://your-bucket/bq.json"
  }
}
