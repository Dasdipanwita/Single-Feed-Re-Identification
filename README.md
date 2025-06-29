# Re-Identification in a Single Feed - Player Tracking

## 📌 Objective
Detect and track players in a 15-second video using a YOLOv11 model with consistent IDs, even when they re-enter the frame.

## ▶️ How to Run

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Place the following files in the same folder:
    - `best.pt` (model)
    - `15sec_input_720p.mp4` (video)

3. Run the script:
    ```bash
    python index.py
    

4. Output video:
    - `output_tracked.mp4` will be saved with tracked players and ID overlays.

## 🧪 Dependencies
- Python 3.8+
- OpenCV
- Ultralytics
- DeepSort-Realtime

Use this to install:
```bash
pip install opencv-python ultralytics deep-sort-realtime
