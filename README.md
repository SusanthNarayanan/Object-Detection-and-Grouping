# Object Detection and Grouping System with Visualization (Basic)

## Overview  
This project implements an AI-powered pipeline for object detection, grouping, and visualization using a Flask web application. The core features include:  

- **Flask Application**: Handles user interactions and serves API routes.  
- **Object Detection Model (Faster R-CNN)**: Detects objects in uploaded images.  
- **Grouping**: Groups detected objects based on their spatial locations using KMeans clustering.  
- **Visualization**: Draws bounding boxes and group labels on images for better interpretability.  

---

## Key Features  
1. **Image Upload**: Users can upload a single image or process images in bulk.  
2. **Object Detection**: Faster R-CNN processes images to detect objects with bounding boxes, labels, and confidence scores.  
3. **KMeans Clustering**: Groups detected objects based on spatial proximity.  
4. **Visualization**: Outputs images with color-coded bounding boxes and group IDs.  
5. **Bulk Processing**: Processes all images in a folder, applying detection, grouping, and visualization.  

---

## Application Flow  

### 1. User Uploads Image  
- Users upload an image via an HTML form with optional parameters:  
  - **Confidence Threshold**: Minimum confidence required for detection.  
  - **IoU Threshold**: Controls the overlap allowed between bounding boxes during Non-Maximum Suppression (NMS).  

### 2. Object Detection  
- The uploaded image is processed by a pre-trained Faster R-CNN model.  
- Bounding boxes, class labels, and confidence scores are extracted.  

### 3. Grouping  
- KMeans clustering groups detected objects based on the centers of bounding boxes.  

### 4. Visualization  
- Bounding boxes are drawn on the image with group labels.  
- The resulting image is saved in the `static/visualizations/` folder.  

### 5. Bulk Processing  
- The system processes all images in the `sample_images/` folder, generating detection, grouping, and visualization outputs for each image.  

---

## Input/Output Formats  

### **Input**  

1. **Single Image Upload** (`/upload`):  
   - **POST Request** with:  
     - `image`: Image file.  
     - `conf_threshold`: Confidence threshold (optional).  
     - `iou_threshold`: IoU threshold (optional).  

2. **Bulk Processing** (`/process_bulk`):  
   - **GET Request** with:  
     - `conf_threshold`: Confidence threshold (optional).  
     - `iou_threshold`: IoU threshold (optional).  

### **Output**  
The output includes:  
- **detections**: Bounding boxes, class labels, and confidence scores for detected objects.  
- **groups**: Group IDs assigned to objects based on clustering.  
- **visualization_path**: Path to the visualized image with bounding boxes and group labels.  

---

## Folder Structure  

```plaintext
project/
│
├── sample_images/           # Uploaded input images  
├── static/visualizations/   # Output images with visualizations  
├── templates/               # HTML templates for the web interface  
│   └── index.html           # Upload form and parameters  
├── app.py                   # Main Flask application  
├── detection/  
│   └── detector.py          # Object detection logic using Faster R-CNN  
├── grouping/  
│   └── grouper.py           # KMeans clustering logic  
├── utils/  
│   └── visualization.py     # Visualization utilities for drawing bounding boxes  
├── requirements.txt         # Python dependencies  
└── README.md                # Project documentation  
