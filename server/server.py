from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
import json
from aggregator import Aggregator

CORS(app)

aggregator = Aggregator()

@app.route('/')
def hello():
    return """<script> 
                function send_ajax(){
                    var xhr = new XMLHttpRequest();
                    xhr.open('GET', 'http://127.0.0.1:5000/search?test=123');
                    xhr.send();
                }
            </script>
            <div onclick='send_ajax()' style='width:100px;height:100px;background-color:red'></div>"""

@app.route('/reverse_search', methods=['GET'])
def reverse_search():
    skills = request.args['skills'].split("+")
    print(skills)
    return '[{"title": "senior java developer", "result": 50}, {"title": "asfdasdf", "result": 10}]'

@app.route('/search', methods=['GET'])
def search():
    temp = aggregator.search_in_db(request.args['text'], int(request.args['limit']))
    return temp
    
if __name__ == '__main__':
    app.run()