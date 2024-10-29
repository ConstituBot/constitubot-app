import streamlit as st
import requests


# Display an image (Make sure 'image.jpg' is in your working directory or provide an image URL)
st.image("/home/arthur/Documentos/UEA/constitubot-app/brasao_republica.jpg", caption="República Federativa do Brasil")

# Title
st.title("ConstituBot")

# Subtext
st.subheader("A mais novo chatbot de consulta à Constituição Brasileira!")

st.write("""Eu sou um chatbot especializado em fornecer informações sobre a Constituição Brasileira. Minha função principal é fornecer respostas claras e precisas sobre as disposições constitucionais, interpretando o texto legal da Constituição Federal do Brasil e, quando necessário, me referindo a outras normas legais complementares disponíveis no site leg.br.

Algumas possibilidades de uso incluem:

 - Consultas sobre direitos e deveres constitucionais;
 - Busca por artigos específicos da Constituição;
 - Explicações sobre instituições e processos políticos previstos na Carta Magna;
 - Informações sobre competências e atribuições dos poderes públicos (executivo, legislativo e judiciário);
 - Verificações sobre a compatibilidade de leis e atos com a Constituição.
         
Em suma, meu objetivo é auxiliar usuários a esclarecer dúvidas e a aprofundar o conhecimento sobre a legislação brasileira, especialmente em relação à Constituição Federal.
""")

# Input text box for questions
user_input = st.text_input("Digite aqui sua pergunta:")

# API URL (Make sure to replace with the correct URL and port where your Flask app is running)
api_url = "http://127.0.0.1:5000/chatbot"  # Update the port if needed

# Display chatbot response when user submits a question
if user_input:
    # Send a POST request to the Flask API
    response = requests.post(api_url, json={"message": user_input})
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract chatbot response from JSON
        chatbot_response = response.json().get("response", "Não foi possível obter resposta.")
        st.write(chatbot_response)
    else:
        st.write("Erro: Não foi possível conectar ao chatbot.")
