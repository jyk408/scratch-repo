import torch
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda

dataset = datasets.FashionMNIST(
    root="data", # dataset 위치
    train=True, # 학습용 데이터셋
    download=True, # 데이터셋이 root 디렉토리에 없으면 다운로드
    # ToTensor()는 PIL image 혹은 numpy의 ndarray 를 FloatTensor로 변환하고 이미지의 픽셀 크기(intensity)값을 0~1범위로 조정(scale)
    transform=ToTensor(), # 데이터셋을 tensor로 변형
    # 다음 Lambda함수는 원-핫으로 부호화된 텐서로 바꾸는 함수이다.
    # 이 함수는 크기 10짜리 0을 만들고 scatter_를 호출해 주어진 정답 y 에 해당 하는 인덱스에 value=1을 할당한다
    target_transform=Lambda(lambda y : torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y), value=1))
)

