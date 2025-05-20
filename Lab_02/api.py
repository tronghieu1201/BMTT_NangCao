from flask import Flask, request, jsonify
from cipher import CaesarCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        data = request.json
        if not data or 'plain_text' not in data or 'key' not in data:
            return jsonify({'error': 'Missing plain_text or key'}), 400
        plain_text = data['plain_text']
        key = int(data['key'])
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        return jsonify({'encrypted_message': encrypted_text})
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid key format'}), 400

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        data = request.json
        if not data or 'cipher_text' not in data or 'key' not in data:
            return jsonify({'error': 'Missing cipher_text or key'}), 400
        cipher_text = data['cipher_text']
        key = int(data['key'])
        decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
        return jsonify({'decrypted_message': decrypted_text})
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid key format'}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
