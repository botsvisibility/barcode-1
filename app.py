import firebase_admin
from firebase_admin import credentials

from firebase_admin import db, credentials,firestore
from flask import Flask, render_template
cd = credentials.Certificate("cred.json")
firebase_admin.initialize_app(cd,{"databaseURL":"https://esp32-61087-default-rtdb.firebaseio.com/" })

app = Flask(__name__,template_folder='template')

@app.route('/')
def my_route():
    values_2 = []
    values = []

    ref = db.reference('/test/json/value/round')
    ref_1 = db.reference('/test/json/value/time')
    datas = ref.get()
    times = ref_1.get()

    values_2 = [value for value in reversed(times.values()) if value not in values_2]
    values = [value for value in reversed(datas.values()) if value not in values]

    
    
    return render_template('index.html', my_list=values,my_list2= values_2)

if __name__ == '__main__':
    app.run(debug=False)