from fastapi import UploadFile, File, APIRouter

from models.ml import up_img

router = APIRouter(
    prefix="/extract",
    tags=["Upload Image"]
)

@router.post("/")
async def extract(file: UploadFile = File(...)):
    contents = await file.read()
    return up_img(contents=contents)