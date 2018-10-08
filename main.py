import json

from google.cloud import storage
from google.cloud import vision

vision_client = vision.ImageAnnotatorClient()
storage_client = storage.Client()

with open('config.json') as f:
    config = json.loads(f.read())


def extract_text(data, context):
    print('Processing file gs://{}/{}'.format(data['bucket'], data['name']))

    gcs_source = vision.types.GcsSource(
        uri='gs://{}/{}'.format(data['bucket'], data['name']))
    input_config = vision.types.InputConfig(
        gcs_source=gcs_source, mime_type=data['contentType'])

    dest_uri = '{}/{}/'.format(config['output_path'], data['name'])
    print('Setting destination uri {}'.format(dest_uri))
    gcs_destination = vision.types.GcsDestination(uri=dest_uri)
    output_config = vision.types.OutputConfig(
        gcs_destination=gcs_destination, batch_size=config['batch_size'])

    feature = vision.types.Feature(
        type=vision.enums.Feature.Type.DOCUMENT_TEXT_DETECTION)
    async_request = vision.types.AsyncAnnotateFileRequest(
        features=[feature],
        input_config=input_config,
        output_config=output_config)

    print('Submitting Cloud Vision request')
    vision_client.async_batch_annotate_files(
        requests=[async_request])
