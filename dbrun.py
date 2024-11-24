from dbapp import create_app

# Create the Flask app
flask_app = create_app()

# Run the app
if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=5000, debug=True)
