import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load YOLOv11 model
model = YOLO("best.pt")

# Initialize DeepSORT tracker
tracker = DeepSort(max_age=15, n_init=2)

# Load input video
video_path = "15sec_input_720p.mp4"
cap = cv2.VideoCapture(video_path)

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define output video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'XVID' or 'avc1' if needed
out = cv2.VideoWriter("output_tracked.mp4", fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    detections = []

    for result in results.boxes.data:
        x1, y1, x2, y2, conf, cls = result.cpu().numpy()
        if int(cls) == 0:  # Class 0 = player
            detections.append(([x1, y1, x2 - x1, y2 - y1], conf, 'player'))

    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        l, t, r, b = track.to_ltrb()

        cv2.rectangle(frame, (int(l), int(t)), (int(r), int(b)), (0, 255, 0), 2)
        cv2.putText(frame, f"ID {track_id}", (int(l), int(t)-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Show frame (optional)
    cv2.imshow("Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Write the frame to the output video
    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()
