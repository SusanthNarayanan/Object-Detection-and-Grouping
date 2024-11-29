<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Object Detection and Grouping System</title>
</head>
<body>
  <h1>Object Detection and Grouping System with Visualization</h1>

  <h2>Overview</h2>
  <p>
    This project implements an AI-powered pipeline for object detection, grouping, and visualization using a Flask web application. The core features include:
  </p>
  <ul>
    <li><strong>Flask Application</strong>: Handles user interactions and serves API routes.</li>
    <li><strong>Object Detection Model (Faster R-CNN)</strong>: Detects objects in uploaded images.</li>
    <li><strong>Grouping</strong>: Groups detected objects based on their spatial locations using KMeans clustering.</li>
    <li><strong>Visualization</strong>: Draws bounding boxes and group labels on images for better interpretability.</li>
  </ul>

  <hr>

  <h2>Key Features</h2>
  <ol>
    <li><strong>Image Upload</strong>: Users can upload a single image or process images in bulk.</li>
    <li><strong>Object Detection</strong>: Faster R-CNN processes images to detect objects with bounding boxes, labels, and confidence scores.</li>
    <li><strong>KMeans Clustering</strong>: Groups detected objects based on spatial proximity.</li>
    <li><strong>Visualization</strong>: Outputs images with color-coded bounding boxes and group IDs.</li>
    <li><strong>Bulk Processing</strong>: Processes all images in a folder, applying detection, grouping, and visualization.</li>
  </ol>

  <hr>

  <h2>Application Flow</h2>

  <h3>1. User Uploads Image</h3>
  <ul>
    <li>Users upload an image via an HTML form with optional parameters:
      <ul>
        <li><strong>Confidence Threshold</strong>: Minimum confidence required for detection.</li>
        <li><strong>IoU Threshold</strong>: Controls the overlap allowed between bounding boxes during Non-Maximum Suppression (NMS).</li>
      </ul>
    </li>
  </ul>

  <h3>2. Object Detection</h3>
  <ul>
    <li>The uploaded image is processed by a pre-trained Faster R-CNN model.</li>
    <li>Bounding boxes, class labels, and confidence scores are extracted.</li>
  </ul>

  <h3>3. Grouping</h3>
  <ul>
    <li>KMeans clustering groups detected objects based on the centers of bounding boxes.</li>
  </ul>

  <h3>4. Visualization</h3>
  <ul>
    <li>Bounding boxes are drawn on the image with group labels.</li>
    <li>The resulting image is saved in the <code>static/visualizations/</code> folder.</li>
  </ul>

  <h3>5. Bulk Processing</h3>
  <ul>
    <li>The system processes all images in the <code>sample_images/</code> folder, generating detection, grouping, and visualization outputs for each image.</li>
  </ul>

  <hr>

  <h2>Input/Output Formats</h2>

  <h3>Input</h3>
  <ol>
    <li><strong>Single Image Upload</strong> (<code>/upload</code>):
      <ul>
        <li><strong>POST Request</strong> with:
          <ul>
            <li><code>image</code>: Image file.</li>
            <li><code>conf_threshold</code>: Confidence threshold (optional).</li>
            <li><code>iou_threshold</code>: IoU threshold (optional).</li>
          </ul>
        </li>
      </ul>
    </li>
    <li><strong>Bulk Processing</strong> (<code>/process_bulk</code>):
      <ul>
        <li><strong>GET Request</strong> with:
          <ul>
            <li><code>conf_threshold</code>: Confidence threshold (optional).</li>
            <li><code>iou_threshold</code>: IoU threshold (optional).</li>
          </ul>
        </li>
      </ul>
    </li>
  </ol>

  <h3>Output</h3>
  <ul>
    <li><strong>detections</strong>: Bounding boxes, class labels, and confidence scores for detected objects.</li>
    <li><strong>groups</strong>: Group IDs assigned to objects based on clustering.</li>
    <li><strong>visualization_path</strong>: Path to the visualized image with bounding boxes and group labels.</li>
  </ul>

  <hr>

  <h2>Folder Structure</h2>
  <pre>
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
  </pre>

  <hr>

  <h2>Steps to Run the Project</h2>

  <h3>1. Extract the ZIP File</h3>
  <p>Extract the project folder to your desired location.</p>

  <h3>2. Set Up a Virtual Environment</h3>
  <pre>
# Create a virtual environment
python -m venv venv

Activate the virtual environment
# Windows
.\venv\Scripts\activate
  </pre>

  <h3>3. Install Dependencies</h3>
  <p>Install the required libraries from <code>requirements.txt</code>:</p>
  <pre>
pip install -r requirements.txt
  </pre>

  <h3>4. Prepare Folders</h3>
  <p>Ensure the following folders exist:</p>
  <ul>
    <li><code>sample_images/</code>: For input images.</li>
    <li><code>static/visualizations/</code>: To save output visualizations.</li>
  </ul>

  <h3>5. Run the Flask Server</h3>
  <p>Start the application using:</p>
  <pre>
python app.py
  </pre>

  <h3>6. Access the Application</h3>
  <p>Open your browser and navigate to:</p>
  <pre>
http://127.0.0.1:5000/
  </pre>

  <h3>7. Upload Images and Process</h3>
  <ul>
    <li>Use the web interface to upload images and set thresholds for detection.</li>
    <li>Results (detections, groupings) are returned as JSON, and visualized images are saved in <code>static/visualizations/</code>.</li>
  </ul>

  <h3>8. Bulk Processing</h3>
  <p>To process all images in the <code>sample_images/</code> folder, navigate to:</p>
  <pre>
http://127.0.0.1:5000/process_bulk
  </pre>

  <h3>9. Stop the Server</h3>
  <p>To stop the Flask server:</p>
  <pre>
Ctrl + C
# Deactivate the virtual environment
deactivate
  </pre>

  <hr>

  <h2>Technologies Used</h2>
  <ul>
    <li><strong>Flask</strong>: Backend framework for API and user interactions.</li>
    <li><strong>Faster R-CNN</strong>: Pretrained model for object detection.</li>
    <li><strong>KMeans Clustering</strong>: Groups objects based on bounding box centers.</li>
    <li><strong>OpenCV</strong>: For visualization and image processing.</li>
  </ul>
</body>
</html>
