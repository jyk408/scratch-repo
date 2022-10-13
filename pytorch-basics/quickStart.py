import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

"""
데이터 작업하기: 데이터 작업을 위한 torch.utils.data.DataLoader와 torch.utils.data.Dataset이 존재
Dataset은 샘플과 label(정답)을 저장하고 dataLoader는 dataset을 순회가능한(iterable)로 감싼다
"""

# 공개 데이터셋에서 학습 데이터를 내려받기
training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

# 공개 데이터셋에서 테스트 데이터를 내려받기
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)

batch_size = 64

# DataLoader생성
train_dataloader = DataLoader(training_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

for X, y in test_dataloader:
    print(f"Shape of X [N, C, H, W]: {X.shape}")
    print(f"Shape of y: {y.shape} {y.dtype}")
    break