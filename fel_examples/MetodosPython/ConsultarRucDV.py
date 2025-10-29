# Modulo que brinda funciones de SOAP
import zeep
# Link del WS
wsdl = 'https://demoemision.thefactoryhka.com.pa/ws/obj/v1.0/Service.svc?singleWsdl'
# Establecemos el cliente como el WS
cliente = zeep.Client(wsdl=wsdl)
# Declaramos el diccionario que pasa los datos de factura
datos = {
    "consultarRucDVRequest": {
        "tokenEmpresa": "SOLICITAR",
        "tokenPassword": "SOLICITAR",
        "tipoRuc": "1 - natural, 2 - juridico",
        "ruc": "RUC",
    }
}
# Declaramos el metodo a usar, recorremos el diccionario y lo enviamos
res = (cliente.service.ConsultarRucDV(**datos))
# Se imprime la respuesta a la solicitud del servicio
print(res)
