from flask import Flask, request, jsonify
from code import predict 

app = Flask(__name__)

@app.route("/generate", methods=['POST'])
def generate():
    payload = request.json
    assert payload
    #{ 'input': word, 'max_length': token_max_length, 'temperature': temp, 'token': token };
    prompt, max_len, pen_alpha, top_k = payload['input'], payload['max_length'], payload['alpha'], payload['top_k']
    res = predict(prompt, max_len=max_len, penalty_alpha=pen_alpha, top_k=top_k)
    return jsonify({'message': res, 'success': True})


if __name__ == '__main__':
    app.run('localhost', 5700)
