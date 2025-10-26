from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
# 🔴 1. ¡CÁMBIALA! Clave secreta para manejar las sesiones
# Debe ser una cadena de texto larga y única.
app.secret_key = 'una_clave_secreta_para_tu_proyecto_personal_9876' 

# 🔴 2. ¡CÁMBIALA! La contraseña que tu novia debe usar.
CONTRASENA_SECRETA = "nuestroaniversario" 

@app.route('/')
def index():
    # Si la sesión ya está activa (ya ingresó la clave), va directo al cofre
    if session.get('logged_in'):
        return redirect(url_for('cofre'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user_input = request.form['password']
    
    # Comprueba la contraseña (ignorando mayúsculas/minúsculas y espacios extra)
    if user_input.lower().strip() == CONTRASENA_SECRETA.lower().strip():
        session['logged_in'] = True
        return redirect(url_for('cofre'))
    else:
        # Muestra el mensaje de error en la página de login
        return render_template('login.html', error="¡Clave incorrecta! Sólo el amor tiene la llave correcta. 😉")

@app.route('/cofre')
def cofre():
    # Protección: si no hay sesión activa, redirige al login
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    
    return render_template('cartas.html')

@app.route('/logout')
def logout():
    # Cierra la sesión
    session.pop('logged_in', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Inicia el servidor web en tu computadora
    app.run(debug=True)