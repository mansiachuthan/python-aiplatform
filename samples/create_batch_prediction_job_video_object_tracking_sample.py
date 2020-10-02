# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START aiplatform_create_batch_prediction_job_video_object_tracking_sample]
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value


def create_batch_prediction_job_video_object_tracking_sample(
    display_name: str,
    model_name: str,
    gcs_source_uri: str,
    gcs_destination_output_uri_prefix: str,
    project: str,
):
    client_options = {"api_endpoint": "us-central1-aiplatform.googleapis.com"}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.JobServiceClient(client_options=client_options)
    location = "us-central1"
    parent = "projects/{project}/locations/{location}".format(
        project=project, location=location
    )
    model_parameters_dict = {"confidenceThreshold": 0.0}
    model_parameters = json_format.ParseDict(model_parameters_dict, Value())

    batch_prediction_job = {
        "display_name": display_name,
        # Format: 'projects/{project}/locations/{location}/models/{model_id}'
        "model": model_name,
        "model_parameters": model_parameters,
        "input_config": {
            "instances_format": "jsonl",
            "gcs_source": {"uris": [gcs_source_uri]},
        },
        "output_config": {
            "predictions_format": "csv",
            "gcs_destination": {"output_uri_prefix": gcs_destination_output_uri_prefix},
        },
    }
    response = client.create_batch_prediction_job(
        parent=parent, batch_prediction_job=batch_prediction_job
    )
    print("response")
    print(" name:", response.name)
    print(" display_name:", response.display_name)
    print(" model:", response.model)
    print(
        " model_parameters:", json_format.MessageToDict(response._pb.model_parameters)
    )
    print(" generate_explanation:", response.generate_explanation)
    print(" state:", response.state)
    print(" start_time:", response.start_time)
    print(" end_time:", response.end_time)
    print(" labels:", response.labels)
    input_config = response.input_config
    output_config = response.output_config
    dedicated_resources = response.dedicated_resources
    manual_batch_tuning_parameters = response.manual_batch_tuning_parameters
    output_info = response.output_info
    error = response.error
    partial_failures = response.partial_failures
    resources_consumed = response.resources_consumed
    completion_stats = response.completion_stats


# [END aiplatform_create_batch_prediction_job_video_object_tracking_sample]
