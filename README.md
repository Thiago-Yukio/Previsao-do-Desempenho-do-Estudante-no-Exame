# Previsão do Desempenho do Estudante no Exame

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.9-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)

## Sobre o projeto:

Este projeto aplica técnicas de **Machine Learning** para prever o desempenho de estudantes em exames com base em hábitos de estudo, rotina diária e fatores relacionados ao estilo de vida.

Foi desenvolvido utilizando **Python**, **Scikit-Learn** e **Streamlit**, permitindo que qualquer usuário informe os dados de um estudante e obtenha uma previsão automática de sua classificação de desempenho.

O projeto demonstra um fluxo completo de Ciência de Dados, passando por:

* análise exploratória dos dados;
* tratamento de valores ausentes;
* engenharia de atributos;
* treinamento de diferentes algoritmos;
* seleção do melhor modelo;
* implantação em uma aplicação web interativa.

---

## Objetivos:

* Analisar fatores que influenciam o desempenho acadêmico.
* Comparar diferentes algoritmos de Machine Learning.
* Construir um modelo capaz de classificar estudantes em diferentes níveis de desempenho.
* Disponibilizar o modelo através de uma interface simples utilizando Streamlit.

---

## Dataset:

O conjunto de dados contém informações sobre **1000 estudantes**, incluindo características acadêmicas e comportamentais.

Entre as variáveis estão:

* Idade
* Horas de estudo por dia
* Horas gastas em redes sociais
* Horas assistindo Netflix
* Trabalho de meio período
* Frequência escolar
* Horas de sono
* Frequência de exercícios físicos
* Avaliação da saúde mental
* Participação em atividades extracurriculares
* Nota do exame

Durante o pré-processamento:

* foram removidos registros com valores ausentes;
* variáveis categóricas foram convertidas utilizando **LabelEncoder**;
* foi criada uma variável alvo denominada **classificação do exame**.

---

## Classificação do desempenho:

A nota do exame foi convertida em três categorias:

| Nota    | Classificação           |
| ------- | ----------------------- |
| ≤ 50    | 🔴 Baixo desempenho     |
| 50 a 75 | 🟡 Médio desempenho     |
| > 75    | 🟢 Excelente desempenho |

---

## Análise Exploratória:

Durante o projeto foram realizadas:

* análise estatística;
* identificação de valores nulos;
* histogramas;
* matriz de correlação;
* análise das variáveis categóricas;
* distribuição das classes.

---

## Modelos avaliados:

Foram comparados os seguintes algoritmos:

* Decision Tree Classifier
* Random Forest Classifier
* Gradient Boosting Classifier
* HistGradientBoosting Classifier
* Decision Tree Regressor
* Random Forest Regressor

A seleção dos hiperparâmetros foi realizada utilizando **GridSearchCV** com validação cruzada de cinco folds.

---

## Melhor modelo:

O algoritmo que apresentou o melhor desempenho foi o:

**RandomForestClassifier**

Parâmetros:

```python
RandomForestClassifier(
    class_weight="balanced",
    random_state=42,
    max_depth=10,
    n_estimators=100
)
```

### Métricas:

| Métrica        |  Resultado |
| -------------- | ---------: |
| Accuracy       | **79,85%** |
| F1-Score Macro | **77,99%** |

---

## Aplicação Web:

A interface foi desenvolvida utilizando **Streamlit**.

O usuário informa características do estudante como:

* idade;
* horas de estudo;
* horas em redes sociais;
* horas assistindo Netflix;
* trabalho de meio período;
* frequência escolar;
* horas de sono;
* frequência de exercícios;
* saúde mental;
* participação em atividades extracurriculares.

Ao clicar no botão de previsão, o sistema informa uma das seguintes classificações:

* 🟢 Excelente desempenho
* 🟡 Médio desempenho
* 🔴 Baixo desempenho


## 👨‍💻 Autor

**Thiago Yukio**

GitHub:

https://github.com/Thiago-Yukio
