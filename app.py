from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.secret_key = 'teste'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.getenv("EMAIL"),
    "MAIL_PASSWORD": os.getenv("SENHA"),
}

app.config.update(mail_settings)
mail = Mail(app)

class   Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )

        msg = Message(
            subject = f'{formContato.nome} te enviou uma mensagem no Portfolio',
            sender = app.config.get("MAIL_USERNAME"),
            recipients= ['natacomercial11@gmail.com'],
            body = f'''
                {formContato.nome} usando o Email {formContato.email}, te enviou a mensagem:

                {formContato.mensagem}'''
        )
        mail.send(msg)
        flash('Message sucessfuly send')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

