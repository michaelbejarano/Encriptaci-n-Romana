from flask import Flask, render_template, request

app = Flask(__name__)


def cifrar_cesar(texto, desplazamiento):
    resultado = ""

    for letra in texto:
        if letra.isalpha():
            if letra.isupper():
                nueva = chr((ord(letra) - 65 + desplazamiento) % 26 + 65)
            else:
                nueva = chr((ord(letra) - 97 + desplazamiento) % 26 + 97)
            resultado += nueva
        else:
            resultado += letra

    return resultado


def fuerza_bruta_cesar(texto):
    resultados = []

    for i in range(1, 26):
        intento = cifrar_cesar(texto, -i)
        resultados.append({
            "giro": i,
            "texto": intento
        })

    return resultados


@app.route("/", methods=["GET", "POST"])
def index():
    texto = ""
    giro = ""
    texto_cifrado = ""
    resultados_fuerza_bruta = []

    if request.method == "POST":
        accion = request.form.get("accion")
        texto = request.form.get("texto", "")
        giro = request.form.get("giro", "").strip()

        if accion == "cifrar" and giro:
            texto_cifrado = cifrar_cesar(texto, int(giro))

        elif accion == "fuerza_bruta":
            resultados_fuerza_bruta = fuerza_bruta_cesar(texto)

    return render_template(
        "index.html",
        texto=texto,
        giro=giro,
        texto_cifrado=texto_cifrado,
        resultados_fuerza_bruta=resultados_fuerza_bruta
    )


if __name__ == "__main__":
    app.run(debug=True)