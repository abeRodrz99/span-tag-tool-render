from flask import Flask, request, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

def remove_span_tags(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    for span in soup.find_all("span"):
        span.unwrap()
    return soup.prettify()

@app.route("/", methods=["POST"])
def process_html():
    data = request.get_json()
    if "html" not in data:
        return jsonify({"error": "Missing 'html' field"}), 400

    updated_html = remove_span_tags(data["html"])
    return jsonify({"updated_html": updated_html})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
