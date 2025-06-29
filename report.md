
---

### 📄 report.md / report.pdf (Brief Report)

**Required Points to Cover:**

```markdown
# Re-Identification Assignment – Report

## 1. Approach & Methodology

- Used the provided `best.pt` YOLOv11 model to detect players per frame.
- Used DeepSORT tracker to assign and maintain unique IDs across frames.
- Filtered only class `0` (players) for tracking.

## 2. Techniques & Outcomes

- Applied `max_age=15` and `n_init=2` in DeepSORT to ensure re-ID when players re-entered after short occlusion.
- Real-time simulation achieved using OpenCV’s `imshow` and frame-wise processing.
- Output saved as a video with bounding boxes and ID labels.

## 3. Challenges Encountered

- Minor ID switches on fast movement or partial occlusion (minimized by tuning `max_age`).
- Model occasionally detected ball or misclassified objects (ignored non-player classes).

## 4. Incomplete or Further Improvements

- Currently tracks only players (not ball).
- Could improve with stronger appearance embeddings or hybrid model (e.g., ByteTrack).
- Optionally include per-ID analytics (appearance duration, re-entry count).
