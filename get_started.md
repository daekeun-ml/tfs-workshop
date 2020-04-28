# 사전 준비

## S3 Bucket 생성하기 

SageMaker는 S3를 데이터와 모델 저장소로 사용합니다. 여기서는 해당 목적으로 S3 Bucket을 생성합니다. 본 실습에서는 `Seoul (ap-northeast-2)` 리전을 사용합니다.<br>

1. [AWS 관리 콘솔](https://console.aws.amazon.com/)에 Sign in 합니다. <br>
    만약 AWS 측에서 Event Engine을 사용하여 임시 아이디를 생성한 경우 제공받으신 URL을 여시고 team hash code를 입력하시면 됩니다.<br>
    Event Engine 접속 가이드는 https://bit.ly/workshop-guide-sagemaker 를 참조해 주세요.

1. AWS Services 리스트에서 S3 로 이동합니다.
1. `"+ Create Bucket"` 버튼을 선택합니다.
1. 아래 내용 설정 후 화면 왼쪽 아래 Create 클릭합니다.

* Bucket name: sagemaker-hol-{userid}  [반드시 고유한 값 설정] 
* Region : Asia Pacific (Seoul)
    ![001](./images/doc/001.png?classes=border)

## Notebook instance 생성

1. 새로운 Notebook instance를 생성하기 위해 왼쪽 패널 메뉴 중 Notebook Instances 선택 후 오른쪽 상단의 `Create notebook instance` 버튼을 클릭합니다.

    ![002](./images/doc/002.png?classes=border)

1. Notebook instance 이름으로 `sagemaker-inference-hol-[YOUR-NAME]` 으로 넣은 뒤 `ml.t2.medium` 인스턴스 타입을 선택합니다. 

    ![003](./images/doc/003.png?classes=border)

1. IAM role은 `Create a new role` 을 선택하고, 생성된 팝업 창에서는 `S3 buckets you specify – optional` 밑에 `Specific S3 Bucket` 을 선택 합니다. 그리고 텍스트 필드에 위에서 만든 S3 bucket 이름(예: sagemaker-xxxxx)을 선택 합니다. 이후 `Create role` 을 클릭합니다.

    ![004](./images/doc/004.png?classes=border)

1. 다시 Create Notebook instance 페이지로 돌아온 뒤 `Create notebook instance` 를 클릭합니다.

## Notebook Instance 접근하기

1. 서버 상태가 `InService` 로 바뀔 때까지 기다립니다. 보통 5분정도의 시간이 소요 됩니다. 
1. `Open Jupyter`를 클릭하면 방금 생성한 notebook instance의 Jupyter 홈페이지로 이동하게 됩니다.

    ![005](./images/doc/005.png?classes=border)
    
1. 본 핸즈온 실습에 필요한 파일들을 github 저장소에서 복사하기 위해 Jupyter 홈페이지의 오른쪽 상단의 New 버튼을 클릭 후, Terminal 항목을 클릭합니다.

    ![006](./images/doc/006.png?classes=border)

1. 검은색 Terminal 화면이 출력되면, 아래의 명령어를 순차적으로 입력합니다. 이 과정은 네트워크 속도에 따라 변동적이지만 평균적으로 약 10초 정도 소요됩니다.

    ```
    $ cd SageMaker
    $ git clone https://github.com/daekeun-ml/tfs-workshop.git
    ```
    ![007](./images/doc/007.png?classes=border)

1. Github 코드가 복사되었으면 Google object detection API를 아래의 명령어로 설치합니다. 이 API는 TensorFlow Serving에는 필요 없지만, 추론(inference) 결과를 확인할 때 유용하게 활용할 수 있습니다. 이 과정은 네트워크 속도에 따라 변동적이지만, 약 2분 정도 소요됩니다.

    ```
    $ cd tfs-workshop/files
    $ bash init.sh
    ```
    ![008](./images/doc/008.png?classes=border)        

1. 아래 스크린샷처럼 `Finished processing dependencies for object-detection==0.1` 문구가 정상적으로 출력되었는지 확인합니다.

    ![009](./images/doc/009.png?classes=border)        

1. 다시 Jupyter Notebook 홈페이지로 돌아가서 `tfs-workshop` 폴더가 생성되었는지 확인하고,  `tfs-workshop` 폴더를 클릭합니다.

    ![010](./images/doc/010.png?classes=border)   

1. 아래 스크린샷의 파일들이 정상적으로 생성되었는지 확인합니다. `.ipynb` 파일들이 다음 모듈에서 실습으로 사용하게 될 코드들입니다. 

    ![011](./images/doc/011.png?classes=border)   

수고하셨습니다. 준비 과정을 완료하였습니다. <br>
이어서 TensorFlow로 사전 훈련한 모델을 Endpoint로 호스팅하는 방법은 `tensorflow-serving-endpoint.ipynb`을, 
MXNet(GluonCV)으로 사전 훈련한 모델을 Endpoint로 호스팅하는 방법은 `mxnet-serving-endpoint.ipynb`을 실행하시면 됩니다.
