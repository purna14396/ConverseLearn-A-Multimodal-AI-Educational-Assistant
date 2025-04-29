import streamlit as st

# Set the background color using CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #021129;  /* Blue color */
        
    }
    </style>
    """,
    unsafe_allow_html=True
)

# navigation bar using custom HTML and CSS
st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

    .navbar {
    background:  #021129;
    margin: 0px -256px;
    padding-left:80px;
    padding-right:80px;

    margin-top:-39px;
    color: hsl(0, 0%, 100%);
    height: 60px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    
    }

    .navbar .logo {
    font-size: 30px;
    font-weight: bold;
    padding-bottom:10px;
    }

    .navbar a {
    color: #fff;
    text-decoration: none;
    font-size: 18px;
    font-weight: bold;
    }

    .navbar a:hover {
    color: lightblue;
    
    }

    .navbar ul {
    display: flex;
    list-style-type: none;
    }

    .navbar ul li {
    margin-left: 20px;
    }
    .navbar .logout{
    border: 2px solid rgb(180, 175, 175);
    color: rgb(245, 0, 0);
    padding: 10px;
    border-radius: 10px;
    }
    .navbar .logout:hover {
        color: red;
        transform: scale(1.2);
    }
    </style>
    
    
    
    
    <!-- Navbar -->
    
    <nav class="navbar">
        <div class="logo">Converse Learn</div>
        <ul class="nav">
            <li>
            <a href="#">Home</a>
            </li>
            <li>
            <a href="#services">Services</a>
            </li>
            <li>
            <a href="https://www.linkedin.com/in/purna-sai-potu-96a15523b/" target="_blank">Contact</a>
            </li>
            <li class="logout-btn">
            <a href="#" class="logout" >Logout</a>
            </li>
        </ul>
    </nav>

    """,
    unsafe_allow_html=True
)
    


# Inject CSS for positioning the button container
st.markdown("""
    <style>
    .logout-container {
        
        top: 10px;
        right: 10px;
        z-index: 1000;
        padding-left:1000px;
    }
    </style>
""", unsafe_allow_html=True)


# main content
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

    .header {
        height: 400px;
        background: #021129;
        margin: 0px -256px;
        margin-top: 50px;
        margin-bottom: 100px;
        padding-left: 30px;
        padding-right: 70px;
        gap: 40px;
        color: hsl(0, 0%, 100%);
        display: flex;
        justify-content: space-between;
    }

    .header h1 {
        color: white;
        font-size: 3rem;
        font-weight: bold;
        line-height: 1.2;
        margin-top: 20px;
        margin-bottom: 100px;
    }

    .header .tagline {
        color: white;
        max-width: 55%;
        margin-left: 50px;
    }

    .header p {
        line-height: 190%;
    }

    .header img {
        padding-top: 10px;
        padding-right: 10px;
        width: 400px;
        border-radius: 100px;
    }

    #services {
        margin: 0px -200px;
        display: flex;
        justify-content: space-between;
        gap: 30px;
        padding: 25px;
        border-radius: 50px;
        
        
        background: #343c42;
    }

    .service-card {
        background: #021129;
        color: white;
        padding: 20px;
        border-radius: 50px;
        text-align: center;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        cursor: pointer;
    }

    .service-card:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px  rgba(255,255,255,1);
    }

    .service-card h2 {
        margin-bottom: 20px;
        font-size: 2rem;
    }

    .service-card p {
        line-height: 1.8;
    }
    
    .copyright {
        text-align: center;
        color: white;
        padding: 20px;
        margin-top: 50px;
        margin-bottom: -50px;
       
        font-size: 1rem;
        opacity: 0.7;
        letter-spacing: 1px;
    }
    
    </style>

    <!-- header -->
    <header class="header">
        <div class="tagline">
            <h1>
                Learn, Practice and Succeed with AI support.
            </h1>
            <p>
                ConverseLearn is an AI-powered educational platform designed to help users master communication skills through interactive learning and practice. It combines a conversational AI assistant for grammar guidance with personalized quizzes and real-time feedback. The platform adapts quiz difficulty based on performance, making language learning engaging, supportive, and effective.
            </p>
        </div>
        <img src="https://i.postimg.cc/DZfqqQ5T/AI-Bot-image.png" alt="" />
    </header>
    
    <br><br><br>

    <!-- Services Section -->
    <div id="services">
        <div class="service-card">
            <h2>Learn and Practice Grammar</h2>
            <p>Improve your grammar skills with interactive lessons and quizzes tailored to your progress.</p>
        </div>
        <div class="service-card">
            <h2>AI Speech Analysis</h2>
            <p>Receive instant feedback on your pronunciation and fluency with AI-powered speech analysis.</p>
        </div>
        <div class="service-card">
            <h2>Conversational AI</h2>
            <p>Practice real-world conversations with our intelligent AI chatbot for better communication skills.</p>
        </div>
    </div>

    
    <div class="copyright">
        © 2025 Developed by ConverseLearn
    </div>

    """,
    unsafe_allow_html=True
)
