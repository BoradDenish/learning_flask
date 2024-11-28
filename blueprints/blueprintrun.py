import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from blueprints.blueprintapp import create_app, db

flask_app = create_app()

with flask_app.app_context():
    db.create_all()

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=5000, debug=True)
