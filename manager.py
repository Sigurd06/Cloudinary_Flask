from os import getenv
from app import create_app

app = create_app(getenv('SETTINGS_NAME') or 'default')

if __name__ == '__main__':
    app.run(debug=True)