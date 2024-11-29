from flask import Flask, request, jsonify, render_template
import os
from detection.detector import detect_objects
from grouping.grouper import group_products
from utils.visualization import visualize_detections

app = Flask(__name__)
UPLOAD_FOLDER = "sample_images/"
VISUALIZATION_FOLDER = "static/visualizations/"
os.makedirs(VISUALIZATION_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({"error": "No image file found"}), 400

    file = request.files['image']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Step 1: Detect objects
    detections = detect_objects(file_path)

    # Step 2: Group products
    groups = group_products(detections)

    # Step 3: Visualize detections
    vis_path = os.path.join(VISUALIZATION_FOLDER, f"vis_{file.filename}")
    visualize_detections(file_path, detections, groups, vis_path)

    # Return JSON response
    response = {
        "detections": detections,
        "groups": groups,
        "visualization_path": vis_path
    }
    return jsonify(response)

@app.route('/process_bulk', methods=['GET'])
def process_bulk():
    responses = []

    for filename in os.listdir(UPLOAD_FOLDER):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(UPLOAD_FOLDER, filename)

            # Step 1: Detect objects
            detections = detect_objects(file_path)

            # Step 2: Group products
            groups = group_products(detections)

            # Step 3: Visualize detections
            vis_path = os.path.join(VISUALIZATION_FOLDER, f"vis_{filename}")
            visualize_detections(file_path, detections, groups, vis_path)

            # Append response for this file
            responses.append({
                "filename": filename,
                "detections": detections,
                "groups": groups,
                "visualization_path": vis_path
            })

    return jsonify(responses)

if __name__ == '__main__':
    app.run(debug=True)
