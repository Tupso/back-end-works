import jwt
import argparse


def decode_token(token, secret, field=None):
    try:
        # Decodificamos el token
        decoded_token = jwt.decode(token, secret, algorithms=["HS256"])

        if field:
             # Pintamos el valor del campo solicitado o se informa de su ausencia
            if field in decoded_token:
                print(decoded_token[field])
            else:
                print("Campo no encontrado")
        else:
            # Imprimir el contenido del token
            print(decoded_token)

    except jwt.InvalidTokenError:
        print("La firma debe ser incorrecta")


def main():
    parser = argparse.ArgumentParser(description="Decodificar tokens JWT")
    parser.add_argument("--token", required=True, help="Token a decodificar")
    parser.add_argument("--secret", required=True, help="Secreto de la firma del token")
    parser.add_argument("--field", help="Nombre de un campo dentro del cuerpo del token JWT")

    args = parser.parse_args()

    decode_token(args.token, args.secret, args.field)


if __name__ == '__main__':
    main()