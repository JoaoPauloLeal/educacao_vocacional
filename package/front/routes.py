from fastapi import Request
from fastapi.responses import HTMLResponse
from package.front.app_define import start_define
import multiprocessing
import uvicorn


def start_web():
    try:
        app = start_routes()
        multiprocessing.freeze_support()
        uvicorn.run(app, host='127.0.0.1', port=8080, debug=True, log_level="info")
    except:
        print('ERRO AO STARTAR VERIFICADOR DE INCONSISTENCIA')


def start_routes():
    app, templates = start_define()

    @app.get("/", response_class=HTMLResponse)
    async def home(request: Request):
        return templates.TemplateResponse("main.html", {"request": request})

    @app.post("/", response_class=HTMLResponse)
    async def teste_vocacional(request: Request):
        return templates.TemplateResponse("resultado.html", {"request": request})

    @app.get("/painel_leads", response_class=HTMLResponse)
    async def home(request: Request):
        return templates.TemplateResponse("painel_leads.html", {"request": request})

    @app.get("/resumo_aluno", response_class=HTMLResponse)
    async def home(request: Request):
        return templates.TemplateResponse("resumo_aluno.html", {"request": request})

    return app
