
import json
import azure.functions as func
from drugs import drugs

def main(findByprescription: func.HttpRequest) -> func.HttpResponse:


    prescription = findByprescription.params.get('prescription')
    if not prescription:
        try:
            req_body = findByprescription.get_json()
        except ValueError:
            pass
        else:
            prescription = req_body.get('prescription')

    if prescription:
        values=['0','1']
        if prescription not in values:
            return func.HttpResponse(
                "Unprocessable Entity",
                status_code=422
            )
        else:
            drugsFound=[drug for drug in drugs if drug["prescription"]==int(prescription)]

            if len(drugsFound)>0:
                return func.HttpResponse(json.dumps(
                    {"farmacos":drugsFound}
                    ),
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
             "Se a ejecutado el HttpTrigger correctamente pase el valor del parametro prescripción en la consulta para obetener listado de farmacos.",
             status_code=200
        )
