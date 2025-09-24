from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse
from docx import Document
import tempfile

app = FastAPI()

@app.post("/modify-docx")
async def modify_docx(
    file: UploadFile,
    old_text: str = Form(...),
    new_text: str = Form(...)
):
    # Charger le Word
    doc = Document(file.file)

    # Remplacer dans tous les paragraphes
    for p in doc.paragraphs:
        if old_text in p.text:
            p.text = p.text.replace(old_text, new_text)

    # Sauvegarder dans un fichier temporaire
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
    doc.save(tmp.name)

    return FileResponse(tmp.name, filename="modified.docx")
