from flask import Flask, request, render_template
from server.operators import add, subtract, multiply, divide

app = Flask(__name__,  template_folder='../client', static_folder='../client')

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """Permet de calculer une opération mathématique simple contenant un seul opérateur.

    Entrée:
        expr: Expression sous forme de texte, par exemple ``"4+5"``.

    Sortie:
        Résultat numérique de l'opération demandée.

    Raises:
        ValueError: Si l'expression est vide, mal formée ou contient des
            opérandes qui ne sont pas des nombres.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Traite la page principale de la calculatrice.

    Entrée:
        Requête HTTP GET ou POST contenant l'expression soumise dans le champ ``display``.

    Sortie:
        Page HTML rendue de la calculatrice avec le résultat de l'opération ou un message d'erreur.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)