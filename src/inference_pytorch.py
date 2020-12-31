
# Built-Ins
import io, os, sys
import json
import subprocess, time

import numpy as np
from base64 import b64decode
from PIL import Image

import torch
import torchvision
from torchvision import datasets, transforms, models
from torchvision.models.detection import FasterRCNN
import torchvision.transforms as transforms
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    
def model_fn(model_dir=None):
    '''
    Loads the model into memory from storage and return the model.
    '''
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    # load the model onto the computation device
    model = model.eval().to(device)    
    return model


def transform_fn(model, request_body, content_type='application/x-image', accept_type=None):
    '''
    Deserialize the request body and predicts on the deserialized object with the model from model_fn()
    '''
    if content_type == 'application/x-image':             
        img = np.array(Image.open(io.BytesIO(request_body)))
    elif content_type == 'application/x-npy':    
        img = np.frombuffer(request_body, dtype='uint8').reshape(137, 236)   
    else:
        raise ValueError(
            'Requested unsupported ContentType in content_type : ' + content_type)

    t0 = time.time()
    
    test_transforms = transforms.Compose([
        transforms.ToTensor()
    ])
    img_tensor = test_transforms(img).to(device)
    img_tensor = img_tensor.unsqueeze(0)
    
    with torch.no_grad():    
        result = model(img_tensor)

    t1 = time.time() - t0
    print("--- Elapsed time: %s secs ---" % t1)
    
    scores = result[0]['scores'].detach().cpu().numpy()
    bboxes = result[0]['boxes'].detach().cpu().numpy()
    cids = result[0]['labels'].detach().cpu().numpy()     
    
    outputs = json.dumps({'score': scores.tolist(), 
                       'bbox': bboxes.tolist(),
                         'cid': cids.tolist()})
    
    return outputs
