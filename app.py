from flask import Flask,render_template,request,redirect,session
import pickle
import numpy as np


# 1.created object for class Flask
app=Flask(__name__)

# loading model--model should contain only numbers
with open("ipl_model.pkl","rb")as f:
    model=pickle.load(f)

#7.
def predict_score(batting_team='Chennai Super Kings', bowling_team='Mumbai Indians', overs=5.1, runs=50,
                   wickets=0, runs_in_prev_5=50, wickets_in_prev_5=0):
  temp_array = list()

  # Batting Team
  if batting_team == 'Chennai Super Kings':
    temp_array = temp_array + [1,0,0,0,0,0,0,0]
  elif batting_team == 'Delhi Daredevils':
    temp_array = temp_array + [0,1,0,0,0,0,0,0]
  elif batting_team == 'Kings XI Punjab':
    temp_array = temp_array + [0,0,1,0,0,0,0,0]
  elif batting_team == 'Kolkata Knight Riders':
    temp_array = temp_array + [0,0,0,1,0,0,0,0]
  elif batting_team == 'Mumbai Indians':
    temp_array = temp_array + [0,0,0,0,1,0,0,0]
  elif batting_team == 'Rajasthan Royals':
    temp_array = temp_array + [0,0,0,0,0,1,0,0]
  elif batting_team == 'Royal Challengers Bangalore':
    temp_array = temp_array + [0,0,0,0,0,0,1,0]
  elif batting_team == 'Sunrisers Hyderabad':
    temp_array = temp_array + [0,0,0,0,0,0,0,1]

  # Bowling Team
  if bowling_team == 'Chennai Super Kings':
    temp_array = temp_array + [1,0,0,0,0,0,0,0]
  elif bowling_team == 'Delhi Daredevils':
    temp_array = temp_array + [0,1,0,0,0,0,0,0]
  elif bowling_team == 'Kings XI Punjab':
    temp_array = temp_array + [0,0,1,0,0,0,0,0]
  elif bowling_team == 'Kolkata Knight Riders':
    temp_array = temp_array + [0,0,0,1,0,0,0,0]
  elif bowling_team == 'Mumbai Indians':
    temp_array = temp_array + [0,0,0,0,1,0,0,0]
  elif bowling_team == 'Rajasthan Royals':
    temp_array = temp_array + [0,0,0,0,0,1,0,0]
  elif bowling_team == 'Royal Challengers Bangalore':
    temp_array = temp_array + [0,0,0,0,0,0,1,0]
  elif bowling_team == 'Sunrisers Hyderabad':
    temp_array = temp_array + [0,0,0,0,0,0,0,1]

  # Overs, Runs, Wickets, Runs_in_prev_5, Wickets_in_prev_5
  temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]

  # Converting into numpy array
  temp_array = np.array([temp_array])
  print(temp_array)

  # Prediction
  return int(model.predict(temp_array)[0])



# 3.creating router
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html') 

# 4.
@app.route("/predict",methods=['POST','GET'])
#5. we have to check wheter form.get is string or number
def predict():
    if request.method=='POST':
        batting_team=request.form.get('batting_team')
        bowling_team=request.form.get('bowling_team')
        overs=float(request.form.get('overs'))
        runs=int(request.form.get('runs'))
        wickets=int(request.form.get('wickets'))
        runs_in_prev_5=int(request.form.get('runs_in_prev_5'))
        wickets_in_prev_5=int(request.form.get('wickets_in_prev_5'))
       
        score=predict_score(batting_team=batting_team,bowling_team=bowling_team,overs=overs,runs=runs,
                            wickets=wickets,runs_in_prev_5=runs_in_prev_5,
                      wickets_in_prev_5=wickets_in_prev_5)
        print(score)
        return render_template('predict.html',prediction=score)


    return render_template('predict.html') 





#2. to create main function
if __name__=='__main__':
    # running server
    app.run(debug=True,port=4008,host='0.0.0.0')

