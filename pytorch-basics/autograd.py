import torch

x = torch.ones(5) # input tensor: [1, 1, 1, 1, 1]
y = torch.zeros(3) # expected output
weight = torch.rand(5, 3, requires_grad=True)
bias = torch.rand(3, requires_grad=True)
z = torch.matmul(x, weight) + bias # matrix multiplication (행렬 곱)
loss = torch.nn.functional.binary_cross_entropy_with_logits(z, y)

print(f"Gradient function for z: {z.grad_fn}")
print(f"Gradient function for loss: {loss.grad_fn}")

# 변화도(gradient) 계산
loss.backward() # 도함수(derivative) 계산
print(weight.grad)
print(bias.grad)

# 변화도 추적 멈추기: 모델을 학습 후 입력 데이터만 단순히 적용하기 위해 propagation(순전파) 연산만 필요할 경우
# 변화도 추적을 멈추는 이유
## 일부 매개변수를 고정된 매개변수로 표시. 즉, 사전학습된 신경망을 미세조정(fine-tuning)할 때 사용
## 변화도를 추적하지 않는 연산이 연산 속도가 빠르다
z = torch.matmul(x, weight) + bias
print(z.requires_grad)

with torch.no_grad():
    z = torch.matmul(x, weight) + bias

print(z.requires_grad)

## 변화도 계산을 멈추는 다른 방법 - detach()
z = torch.matmul(x, weight) + bias
z_detached = z.detach()
print(z_detached.requires_grad) # requires_grad 속성은 false일 경우 변화도 추적을 안함 (default: True)



