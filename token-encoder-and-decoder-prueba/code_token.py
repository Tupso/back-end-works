import json
import uuid
import jwt
import argparse


def generate_token(payload_file, secret):

    # Leemos el payload.json
    with open(payload_file, 'r') as file:
        payload_data = json.load(file)

    # Generamos un ID unico y lo agregamos como JWT ID (jti)
    payload_data['jti'] = str(uuid.uuid4())

    # Codificación del token con el algoritmo HS256
    encoded_token = jwt.encode(payload_data, secret, algorithm='HS256')

    # Pintamos en pantalla el token
    print('Su token es el siguiente:', encoded_token)


def main():
    parser = argparse.ArgumentParser(description="Generar tokens JWT")
    parser.add_argument("--payload", required=True, help="Ruta al archivo payload.json")
    parser.add_argument("--secret", required=True, help="Secreto para firmar el token")

    args = parser.parse_args()

    generate_token(args.payload, args.secret)


if __name__ == '__main__':
    main()


