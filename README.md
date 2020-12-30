# Deep Learning Inference Hands-on-Lab

## Introduction
​
Amazon SageMaker에서 딥러닝 모델을 모두 훈련하고 추론(inference)해야 하나요? 그렇지 않습니다.
<p>
만약 여러분이 SageMaker에서 훈련 없이 추론만 수행하고 싶다면, 여러분의 온프레미스(on-premise)에서 학습한 모델이나 공개 모델 저장소(model zoo)에 저장되어 있는 사전 훈련된(pre-trained) 모델들을 도커(Docker) 이미지 빌드 없이 곧바로 Amazon SageMaker Endpoint에 모델을 배포할 수 있습니다. 즉, 복잡한
절차 없이 오토스케일링(auto-scaling), A/B 테스트, 고가용성(high availability) 기능을 쉽게 이용할 수 있습니다. 
<p>
이 워크샵을 통해 여러분은 딥러닝 프레임워크로 사전 훈련된 모델을 Amazon SageMaker Endpoint로 호스팅하는 방법을 배울 수 있습니다.

1. [사전 준비 (Optional)](get_started.md)
2. [PyTorch로 사전 훈련한 모델을 Endpoint로 호스팅](pytorch-serving-endpoint.ipynb)
3. [MXNet으로 사전 훈련한 모델을 Endpoint로 호스팅](mxnet-serving-endpoint.ipynb)
4. [TensorFlow로 사전 훈련한 모델을 Endpoint로 호스팅](tensorflow-serving-endpoint.ipynb)

## License Summary

이 샘플 코드는 MIT-0 라이센스에 따라 제공됩니다. LICENSE 파일을 참조하십시오.