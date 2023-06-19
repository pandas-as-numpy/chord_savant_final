# server.py
from flask import Flask, render_template, request, jsonify, render_template
import chord_savant as cs

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    audio_file = request.files["audio"]

    if audio_file and allowed_file(audio_file.filename):
        # Save the audio file to a temporary location
        audio_file.save("/home/linuxz/chord_savant/uploads/audio.mp3")

        cs.run_module()
        chords = cs.chord_recognition("/home/linuxz/chord_savant/uploads/audio.mp3")
        

        # Process and format predictions as desired
        # ...

        # Return the predictions as a JSON response or as a render template
        # return jsonify(chords)
        return render_template("index.html", chords=chords)

    else:
        return "Invalid file format"


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() == "mp3"


if __name__ == "__main__":
    
    app.run()
