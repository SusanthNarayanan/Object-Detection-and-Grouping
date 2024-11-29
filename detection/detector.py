import torch
from torchvision import transforms
from torchvision.models.detection import fasterrcnn_resnet50_fpn
import cv2
import numpy as np

# Load pre-trained detection model
model = fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

def detect_objects(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert BGR image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Transform the image into tensor and add batch dimension
    transform = transforms.Compose([transforms.ToTensor()])
    image_tensor = transform(image).unsqueeze(0)  # Add batch dimension
    
    # Perform detection
    with torch.no_grad():
        outputs = model(image_tensor)

    detections = []
    for box, label, score in zip(
        outputs[0]['boxes'], outputs[0]['labels'], outputs[0]['scores']
    ):
        if score > 0.5:  # Confidence threshold
            detections.append({
                "bbox": box.tolist(),
                "label": int(label),
                "score": float(score)
            })
    return detections
