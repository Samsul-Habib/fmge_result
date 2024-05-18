from bottle import Bottle, request, template
import pandas as pd
import socket    #this module searches the local IP address of machine
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# connect() for UDP doesn't send packets
s.connect(('10.0.0.0', 0))
bbb=s.getsockname()[0]
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
    #app.run(debug=True)
    #Bottle.run(app, host=bbb, port=8080)
    Bottle.run(app, host='0.0.0.0', port=8080)
