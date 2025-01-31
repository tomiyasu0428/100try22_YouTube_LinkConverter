from flask import Flask, request, render_template

app = Flask(__name__)


# URL変換関数
def convert_youtube_shorts(url):
    return url.replace("/shorts/", "/watch?v=") if "/shorts/" in url else url


@app.route("/", methods=["GET", "POST"])
def index():
    converted_url = ""
    if request.method == "POST":
        original_url = request.form.get("url")
        converted_url = convert_youtube_shorts(original_url)
    return render_template("index.html", converted_url=converted_url)


if __name__ == "__main__":
    app.run(debug=True)
