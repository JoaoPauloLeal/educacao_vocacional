import jinja2
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from os import path, listdir


def start_define():
    app = FastAPI()
    jinja2.FileSystemLoader([path.join(path.dirname(__file__), 'view/templates')])
    app.mount("/static", StaticFiles(directory=path.join(path.dirname(__file__), 'view/static')), name="static")
    templates = Jinja2Templates(directory=path.join(path.dirname(__file__), 'view/templates'))

    return app, templates
