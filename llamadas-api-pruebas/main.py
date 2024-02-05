
import argparse
from api_calls import perform_api_call
import json



def main():
    parser = argparse.ArgumentParser(description="Peticiones a la API")
    parser.add_argument("--method", required=True, choices=["GET", "POST", "PUT", "DELETE"], help="Método que se usará para llamar al API")
    parser.add_argument("--resource", required=True, choices=["posts", "comments"], help="Recurso sobre el que se realiza la operación")
    parser.add_argument("--resource_id", help=" Identificador único del recurso")

    args = parser.parse_args()
    perform_api_call(args.method, args.resource, args.resource_id)

    # Leemos el archivo data.json resultante de la peticion a la API
    with open("./response/data.json", "r") as file:
        mydata = json.load(file)

    # Escribimos el archivo comments.json o posts.json en el caso de que la petición realizada haya sido una de las
    # indicadas
    if args.resource == 'comments':
        with open("comments.json", "w") as file:
            json.dump(mydata, file, indent=4)

    elif args.resource == 'posts':
        with open("posts.json", "w") as file:
            json.dump(mydata, file, indent=4)


if __name__ == '__main__':
    main()

