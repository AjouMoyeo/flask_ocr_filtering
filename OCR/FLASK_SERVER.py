from flask import Flask
from werkzeug.utils import secure_filename
import subprocess
from flask import Flask
from werkzeug.utils import secure_filename
import subprocess
from flask import Flask, render_template, request, redirect, url_for
import json
from flask_cors import CORS


app= Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello World'
    
@app.route('/filtering',methods=['POST'])
def filtering():
    data = request.get_json(silent=True)
    text = data.get('title') + data.get('text')
    # 게시글 제목(title), 내용(text) 받아서 필터링
    subprocess.call("filtering.py --text '" + text + "'", shell=True) #입력값이 있음
    with open("filtering_result.txt", 'r', encoding='utf-8') as f:
        result = f.readline()
    return str(result)
        

@app.route('/card', methods = ['POST'])
def file_upload():
    if request.method == 'POST':
        f = request.files['image']
        f.save('image/' + secure_filename(f.filename))

        subprocess.call("OCR.py", shell=True)
        
        with open ('info.json', 'r', encoding = 'utf-8') as f:
            json_data = json.load(f)
            
        return str(json_data)    
        
       
if __name__ =='__main__':
    app.run(port="7000",debug=True)
