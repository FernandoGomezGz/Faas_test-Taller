

import azure.functions as func
from drugs import drugs
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    ver=req.params.get('id')
    np = {
        "id":int(req.params.get('id')),
        "stock":int(req.params.get('stock')),
        "imageUrl":req.params.get('imageUrl'),
        "name":req.params.get('name'),
        "price":float(req.params.get('price')),
        "prescription":int(req.params.get('prescription'))
    }
    
    if not ver:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            ver = req_body.get('id')

    if ver:
        idf = False
        for i in drugs:
            if i["id"] == np["id"]:
                idf = True
        if idf == False and np["id"] != None:
            drugs.append(np)
            return func.HttpResponse(json.dumps(
                {"Farmaco agregado correctamente:": drugs}),
                mimetype="application/json",
                status_code=200
            )
        else:
            return func.HttpResponse(
                    "La id del producto ya existe",
                    status_code=404
                )
    else:
        return func.HttpResponse(
             "Pase los parametros para agregar un nuevo producto.",
             status_code=200
        )
