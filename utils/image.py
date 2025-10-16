from io import BytesIO
from PIL import Image
import base64

def ensure_png_bytes(img_bytes:bytes)->bytes:

    im=Image.open(BytesIO(img_bytes)).convert("RGBA")
    buf=BytesIO()

    im.save(buf,format="PNG")
    return buf.getvalue()

def png_bytes_to_data_url(png_bytes:bytes)->str:
    
    b64=base64.b64encode(png_bytes).decode("utf-8")
    return f"data:image/png;base64,{b64}"