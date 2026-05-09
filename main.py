# Flask library import kar rahe hain
from flask import Flask, request

# random secret key banane ke liye
import secrets

# email validate karne ke liye regex
import re

# Flask app create kar rahe hain
app = Flask(__name__)

# email check function
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# route banaya /generate
@app.route('/generate')

def generate_key():
    # URL se email lena
    email = request.args.get('email')

    # agar email nahi diya
    if not email:
        return "Please provide email like /generate?email=test@gmail.com"

    # agar email invalid ho
    if not is_valid_email(email):
        return "Invalid Email"

    # secret key generate
    secret_key = secrets.token_hex(16)

    # response return
    return f"Email: {email}<br>Secret Key: {secret_key}"


# app run karna
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
