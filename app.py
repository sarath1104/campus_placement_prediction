import streamlit as st
import pickle
pickle_in=open("model.pkl","rb")
model=pickle.load(pickle_in)
def placement_predict(Branch,College,CGPA,internship,backlog,score):
    prediction=model.predict([[Branch,College,CGPA,internship,backlog,score]])
    print(prediction)
    return prediction

def main():

    
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">CAMPUS PLACEMENT PREDICTION  </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Branch = st.selectbox(label= "Branch", options = ['CSE','ECE','IT','EEE','Mechanical','CSD','CSE(AI&ML)','Robotics','Mechanical robotics'])
    branch_map={'CSE': 0,
    'ECE': 1,
    'IT': 2,
    'EEE': 3,
    'Mechanical': 4,
    'CSD': 5,
    'CSE(AI&ML)': 6,
    'Robotics': 7,
    'Mechanical robotics': 8}
    Branch=branch_map[Branch]
    College = st.selectbox(label="College", options=['GVPCE - A','GVPCE - W'])
    College_map={'GVPCE - A':0, 'GVPCE - W':1}
    College= College_map[College]
    CGPA = st.text_input("CGPA")
    internship = st.selectbox(label="Internship", options=['YES','NO'])
    intern_map={'YES':1,'NO':0}
    internship=intern_map[internship]
    Backlog_history = st.selectbox(label="Backlog History", options=['YES','NO'])
    backlog_map={'YES':1,'NO':0}
    Backlog_history=backlog_map[Backlog_history]
    skills=st.multiselect('Skills',['C','C++', 'python','Java', 'front end development','back end development','full stack','Data structures', 'tabulae','MERN','R', 'Photoshop', 'flutter', 'Android development'])
    score_map={ 'C':1,'C++':2, 'python':3,'Java':4, 'front end development':5,'back end development':6,'full stack':7,'Data structures':8, 'tabulae':9,'MERN':10,'R':11, 'Photoshop':12, 'flutter':13, 'Android development':14}
    skills=[score_map[s] for s in skills] 
    result = ""
    if st.button("Predict"):
            if CGPA == "" or len(skills) == 0:
                 st.warning("Please Enter All Values.")
            else:
                def placement_predict(Branch, College, CGPA, internship, Backlog_history, skills):
                    prediction = model.predict([[Branch, College, CGPA, internship, Backlog_history, skills]])
                    print(type(prediction))
                    return prediction[0]
                result=placement_predict(Branch, College, CGPA, internship, Backlog_history, len(skills))
                if(result==0):
                    result='Not Placed'
                else:
                    result='Placed'
                st.success('The Student Is {}'.format(result))
    

if __name__=='__main__':
    main()
