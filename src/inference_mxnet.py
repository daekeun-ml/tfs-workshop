
import os
import time
import sys
import json
import subprocess
from base64 import b64decode

# Install/Update GluonCV:
subprocess.call([sys.executable, '-m', 'pip', 'install', 'gluoncv'])

import mxnet as mx
import gluoncv as gcv
ctx = mx.cpu()

def model_fn(model_dir=None):
    '''
    Loads the model into memory from storage and return the model.
    '''    
    net = gcv.model_zoo.get_model(
        'yolo3_darknet53_coco',
        pretrained=True,
        ctx=ctx,
    )
    net.hybridize(static_alloc=True, static_shape=True)
    #net.load_parameters(os.path.join(model_dir, 'model.params'), ctx=ctx)
    return net

def input_fn(request_body, content_type):
    '''
    Deserialize the request body
    '''    
    if content_type == 'application/json':
        D = json.loads(request_body)

        short = D.get('short')
        image = b64decode(D['image'])
        x, _ = gcv.data.transforms.presets.yolo.transform_test(
            mx.image.imdecode(image), short=short
        )
        return x
    else:
        raise RuntimeError(f'Not support content-type: {content_type}')


def predict_fn(input_object, model):
    '''
    Predicts on the deserialized object with the model from model_fn().
    '''
    x = input_object
    
    t0 = time.time()
    cid, score, bbox = model(x.as_in_context(ctx))
    t1 = time.time() - t0
    print("--- Elapsed time: %s secs ---" % t1)

    return x.shape, cid[0], score[0], bbox[0]


def output_fn(prediction, content_type):
    '''
    Serializes predictions from predict_fn() to JSON format.
    '''    
    shape, cid, score, bbox = prediction
    if content_type == 'application/json':
        return json.dumps({
            'shape': shape,
            'cid': cid.asnumpy().tolist(),
            'score': score.asnumpy().tolist(),
            'bbox': bbox.asnumpy().tolist()
        })
