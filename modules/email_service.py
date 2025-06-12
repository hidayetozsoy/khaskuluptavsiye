from flask_mail import Mail, Message
from flask import current_app
from .email_config import (
    MAIL_SERVER,
    MAIL_PORT,
    MAIL_USE_TLS,
    MAIL_USERNAME,
    MAIL_PASSWORD,
    MAIL_DEFAULT_SENDER
)

class EmailService:
    def __init__(self, app):
        """
        Initialize email service with Flask app
        
        Args:
            app: Flask application instance
        """
        # Configure Flask-Mail
        app.config['MAIL_SERVER'] = MAIL_SERVER
        app.config['MAIL_PORT'] = MAIL_PORT
        app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
        app.config['MAIL_USERNAME'] = MAIL_USERNAME
        app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
        app.config['MAIL_DEFAULT_SENDER'] = MAIL_DEFAULT_SENDER
        
        # Initialize Flask-Mail
        self.mail = Mail()
        self.mail.init_app(app)

    def send_club_application(self, email, club, isim, soyisim):
        """
        Send club application confirmation email
        
        Args:
            email (str): Recipient's email address
            club (str): Club name
            isim (str): Student's first name
            soyisim (str): Student's last name
            
        Returns:
            tuple: (success: bool, message: str)
        """
        try:
            msg = Message(
                subject=f"{club}'müze Hoş Geldiniz",
                recipients=[email],
                body=f"""
Sayın {isim} {soyisim},

{club}'müze hoş geldiniz! Başvurunuz alınmıştır.

En kısa sürede sizinle iletişime geçeceğiz.

Saygılarımızla,
{club}
"""
            )
            self.mail.send(msg)
            return True, 'Başvurunuz başarıyla alındı!'
        except Exception as e:
            return False, f'Başvuru gönderilirken bir hata oluştu: {str(e)}'

    def send_club_suggestion(self, club_name):
        """
        Send club suggestion notification email
        
        Args:
            club_name (str): Name of the suggested club
            
        Returns:
            tuple: (success: bool, message: str)
        """
        try:
            msg = Message(
                subject="Yeni Kulüp Önerisi",
                recipients=[MAIL_USERNAME],
                body=f"""
Birisi yeni kulüp önerisinde bulundu:

Önerilen Kulüp: {club_name}

Bu öneriyi değerlendirmek için lütfen gerekli işlemleri yapın.
"""
            )
            self.mail.send(msg)
            return True, 'Kulüp öneriniz başarıyla gönderildi!'
        except Exception as e:
            return False, f'Kulüp önerisi gönderilirken bir hata oluştu: {str(e)}' 