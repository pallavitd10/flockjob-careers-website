from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru,India',
    'salary':'Rs.10,00,000'
  },
  {
   'id':2,
    'title':'Data Scientist',
    'location':'Mumbai,India',
    'salary':'Rs.15,00,000'
  },
{
   'id':1,
    'title':'Frontend Engineer',
    'location':'San Fransisco,USA'
    
  },
{
  'id':1,
    'title':'Backend Engineer',
    'location':'delhi,India',
    'salary':'Rs.20,00,000'
  }
]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name='FlackJob')

@app.route("/jobs")
def hello_job():
  return jsonify(JOBS)
 


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
