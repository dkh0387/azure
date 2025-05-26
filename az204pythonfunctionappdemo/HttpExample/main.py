import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hallo, {name}!")
    else:
        return func.HttpResponse(
            "Bitte gib einen Namen per Query oder JSON mit.",
            status_code=400
        )
