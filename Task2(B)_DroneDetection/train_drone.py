from ultralytics import YOLO

def main():
    base_model = "yolov8n.pt"
    data_yaml = "data/drone_dataset.yaml"  # <-- update YOUR PATH

    model = YOLO(base_model)

    model.train(
        data=data_yaml,
        epochs=50,
        imgsz=640,
        batch=16,
        workers=8,
        name="drone_yolo_train",
        device=0  # GPU → 0 , CPU → "cpu"
    )

    print("Training complete. Check ./runs/detect/ folder.")

if __name__ == "__main__":
    main()
