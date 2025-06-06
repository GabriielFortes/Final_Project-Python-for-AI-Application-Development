''' 
Executing this function initiates the application of Emotion 
Detector to be executed over the Flask channel and deployed 
on localhost:5000.
'''
from flask import Flask, request, jsonify, render_template
from Emotion_Detection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyze():
    ''' This code receives the text from the HTML interface and 
        runs Emotion Detector over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    if result is None:
        return "Erros: Unable to analyze emotions. Please provide valid text."

    return jsonify(result)


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
