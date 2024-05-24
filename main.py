from fastapi import FastAPI, Query, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import cv2
import imutils
import numpy as np
import requests

def count_people(image):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    image = imutils.resize(image, width=min(800, image.shape[1]))

    (regions, _) = hog.detectMultiScale(image,
                                        winStride=(4, 4),
                                        padding=(4, 4),
                                        scale=1.05)

    count_ppl = 0
    for (x, y, w, h) in regions:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        count_ppl += 1
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

    return count_ppl

def read_image_from_url(url):
    response = requests.get(url)
    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    return image

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get-image")
def get_image():
    image_path = "zdjecie.jpg"
    image = cv2.imread(image_path)
    people = count_people(image)
    return {"number": people}

@app.get("/get-image-from-url")
def get_image_from_url(url: str = Query(...)):
    image = read_image_from_url(url)
    if image is None:
        return JSONResponse(status_code=400, content={"message": "Could not read the image from the URL"})
    people = count_people(image)
    return {"number": people}

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        np_img = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
        people = count_people(image)
        return {"number": people}
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
