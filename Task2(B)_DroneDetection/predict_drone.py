from ultralytics import YOLO
from PIL import Image
import io

_MODEL = None

def load_model(model_path="yolov8n.pt"):
    global _MODEL
    if _MODEL is None:
        _MODEL = YOLO(model_path)
    return _MODEL

def predict_from_bytes(image_bytes, model_path="yolov8n.pt", conf=0.25, iou=0.45):
    model = load_model(model_path)

    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    width, height = image.size

    results = model.predict(
        source=image,
        imgsz=640,
        conf=conf,
        iou=iou,
        verbose=False
    )

    detections = []
    res = results[0]

    if hasattr(res, "boxes") and len(res.boxes) > 0:
        boxes = res.boxes.xyxy.cpu().numpy()
        scores = res.boxes.conf.cpu().numpy()

        class_ids = (
            res.boxes.cls.cpu().numpy().astype(int)
            if hasattr(res.boxes, "cls")
            else [0] * len(scores)
        )

        for box, score, cid in zip(boxes, scores, class_ids):
            x1, y1, x2, y2 = map(float, box)
            detections.append({
                "bbox": [x1, y1, x2, y2],
                "confidence": float(score),
                "class_id": int(cid)
            })

    return {
        "count": len(detections),
        "detections": detections,
        "image_size": [width, height]
    }
