import os
from src import app

if __name__ == "__main__":
    try:
        app.secret_key = os.urandom(12)
        app.run(debug=True, host="0.0.0.0", port=9000)
    except Exception as e:
        print(f"Error: {e}")

    except Exception as e:
        print(e)