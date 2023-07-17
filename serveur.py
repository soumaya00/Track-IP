!/usr/bin/env python3
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def get_ip():
    with open("adresse_ip.txt", "a") as file:
        file.write(request.remote_addr+"\n")
    return redirect("https://www.google.com", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)