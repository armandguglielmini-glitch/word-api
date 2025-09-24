from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse
from docx import Document
from docxtpl import DocxTemplate
import tempfile

app = FastAPI()

@app.post("/modify-docx")
async def modify_docx(
    file: UploadFile,
    old_text: str = Form(...),
    new_text: str = Form(...)
):

    # Charger le template
    doc = DocxTemplate("templates/mon_modele.docx")
    
    # Données à injecter
    context = {
        "NOM": "Dupont",
        "MONTANT": "150 000 €",
        "DATE": "24/09/2025"
    }
    
    # Injecter les données dans le document
    doc.render(context)
    
    # Sauvegarder le document final
    doc.save("outputs/document_final.docx")

    return FileResponse(tmp.name, filename="modified.docx")
