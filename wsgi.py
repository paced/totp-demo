"""Allow app to run when served by a web server."""
from manage import app as application

if __name__ == "__main__":
    application.run(debug=False, host='0.0.0.0')
