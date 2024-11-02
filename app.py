from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

openai.api_key = "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"

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
             f"ve potansiyel sorunları vurgulayın. Yanıtlar Türkçe olsun:\n\n{user_code}\n"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": "You are a senior developer reviewing code."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7,
        )

        review_text = response['choices'][0]['message']['content'].strip()
        return jsonify({"review": review_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  
