import os
import pandas as pd
from pandas import DataFrame
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

# Constants
UPLOAD_FOLDER: str = os.path.join(os.curdir, 'static/uploads')
ALLOWED_DATA_EXTENSIONS: set[str] = {'csv'}

# Singletons (Forgot the real term)
StudentData: DataFrame
ProgramStudents: DataFrame
CertificateStudents: DataFrame

# Setup
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app: Flask = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'


# For each term and program combination, calculate the average student credit hours.
# Average Credits = Total ActiveCred for program / Number of students in program

# Semester | Division | Program | Avg. Credits
# 2023FA   | CGEN3    | A25590C | 12.3
# - Semester comes from the TermId column
# - Division comes from the ProgramDivision column
# - Program comes from the StudentTermProgram column
# - Avg. Credits is calculated from the ActiveCred column

def allowed_data_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_DATA_EXTENSIONS

@app.route("/upload_data_file", methods=['GET', 'POST'])
def upload_data_file():
    global StudentData
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return {"result": "No file part"}
        file: FileStorage = request.files['file']
        
        if file.filename == '':
            return {"result": "No selected file"}
        
        if file and allowed_data_file(file.filename):
            StudentData = pd.read_csv(file.stream)
            ProgramStudents     = StudentData[StudentData["StudentTermProgram"][0] == "A"]
            CertificateStudents = StudentData[StudentData["StudentTermProgram"][0] == "C"]
            print(StudentData)
            print(ProgramStudents)
            print(CertificateStudents)
            return {"result": "Success"}
    return {"result": "GET"}

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('app.html')


if __name__ == "__main__":
    print("We are starting.")
    app.run()
    print("We are done.")