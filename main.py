from PIL import Image
import io
import extcolors

from fastapi import FastAPI, File, UploadFile

app = FastAPI(
        title="ColApi",
        description="This is a tiny application on demand for specific use by deventhusiast",
        version="0.0.1",
)


@app.post("/getcolors/")
async def get_colors_from_image(file: UploadFile):
    request_object_content = await file.read()
    img = Image.open(io.BytesIO(request_object_content))
    colors, pixel_count = extcolors.extract_from_image(img)
    rgb_colors = [ f"rgb({a[0][0]},{a[0][1]},{a[0][2]})" for a in colors]
    return {"colors":rgb_colors}
