"""
Dataset: 샘플과 정답(label)을 저장

DataLoader: dataset을 샘플에 접근할 수 있또록 iterable(순회가능한)객체로 감싼다
"""

import torch
from torch.utils.data import dataset, Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt

# 데이터셋 불러오기
training_data = datasets.FashionMNIST(
    root="data", # 학습/테스트 데이터가 저장되는 경로
    train=True, # 학습/테스트 데이터셋 여부를 선택
    download=True, # root에 데이터셋이 없는 경우 다운로드
    transform=ToTensor() # 특징(feature)과 정답(label) 변형(transform)을 지정
)

test_data = datasets.FashionMNIST(
    root="data", # 학습/테스트 데이터가 저장되는 경로
    train=False, # 학습/테스트 데이터셋 여부를 선택
    download=True, # root에 데이터셋이 없는 경우 다운로드
    transform=ToTensor() # 특징(feature)과 정답(label) 변형(transform)을 지정
)

# 데이터셋을 순회(iterate)하고 시각화하기
labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}

figure = plt.figure(figsize=(8, 8)) # 8x8사이즈의 이미지 시각화
cols, rows = 3, 3 # figure를 세로로 3개 가로로 3개 총 9개 표출
for i in range(1, cols*rows + 1): # figure 9개 표출
    sample_idx = torch.randint(len(training_data), size=(1,)).item()
    image, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[label])
    plt.imshow(image.squeeze(), cmap="gray")
plt.show()

# 파일에서 사용자 정의 데이터셋 만들기: Dataset클래스는 반드시 __init__, __len__, __getitem__이 구현되어야 한다
import os
import pandas as pd
from torchvision.io import read_image

class CustomImageDataset(Dataset):

    def __init__(self, annotations_file, image_directory, transform=None, target_transform=None):
        self.image_labels = pd.read_csv(annotations_file, names=['file_name', 'label'])
        self.image_directory = image_directory
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.image_labels)

    def __getitem__(self, index):
        image_path = os.path.join(self.image_directory, self.image_labels.iloc[index, 0])
        image = read_image(image_path)
        label = self.image_labels.iloc[index, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)

        return image, label


# DataLoader로 학습용 데이터 준비하기
from torch.utils.data import DataLoader

## DataLoader에 dataset을 넘겨 안에 샘플을 순회(iterate)
train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)

train_features, train_labels = next(iter(train_dataloader)) # train_dataset의 샘플을 64개씩 묶어 이미지 순서를 섞은 후 묶음(batch)를 반환
print(f"Feature batch shape: {train_features.size()}")
print(f"Label batch shape: {train_labels.size()}")

# 묶음(batch)의 첫 번째 feature와 label(정답)을 추출
image = train_features[0].squeeze()
label = train_labels[0]
plt.imshow(image, cmap="gray") # 해당 이미지를 plot에 넘겨 gray색상으로 화면에 출력
plt.show()
print(f"Label: {label}")


