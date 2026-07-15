import streamlit as st
import joblib
import numpy as np

modelo = joblib.load('performance_estudantes/melhor_modelo.pkl')

st.markdown(
    "<h1 style='text-align: center;'> Previsão do Desempenho do Estudante no Exame </h1>",
    unsafe_allow_html=True
)
st.divider()
st.markdown("""
> 📌 **Nota Informativa**
> 
> Para as variáveis binárias deste modelo:
> * **0**  equivale a **Não**
> * **1** equivale a **Sim**
""")
st.divider()
idade=st.slider('Idade',17,24)
horas_estudo_dia=st.slider('horas de Estudo por Dia',0.0,8.3)
horas_rede_social=st.slider('Horas de Uso nas Rede Social',0.0,7.2)
horas_netflix=st.slider('Horas Assistidas na Netflix',0.0,5.4)
trabalho_meio_periodo=st.slider('Trabalha no meio Periodo',0,1)
porcentagem_de_presenca=st.slider('Porcentagem de Presença', 56.0,100.0)
horas_sono=st.slider('Horas de Sono por Noite', 3.2,10.0)
frequencia_exercicios=st.slider('Carga Horária de Atividade Física por Dia', 3.2,10.0)
avaliacao_saude_mental=st.slider('Estado da Saúde Mental (0 a 10)',1,10)
participacao_atividades_extracurriculares=st.slider('Participação do Estudante em Atividades Extracurriculares',0,1)


if st.button('Previsão da Classificação do Estudante'):
    dados_inseridos=np.array([[
        idade, horas_estudo_dia,
       horas_rede_social, horas_netflix, trabalho_meio_periodo,
       porcentagem_de_presenca, horas_sono,
       frequencia_exercicios, avaliacao_saude_mental,participacao_atividades_extracurriculares
]])
    previsao=modelo.predict(dados_inseridos)[0]
    if previsao==2:
        st.success('O estudante terá um excelente desempenho no exame.🥳')
    elif previsao==1:
        st.info('O estudante terá um médio desempenho no exame.😃')
    else:
        st.error('O estudante terá um baixo desempenho no exame.😬')
