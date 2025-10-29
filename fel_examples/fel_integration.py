# Modulo que brinda funciones de SOAP
import zeep
# Link del WS
wsdl = 'https://demoemision.thefactoryhka.com.pa/ws/obj/v1.0/Service.svc?singleWsdl'
# Establecemos el cliente como el WS
cliente = zeep.Client(wsdl=wsdl)
# Declaramos el diccionario que pasa los datos de la solicitud
datos = dict(
    tokenEmpresa="SOLICITAR",
    tokenPassword="SOLICITAR",
    # Se declara otro diccionario para almacenar los detalles del documento
    documento=dict(
        codigoSucursalEmisor="0000",
        tipoSucursal="1",
        # Se declara diccionario que almacena los datos de transacción
        datosTransaccion=dict({
            "tipoEmision": "01",
            "tipoDocumento": "01",
            "numeroDocumentoFiscal": "0000001",
            "puntoFacturacionFiscal": "001",
            "naturalezaOperacion": "01",
            "tipoOperacion": 1,
            "destinoOperacion": 1,
            "formatoCAFE": 1,
            "entregaCAFE": 1,
            "envioContenedor": 1,
            "procesoGeneracion": 1,
            "tipoVenta": 1,
            "fechaEmision": "2022-05-19T09:00:00-05:00",
            "cliente": {
                "tipoClienteFE": "02",
                "tipoContribuyente": 1,
                "numeroRUC": 89337412,
                "pais": "PA",
                "correoElectronico1": "",
                "razonSocial": "MIGUEL GÓMEZ"
            }
        }),
        # Se declara diccionario que almacena los ítems del documento
        listaItems=dict(
            item=[{
                "descripcion": "Esta es una prueba 1",
                "cantidad": "1.00",
                "precioUnitario": "20.00",
                "precioUnitarioDescuento": " ",
                "precioItem": "20.00",
                "valorTotal": "21.40",
                "codigoGTIN": "0",
                "cantGTINCom": "0.99",
                "codigoGTINInv": "0",
                "tasaITBMS": "01",
                "valorITBMS": "1.40",
                "cantGTINComInv": "1.00"
            }, {
                "descripcion": "Esta es una prueba 2",
                "cantidad": "1.00",
                "precioUnitario": "20.00",
                "precioUnitarioDescuento": " ",
                "precioItem": "20.00",
                "valorTotal": "21.40",
                "codigoGTIN": "0",
                "cantGTINCom": "0.99",
                "codigoGTINInv": "0",
                "tasaITBMS": "01",
                "valorITBMS": "1.40",
                "cantGTINComInv": "1.00"
            }]
        ),
        # Se declara diccionario que almacena el detalle de los totales del documento
        totalesSubTotales=dict({
            "totalPrecioNeto": "40.00",
            "totalITBMS": "2.80",
            "totalMontoGravado": "2.80",
            "totalDescuento": "",
            "totalAcarreoCobrado": "",
            "valorSeguroCobrado": "",
            "totalFactura": "42.80",
            "totalValorRecibido": "42.80",
            "vuelto": "0.00",
            "tiempoPago": "1",
            "nroItems": "2",
            "totalTodosItems": "42.80"},
            # Se declara un diccionario que contiene la lista de formas de pago
            listaFormaPago=dict(
                # Se declara una lista que almacena las formas de pago
                formaPago=[
                    {
                        "formaPagoFact": "02",
                        "descFormaPago": " ",
                        "valorCuotaPagada": "21.40"
                    },
                    {
                        "formaPagoFact": "02",
                        "descFormaPago": " ",
                        "valorCuotaPagada": "21.40"
                    }
                ]
        )
        )
    )
)
# Declaramos una variable que llama al cliente, el servicio a utilizar y el método de este servicio, pasando como parámetro el diccionario que almacena los datos de la solicitud. Se utiliza ** al pasar el parámetro ya que el mismo está compuesto de un formato llave - valor.
res = (cliente.service.Enviar(**datos))
# Se imprime la respuesta a la solicitud enviada al servicio
print(res)