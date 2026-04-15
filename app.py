from flask import Flask, render_template, request

app = Flask(__name__)

def aritmetica(op, a, b):
    if op == "suma": return a + b
    if op == "resta": return a - b
    if op == "multiplica": return a * b
    if op == "divide": return a / b

def binaria(op, a, b):
    if op == "AND": return a & b
    if op == "OR": return a | b
    if op == "XOR": return a ^ b

def logica(op, a, b):
    if op == "AND": return a and b
    if op == "OR": return a or b
    if op == "NOT": return not a

@app.route("/", methods=["GET","POST"])
def index():
    result = None
    if request.method == "POST":
        tipo = request.form["tipo"]
        op = request.form["operacion"]
        a = int(request.form["a"])
        b = int(request.form["b"]) if "b" in request.form else 0
        if tipo == "aritmetica":
            result = aritmetica(op, a, b)
        elif tipo == "binaria":
            result = binaria(op, a, b)
        elif tipo == "logica":
            result = logica(op, bool(a), bool(b))
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
