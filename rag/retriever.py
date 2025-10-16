import os,re,glob

ALL_ENTRIES=[]

def parse_rd_file(filepath:str):

    with open(filepath,"r",encoding="utf-8") as f:
        content=f.read()
    content=content.replace("\r\n","\n").replace("\r","\n").lstrip("\ufeff")
    blocks=re.split(r'(?m)^\s*##\s+ENTRY_\d+\s*$',content)[1:]
    entries=[]

    for block in blocks:
        lines=[ln.strip() for ln in block.strip().split("\n") if ln.strip()]
        entry={"source_url":"","section":"","system":"","topic":"","tags":[],"content":""}
        content_lines=[]
        for line in lines:

            if line.startswith("SOURCE_URL:"):
                entry["source_url"]=line.split("SOURCE_URL:",1)[1].strip()
                
            elif line.startswith("SECTION:"):
                entry["section"]=line.split("SECTION:",1)[1].strip()

            elif line.startswith("SYSTEM:"):
                entry["system"]=line.split("SYSTEM:",1)[1].strip()

            elif line.startswith("TOPIC:"):
                entry["topic"]=line.split("TOPIC:",1)[1].strip()

            elif line.startswith("RETRIEVAL_TAGS:"):
                raw=line.split("RETRIEVAL_TAGS:",1)[1].strip()
                entry["tags"]=[t.strip() for t in raw.split(",") if t.strip()]

            else:
                content_lines.append(line)

        entry["content"]="\n".join(content_lines).strip()
        if entry["content"]:
            entries.append(entry)


    return entries

def load_all(docs_dir:str):
    global ALL_ENTRIES
    ALL_ENTRIES=[]
    paths=glob.glob(os.path.join(docs_dir,"*.rd"))+glob.glob(os.path.join(docs_dir,"*.md"))
    for p in paths:
        ALL_ENTRIES.extend(parse_rd_file(p))

def retrieve(query:str,k:int=8):
    if not ALL_ENTRIES:
        return []
    q=query.lower()
    words=[w for w in re.findall(r"[a-z0-9#+\-]+",q) if len(w)>1]
    scored=[]
    for e in ALL_ENTRIES:

        blob=" ".join([e.get("system",""),e.get("section",""),e.get("topic","")," ".join(e.get("tags",[])),e.get("content","")]).lower()
        score=0
        if e.get("system","").lower() in q:score+=5
        if e.get("topic","").lower() in q:score+=3

        for t in e.get("tags",[]):
            if t in q:score+=3
        for w in words:
            if w in blob:score+=1
        scored.append((score,e))

    scored.sort(key=lambda x:x[0],reverse=True)

    hits=[e for s,e in scored[:k] if s>0]
    
    if not hits:
        hits=[e for _,e in scored[:k]]
    return hits