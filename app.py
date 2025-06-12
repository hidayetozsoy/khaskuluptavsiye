from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_mail import Mail, Message
from modules.gemini_service import GeminiService
from modules.config import KULUP_LISTESI
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a secure random key

# Flask-Mail configuration for Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'khaskuluptavsiye@gmail.com'  # Replace with your Gmail address
app.config['MAIL_PASSWORD'] = 'zxqv nksu wolp uawz'      # Replace with your Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = 'khaskuluptavsiye@gmail.com'  # Replace with your Gmail address

# Initialize Flask-Mail
mail = Mail(app)
gemini_service = GeminiService()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            isim = request.form.get('isim')
            soyisim = request.form.get('soyisim')
            bolum = request.form.get('bolum')
            hobi = request.form.get('hobi')
            ilgi = request.form.get('ilgi')

            kulup_onerisi = gemini_service.get_club_recommendation(
                isim=isim,
                soyisim=soyisim,
                bolum=bolum,
                hobi=hobi,
                ilgi=ilgi
            )
            
            if "Hata oluştu" in kulup_onerisi[0]:
                flash(kulup_onerisi[0], 'error')
                return redirect(url_for('home'))
            
            # Store the result and user info in session
            session['kulup_onerisi'] = kulup_onerisi
            session['isim'] = isim
            session['soyisim'] = soyisim
            return redirect(url_for('result'))
        except Exception as e:
            flash(f"Bir hata oluştu: {str(e)}", 'error')
            return redirect(url_for('home'))

    return render_template('form.html')

@app.route('/result')
def result():
    kulup_onerisi = session.get('kulup_onerisi')
    if not kulup_onerisi:
        flash("Lütfen önce bir kulüp tavsiyesi alın.", 'error')
        return redirect(url_for('home'))
    return render_template('result.html', kulup=kulup_onerisi)

@app.route('/send-email', methods=['POST'])
def send_email():
    kulup_onerisi = session.get('kulup_onerisi')
    isim = session.get('isim')
    soyisim = session.get('soyisim')
    
    if not all([kulup_onerisi, isim, soyisim]):
        return jsonify({
            'success': False,
            'message': 'Oturum bilgileri eksik. Lütfen tekrar deneyin.'
        })

    try:
        email = request.form.get('email')
        club = request.form.get('club')

        if not email or not club:
            return jsonify({
                'success': False,
                'message': 'Lütfen e-posta adresinizi girin.'
            })

        msg = Message(
            subject=f'{club} Kulübüne Hoş Geldiniz',
            recipients=[email],
            body=f"""
Sayın {isim} {soyisim},

{club} kulübümüze hoş geldiniz! Başvurunuz alınmıştır.

En kısa sürede sizinle iletişime geçeceğiz.

Saygılarımızla,
{club}
"""
        )
        mail.send(msg)
        return jsonify({
            'success': True,
            'message': 'Başvurunuz başarıyla alındı!'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Başvuru gönderilirken bir hata oluştu: {str(e)}'
        })

if __name__ == '__main__':
    app.run(debug=True, port=5001)