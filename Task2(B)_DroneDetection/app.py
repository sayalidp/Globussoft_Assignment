from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from predict_drone import predict_from_bytes
import uvicorn

app = FastAPI(title="Drone Count Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/detect")
async def detect(
    file: UploadFile = File(...),
    conf: float = 0.25,
    iou: float = 0.45,
    model_path: str = "yolov8n.pt"
):
    """Detect drones in an uploaded image."""
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    image_bytes = await file.read()
    try:
        result = predict_from_bytes(
            image_bytes,
            model_path=model_path,
            conf=conf,
            iou=iou
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Detection failed: {e}")

    return result


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
