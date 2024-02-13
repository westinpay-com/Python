from flask import Flask, request
import hashlib
import hmac

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
    status = request.form['status']
    signature = request.form['signature']
    identifier = request.form['identifier']
    data = request.form['data']

    # Generate your signature
    custom_key = data['amount'] + identifier
    secret = b'YOUR_SECRET_KEY'
    my_signature = hmac.new(secret, custom_key.encode('utf-8'), hashlib.sha256).hexdigest().upper()

    my_identifier = 'YOUR_GIVEN_IDENTIFIER'

    if status == "success" and signature == my_signature and identifier == my_identifier:
        # Your operation logic
        pass

if __name__ == '__main__':
    app.run(debug=True)
