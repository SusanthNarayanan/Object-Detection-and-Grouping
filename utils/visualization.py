import cv2
import numpy as np

def visualize_detections(image_path, detections, groups, save_path):
    # Read the input image
    image = cv2.imread(image_path)

    # Iterate over detections
    for det in detections:
        bbox = det["bbox"]
        group_id = det["group_id"]
        score = det["score"]
        label = det["label"]

        # Generate a random color based on group_id
        np.random.seed(group_id)
        color = tuple(np.random.randint(0, 255, 3).tolist())

        # Draw the bounding box
        cv2.rectangle(
            image, 
            (int(bbox[0]), int(bbox[1])), 
            (int(bbox[2]), int(bbox[3])), 
            color, 
            2
        )

        # Put the label and group ID
        text = f"Group: {group_id}, Label: {label}, Score: {score:.2f}"
        cv2.putText(
            image, 
            text, 
            (int(bbox[0]), int(bbox[1]) - 10), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.5, 
            color, 
            2
        )

    # Save the visualized image
    cv2.imwrite(save_path, image)
