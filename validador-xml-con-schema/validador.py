from lxml import etree
import argparse
import json
import xmltodict

def main():

    #parser
    parser = argparse.ArgumentParser(prog='Validador')
    parser.add_argument('--xml', required=True, help='Ruta al archivo XML a validar.')
    parser.add_argument('--xsd', required=True, help='Ruta al archivo XSD de validación.')
    parser.add_argument('--xpath', help='XPath para obtener el valor de un elemento específico.')
    parser.add_argument('--json', action='store_true', help='Transformar XML a JSON.')
    args = parser.parse_args()

    #validar el xml_doc con el schema .xsd
    xmlschema_doc = etree.parse(args.xsd)
    xmlschema = etree.XMLSchema(xmlschema_doc)
    xml_doc = etree.parse(args.xml)
    result = xmlschema.validate(xml_doc)

    if result:
        print('El XML es válido! :)')
    else:
        print('El XML no es válido... :(')

    #buscar con xpath un elementop y printearlo
    xpath_result = xml_doc.xpath(args.xpath)
    if xpath_result:
        print(f"Valor del elemento XPath '{args.xpath}': {xpath_result[0].text}")
    else:
        print(f"No se encontró ningún elemento XPath '{args.xpath}' en el documento XML.")

    #convertir a json
    json_data = {'carta': {}}
    if args.json == True:
        with open("carta.xml") as xml_file:
            contenido_xml = xmltodict.parse(xml_file.read())
            json_data = json.dumps(contenido_xml, indent=4)
        with open('carta.json', 'w') as json_file:
            json_file.write(json_data)

        print(f"Documento JSON generado con éxito")

if __name__=='__main__':
    main()
