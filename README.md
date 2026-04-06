# Encriptación Romana (Cifrado César)
Este proyecto es una aplicación web desarrollada en Python con Flask que permite cifrar textos utilizando el método de encriptación romana, conocido como **Cifrado César**, uno de los métodos de criptografía más antiguos de la historia.

## ¿Qué es la encriptación romana?

El cifrado César fue utilizado por Julio César para enviar mensajes secretos a su ejército.
Consiste en **desplazar las letras del alfabeto** un número determinado de posiciones.

Ejemplo con desplazamiento de 3:
* A → D
* B → E
* C → F

Entonces:
**"HOLA" → "KROD"**

## ¿Cómo funciona?

Imagina que escribes un mensaje, pero cada letra se mueve en el alfabeto.

* Se elige un número (giro)
* Cada letra se reemplaza por otra según ese número
* El resultado es un texto cifrado que no se entiende a simple vista

Además, este proyecto incluye **fuerza bruta**, que prueba todos los posibles desplazamientos para encontrar el mensaje original.


## 🚀 Funcionalidades

* 🔑 Cifrado de texto con desplazamiento personalizado
* 🔓 Descifrado automático mediante fuerza bruta
* 🌐 Interfaz web interactiva


## 🛠️ Tecnologías utilizadas

* Python
* Flask
* HTML

## ⚙️ Instalación y ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/michaelbejarano/Encriptaci-n-Romana.git
```
2. Entrar a la carpeta:

```bash
cd Encriptaci-n-Romana
```

3. Instalar Flask:

```bash
pip install flask
```

4. Ejecutar la aplicación:

```bash
python app.py
```

5. Abrir en el navegador:

```
http://127.0.0.1:5000/
```

---

##  Interfaz del sistema

Aquí puedes ver cómo funciona la aplicación:

<img width="1254" height="793" alt="image" src="https://github.com/user-attachments/assets/64d35c36-4aa2-491f-b90e-ffaef2e18464" />
<img width="1215" height="756" alt="image" src="https://github.com/user-attachments/assets/fe9a3dc7-335a-4a36-a650-e7b73aa95334" />

---

##  Autor

* Michael Bejarano
