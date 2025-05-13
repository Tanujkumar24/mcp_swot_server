import subprocess
import requests
import time
import sys
import os
import io

# Force stdout and stderr to use UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def wait_for_server(url, timeout=15):
    """Wait for the Flask server to be ready."""
    for _ in range(timeout):
        try:
            requests.get(url)
            return True
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    return False

def test_api_endpoint():
    # Start the Flask app in a subprocess
    flask_process = subprocess.Popen(
        [sys.executable, "app.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    try:
        # Wait for server to start
        print("Waiting for server to start...")
        if not wait_for_server("http://127.0.0.1:5000"):
            print("Server did not start in time.")
            return

        print("Server started. Sending request...")
        url = "http://127.0.0.1:5000/analyze"
        payload = {"product_name": "noise headphones"}
        response = requests.post(url, json=payload)
        print("Status Code:", response.status_code)
        print("Response:", response.json())

    finally:
        print("Terminating server...")
        flask_process.terminate()
        flask_process.wait()

if __name__ == "__main__":
    test_api_endpoint()
