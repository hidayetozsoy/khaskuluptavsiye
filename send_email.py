from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Flask-Mail configuration for Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'khaskuluptavsiye@gmail.com'  # Replace with your Gmail address
app.config['MAIL_PASSWORD'] = 'zxqv nksu wolp uawz'      # Replace with your Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = 'khaskuluptavsiye@gmail.com'  # Replace with your Gmail address

# Initialize Flask-Mail
mail = Mail(app)

@app.route('/send-email')
def send_email():
    try:
        # Create email message
        msg = Message(
            subject='Test Email from Flask',
            recipients=['recipient@example.com'],  # Replace with recipient's email
            body='This is a test email sent from a Flask application using Gmail.'
        )
        
        # Send the email
        mail.send(msg)
        return 'Email sent successfully!'
    except Exception as e:
        return f'Error sending email: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)