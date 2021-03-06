from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import subprocess
from subprocess import PIPE,TimeoutExpired

from PlayLangClass import PlayLangClass

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_item(request: Request, code: str = None, lang: str = None, input: str = None):
    res = PlayLangClass(code=code, lang=lang, input=input).main()
    return templates.TemplateResponse("index.html", {"request": request, "out": res["out"], "err": res["err"], "code": code, "lang": lang, "input": input})