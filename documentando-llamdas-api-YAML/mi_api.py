from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Ruta para mostrar el archivo api_doc.yaml
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/'
API_URL = '/services/spec'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Consultas a JSONPlaceholder API"
    }
)


app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route(API_URL)
def api_spec():
    return send_from_directory('.', 'api_doc.yaml')


if __name__ == '__main__':
    app.run(debug=True)


