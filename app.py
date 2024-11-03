from flask import Flask, request, jsonify, render_template
import openai
import os
app = Flask(__name__)
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/code_review', methods=['POST'])
def code_review():
    data = request.get_json()
    user_code = data.get("code")

    if not user_code:
        return jsonify({"error": "Code is required"}), 400

    prompt = f"Aşağıdaki kodu inceleyin ve bir üst düzey geliştirici gibi yorum yapın. " \
             f"iyileştirme önerilerinde bulunun " \
             f"Eğer öneride bulunan kodu güncelleyebiliyorsan güncellenmiş halini de en sona ekle " \
             f"ve potansiyel sorunları vurgulayın. Yanıtlar Türkçe olsun:\n\n{user_code}\n"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": "You are a senior developer reviewing code."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=700,
            temperature=0.7,
        )

        review_text = response['choices'][0]['message']['content'].strip()
        return jsonify({"review": review_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  
