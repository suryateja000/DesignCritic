import numpy as np
from io import BytesIO
from typing import List
from PIL import Image
from sklearn.cluster import KMeans

def extract_palette(image_bytes:bytes,k:int=5,sample:int=5000)->List[str]:

    img=Image.open(BytesIO(image_bytes)).convert("RGB")
    arr=np.array(img)
    px=arr.reshape(-1,3)

    if len(px)>sample:
        idx=np.random.choice(len(px),sample,replace=False)
        px=px[idx]


    km=KMeans(n_clusters=k,random_state=42,n_init='auto')
    km.fit(px)
    
    ctr=km.cluster_centers_.astype(int)
    return [f"#{r:02x}{g:02x}{b:02x}" for r,g,b in ctr]