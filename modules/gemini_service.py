import google.generativeai as genai
from .config import GEMINI_API_KEY, KULUP_LISTESI

class GeminiService:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def get_club_recommendation(self, isim, soyisim, bolum, hobi, ilgi):
        mesaj = f"""
        Aşağıdaki öğrenci için sadece şu kulüplerden en uygun olan 5 tanesini öner. Her kulübü yeni satırda yaz. Yorum ekleme:
        {', '.join(KULUP_LISTESI)}

        Öğrenci bilgileri:
        - İsim: {isim} {soyisim}
        - Bölüm: {bolum}
        - Hobi: {hobi}
        - İlgi Alanları: {ilgi}
        """

        try:
            response = self.model.generate_content(mesaj)
            # Split the response into a list and clean up each item
            clubs = [club.strip() for club in response.text.split('\n') if club.strip()]
            return clubs
        except Exception as e:
            return [f"Bir hata oluştu. Lütfen daha sonra tekrar deneyiniz."] 