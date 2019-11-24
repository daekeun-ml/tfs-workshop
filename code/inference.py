import base64
import io
import json
import requests
from PIL import Image
import numpy as np

def input_handler(data, context):
    """ Pre-process request input before it is sent to TensorFlow Serving REST API

    Args:
        data (obj): the request data stream
        context (Context): an object containing request and configuration details

    Returns:
        (dict): a JSON-serializable dict that contains request body and headers
    """

    if context.request_content_type == 'application/x-image':
        image = Image.open(io.BytesIO(data.read()))
        #image = Image.open(io.BytesIO(open(data, 'rb').read()))
        image_np = np.asarray(image)
        instance = image_np[np.newaxis, ...]
        return json.dumps({"instances": instance.tolist()})
    else:
        _return_error(415, 'Unsupported content type "{}"'.format(context.request_content_type or 'Unknown'))


def output_handler(response, context):
    """Post-process TensorFlow Serving output before it is returned to the client.

    Args:
        response (obj): the TensorFlow serving response
        context (Context): an object containing request and configuration details

    Returns:
        (bytes, string): data to return to client, response content type
    """
    if response.status_code != 200:
        _return_error(response.status_code, response.content.decode('utf-8'))
    response_content_type = context.accept_header
    prediction = response.content
    return prediction, response_content_type


def _return_error(code, message):
    raise ValueError('Error: {}, {}'.format(str(code), message))