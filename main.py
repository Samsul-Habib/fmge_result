from bottle import Bottle, request, template
import pandas as pd
app = Bottle()
df = pd.read_csv('out.txt', header=None, delimiter=',')

# Extract each column into separate lists
S_No = df[0].tolist()
Roll_No = df[1].tolist()
original_Roll_No = Roll_No.copy()
Roll_No = [str(element) if isinstance(element, int) else element for element in Roll_No]
Application_ID = df[2].tolist()
Score = df[3].tolist()
Result = df[4].tolist()
Year = df[5].tolist()
@app.route('/')
def index():
    return template('index')

@app.route('/fetch_data', method='POST')
def fetch_data():
    roll_number = request.forms.get('roll_number')
    try:
        ind = Roll_No.index(roll_number)
        student_data = (Score[ind], Result[ind], Year[ind])
        return template('result', student_data=student_data)
    except ValueError:
        return '<p style="font-size: 20px; color: red;">Roll number not found</p>'

if __name__ == '__main__':
    Bottle.run(app, host='0.0.0.0', port=8080)
