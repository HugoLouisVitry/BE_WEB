from App_financement.config import DEBUG, WEB_SERVER
from App_financement.views import app


if __name__ == '__main__':
    app.run(host=WEB_SERVER['host'],
            port=WEB_SERVER['port'],
            debug=DEBUG)
