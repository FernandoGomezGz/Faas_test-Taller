

import json
import azure.functions as func
from drugs import drugs


def main(delete: func.HttpRequest) -> func.HttpResponse:

    product = delete.params.get('id')
    
    if not product:
        try:
            req_body = delete.get_json()
        except ValueError:
            pass
        else:
            product = req_body.get('id')

    if product:
        drugFound = [drug for drug in drugs if drug['id'] == int(product)]
        if len(drugFound) > 0:
            for index, drug in enumerate(drugs):
                if (drug["id"] == int(product)):
                    drugs.pop(index)
                    return func.HttpResponse(
                            "Se ha eliminado el producto correctamente",
                            mimetype="application/json",
                            status_code=200
                    )
        else:
                return func.HttpResponse(
                    "Not found.",
                    status_code=404
                )
    else:
        return func.HttpResponse(
             "Ingrese los parametros para eliminar un producto.",
             status_code=200
        )
