import cv2
import numpy
import ultralytics
import torch

print("OpenCV:", cv2.__version__)
print("NumPy:", numpy.__version__)
print("Ultralytics:", ultralytics.__version__)
print("PyTorch:", torch.__version__)
print("GPU bor:", torch.cuda.is_available())