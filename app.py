from flask import Flask, request, render_template_string
import math

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>BCS601 Cloud Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 400px;
            margin: 50px auto;
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        h2 {
            text-align: center;
            color: #333;
        }

        label {
            font-weight: bold;
        }

        input {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            margin-bottom: 15px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        button {
            width: 100%;
            padding: 10px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background: #0056b3;
        }

        .result {
            margin-top: 20px;
            background: #eef3ff;
            padding: 15px;
            border-radius: 8px;
        }

        ul {
            padding-left: 20px;
        }

        li {
            margin-bottom: 5px;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>BCS601 Project</h2>
    <p style="text-align:center;">Nayana K (4MW23CS080)</p>

    <form method="post">
        <label>Enter Number 1:</label>
        <input type="number" name="num1" required>

        <label>Enter Number 2:</label>
        <input type="number" name="num2" required>

        <label>Enter a String:</label>
        <input type="text" name="text" required>

        <button type="submit">Submit</button>
    </form>

    {% if result %}
    <div class="result">
        <h3>Results</h3>
        <p><b>HCF:</b> {{ result.hcf }}</p>
        <p><b>LCM:</b> {{ result.lcm }}</p>
        <p><b>Reversed String:</b> {{ result.rev }}</p>

        <h4>Factorials (4–8)</h4>
        <ul>
        {% for num, fact in result.fact %}
            <li>{{ num }}! = {{ fact }}</li>
        {% endfor %}
        </ul>
    </div>
    {% endif %}
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        text = request.form["text"]

        hcf = math.gcd(num1, num2)
        lcm = (num1 * num2) // hcf
        reversed_text = text[::-1]
        factorials = [(i, math.factorial(i)) for i in range(4, 9)]

        result = {
            "hcf": hcf,
            "lcm": lcm,
            "rev": reversed_text,
            "fact": factorials
        }

    return render_template_string(html_code, result=result)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)