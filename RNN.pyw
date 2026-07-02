pip install streamlit
pip install streamlit-lottie
pip install streamlit-option-menu
pip install streamlit-extras
pip install plotly
---------------------------------------------------
🎬 IMDb Movie Review Sentiment Analysis
Deep Learning | RNN | Keras

---------------------------------------
|       Lottie Animation              |
---------------------------------------

Enter Movie Review

[ Text Area ]

        Predict Button

---------------------------------------
Prediction

😊 Positive

Confidence
██████████████████ 96%

Gauge Meter

---------------------------------------
Prediction History

---------------------------------------
Footer
Made with ❤️ using Streamlit
st.set_page_config(
    page_title="IMDb Sentiment Analysis",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#141E30,#243B55);
color:white;
}

.big-title{
font-size:45px;
font-weight:bold;
text-align:center;
color:white;
}

.subtitle{
text-align:center;
font-size:20px;
color:#dddddd;
}

.card{
background:rgba(255,255,255,0.08);
padding:25px;
border-radius:20px;
backdrop-filter:blur(10px);
box-shadow:0px 10px 30px rgba(0,0,0,0.4);
}

.stButton>button{
background:#00C9FF;
background:linear-gradient(90deg,#00C9FF,#92FE9D);
color:black;
font-weight:bold;
border-radius:12px;
height:55px;
width:100%;
font-size:18px;
transition:0.4s;
}

.stButton>button:hover{
transform:scale(1.05);
}

textarea{
border-radius:15px !important;
}

</style>
""",unsafe_allow_html=True)
st.markdown('<p class="big-title">🎬 IMDb Sentiment Analysis</p>',unsafe_allow_html=True)

st.markdown('<p class="subtitle">Deep Learning using Recurrent Neural Network (RNN)</p>',unsafe_allow_html=True)
from streamlit_lottie import st_lottie
import requests

def load_lottie(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie=load_lottie("https://assets2.lottiefiles.com/packages/lf20_49rdyysj.json")

st_lottie(lottie,height=250)
st.markdown('<div class="card">',unsafe_allow_html=True)

review=st.text_area("Enter Movie Review")

predict=st.button("Predict Sentiment")

st.markdown("</div>",unsafe_allow_html=True)
progress=0

bar=st.progress(0)

for i in range(96):
    progress=i+1
    bar.progress(progress)
st.balloons()
st.snow()
import plotly.graph_objects as go

fig=go.Figure(go.Indicator(
    mode="gauge+number",
    value=96,
    title={'text':"Confidence"},
    gauge={
        'axis':{'range':[0,100]},
        'bar':{'color':"green"}
    }
))

st.plotly_chart(fig,use_container_width=True)
if prediction=="Positive":
    st.success("😊 Positive Review")
else:
    st.error("😞 Negative Review")
with st.sidebar:

    st.image("logo.png",width=120)

    st.title("IMDb RNN")

    st.info("""
Model : Simple RNN

Dataset : IMDb

Framework : TensorFlow / Keras

Accuracy : 88%

Language : Python
""")
if "history" not in st.session_state:
    st.session_state.history=[]

st.session_state.history.append(prediction)

st.write(st.session_state.history)
c1,c2,c3=st.columns(3)

c1.metric("Accuracy","88%")

c2.metric("Vocabulary","20,000")

c3.metric("Max Length","200")
st.markdown("""
---
<center>
Made with ❤️ using Streamlit | TensorFlow | Keras | Deep Learning
</center>
""",unsafe_allow_html=True)