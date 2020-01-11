from flask import Flask, requests
from flask_cors import CORS
app = Flask(__name__)

CORS(app)

@app.route('/')
def hello():
    return """<script> 
                function send_ajax(){
                    var xhr = new XMLHttpRequest();
                    xhr.open('GET', 'http://127.0.0.1:5000');
                    xhr.send();
                }
            </script>
            <div onclick='send_ajax()' style='width:100px;height:100px;background-color:red'></div>"""

@app.route('/search', methods=['GET']):
    print(requests.args)
    
if __name__ == '__main__':
    app.run()
