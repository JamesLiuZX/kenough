from fastapi import FastAPI, File, UploadFile
import os
from process import video_to_photos, photos_to_video

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


# Downloads file for processing
@app.post("/upload_file")
async def get_file(file: UploadFile, model: str = None, language: str = None):
    video_path = f"video/{file.filename}"

    # Saves a local copy of the file to be used to split into individual photo frames
    with open(video_path, "wb") as buffer:
        buffer.write(file.file.read())

    # Split video into individual frames
    try:
        photo_path = video_to_photos(file_url=video_path)
    except Exception:
        return "Failure to split video please try again!"
    
    # Run generation model
    #TODO
    output_path = await generate_path()
    # return file_path


    # Stich photos back to create video
    try:
        result = video_to_photos(file_url=output_path)
    except Exception:
        return "Failure to stitch video please try again!"




    # Delete the file after accessing it
    # if os.path.exists(file_path):
    #     os.remove(file_path)

    return {"File Path to video": result}