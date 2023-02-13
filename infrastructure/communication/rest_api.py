from fastapi import FastAPI, UploadFile

from domain.services.video_service import VideoService

app = FastAPI()

video_service = VideoService()


@app.post("/video/upload")
async def upload_video(file: UploadFile):
    v_id = video_service.upload_video(file)
    return {"video_id": str(v_id)}


@app.get("/video/{video_id}")
async def get_video(video_id: str):
    v_id = video_service.get_video(video_id)
    return {"video_id": str(v_id)}
