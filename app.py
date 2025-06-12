from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from modules.gemini_service import GeminiService
from modules.email_service import EmailService
from modules.config import KULUP_LISTESI
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a secure random key

# Initialize services
gemini_service = GeminiService()
email_service = EmailService(app)

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

        success, message = email_service.send_club_application(email, club, isim, soyisim)
        return jsonify({
            'success': success,
            'message': message
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Başvuru gönderilirken bir hata oluştu: {str(e)}'
        })

@app.route('/suggest-club', methods=['POST'])
def suggest_club():
    try:
        club_name = request.form.get('club_name')
        
        if not club_name:
            return jsonify({
                'success': False,
                'message': 'Lütfen bir kulüp adı girin.'
            })

        success, message = email_service.send_club_suggestion(club_name)
        return jsonify({
            'success': success,
            'message': message
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Kulüp önerisi gönderilirken bir hata oluştu: {str(e)}'
        })

if __name__ == '__main__':
    app.run(debug=True, port=5001)