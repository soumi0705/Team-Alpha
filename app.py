from flask import Flask, render_template
from beautiful_soup import state_names,state_number,state_conf,state_active,state_disc,helpline
class State:
        name=[]
        number=[]
        conf=[]
        active=[]
        disc=[]
s = State()
s.name=state_names
s.number=state_number
s.conf=state_conf
s.active=state_active
s.disc=state_disc
s.helpline=helpline
app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('home.html',name=state_names,number=state_number,conf=state_conf,active=state_active,disc=state_disc,hel=helpline)
    


if __name__=='__main__':
    app.run(debug=True) 