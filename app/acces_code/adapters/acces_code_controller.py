from flask import Blueprint
from ..services.decode_keys import DecodeKeys

acces_blue_print = Blueprint("keys",__name__)
@acces_blue_print.route("/acces_code", methods=["GET"], endpoint="acces_code")
def main():
    response  ='El codigo de acceso es: {0}'
    decode_keys = DecodeKeys()
    acces_code = "".join(decode_keys.search_code())
    return response.format(acces_code)
