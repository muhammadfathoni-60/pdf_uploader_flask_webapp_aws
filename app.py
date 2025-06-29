import os
from src import app

if __name__ == "__main__":
    try:
        app.secret_key = os.urandom(12)  # Generate a random secret key
        app.run(debug=True, host="0.0.0.0", port=9000)  # Run the Flask app
    except Exception as err:
        print(f"Terjadi kesalahan: {err}")
