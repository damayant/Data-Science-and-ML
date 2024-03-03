from googleapiclient.discovery import build

def trigger_df_job(cloud_event,env):
    service =  build('dataflow','v1b3')
    project = 'teak-brook-416012'
    template_path = 'gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery'
    template_body = {
        "inputFilePattern": "gs://bkt007/gcp_data_eng - user.csv",
        "JSONPath": "gs://df_bkt007_metadata/bq.json",
        "outputTable": "teak-brook-416012:user_data.user_test",
        "bigQueryLoadingTemporaryDirectory": "gs://df_bkt007_metadata",
        "javascriptTextTransformGcsPath": "gs://df_bkt007_metadata/udf.js",
        "javascriptTextTransformFunctionName": "transform"
    }
    request =  service.projects().templates().launch(projectId = project, gcsPath = template_path,body=template_body)
    response = request.execute()
    print(response)




# "parameters": {
#         "inputFilePattern": "gs://bkt007/gcp_data_eng - user.csv",
#         "JSONPath": "gs://df_bkt007_metadata/bq.json",
#         "outputTable": "teak-brook-416012:user_data.user_test",
#         "bigQueryLoadingTemporaryDirectory": "gs://df_bkt007_metadata",
#         "javascriptTextTransformGcsPath": "gs://df_bkt007_metadata/udf.js",
#         "javascriptTextTransformFunctionName": "transform"
#     }