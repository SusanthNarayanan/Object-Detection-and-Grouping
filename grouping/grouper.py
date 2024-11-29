from sklearn.cluster import KMeans
import numpy as np

def group_products(detections):

    # Extract bounding box centers
    centers = [
        [(bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2]
        for det in detections for bbox in [det['bbox']]
    ]
    centers = np.array(centers)

    # Check if the number of samples is less than the number of clusters
    n_samples = len(centers)
    n_clusters = min(3, n_samples)  # Ensure n_clusters is at most n_samples

    if n_samples < 2:
        # If only one or no samples, assign all detections to a single group
        for det in detections:
            det["group_id"] = 0
        return [0] * n_samples

    # Group using KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(centers)
    groups = kmeans.labels_.tolist()

    # Assign group IDs to detections
    for i, det in enumerate(detections):
        det["group_id"] = groups[i]

    return groups
