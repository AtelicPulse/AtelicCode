from flask import Flask, request, jsonify
from code_autocomplete import get_suggestions
from bug_detection import detect_bugs

app = Flask(__name__)


@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    data = request.json.get("code", "")
    suggestions = get_suggestions(data)
    return jsonify({"suggestions": suggestions})


@app.route('/bug-detection', methods=['POST'])
def bug_detection():
    data = request.json.get("code", "")
    bugs = detect_bugs(data)
    return jsonify({"bugs": bugs})


if __name__ == '__main__':
    app.run(debug=True)
