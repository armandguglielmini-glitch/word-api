from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse
from docx import Document
from docxtpl import DocxTemplate
import tempfile

app = FastAPI()

@app.post("/fill-template")
async def fill_template(file: UploadFile, data: str = Form(...)):
    """
    - file : modèle Word (.docx) avec {{variables}}
    - data : JSON envoyé par Retool (clé/valeurs à injecter dans le docx)
    """

    # Charger le modèle Word
    doc = DocxTemplate(file.file)

    # Parser le JSON reçu depuis Retool
    context = json.loads(data)

    # Rendre le template avec les données
    doc.render(context)

    # Sauvegarder le doc modifié dans un fichier temporaire
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
    doc.save(tmp.name)

    return FileResponse(tmp.name, filename="modified.docx")
