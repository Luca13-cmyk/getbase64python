
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import base64
from mimetypes import MimeTypes

try:
    pathfile = str(input("Digite o caminho do arquivo: "))
except:
    print("Ex: /home/user/Desktop/img.jpeg")
else:
    with open(pathfile, "rb") as Image:
        mime = MimeTypes()
        mime_type = mime.guess_type(pathfile)
        base64definer = base64.b64encode(Image.read())
        base64definer = str(base64definer)
        base64definer = base64definer.replace("'", "")
        base64definer = base64definer.replace("b/9j", "/9j")
        print(f"data:{mime_type[0]};base64,{base64definer}")
