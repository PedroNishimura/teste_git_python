from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

##########################################################
########################### 01 ###########################
##########################################################
@app.route('/')
def index():
    return render_template('index.html')


##########################################################
########################### 02 ###########################
##########################################################
# CRIANDO O DATAFRAME
df = pd.DataFrame({
    'alunos': ['Renato', 'Fernando', 'Rodrigo', 'Ana', 'Joana', 'Silvio', 'Carolina'],
    'notas': [15.00, 39.58, 62.92, 41.46, 48.33, 63.13, 70.00]
})

# RENDERIZE OS VALORES DO DATAFRAME df EM UMA TABELA HTML DENTRO DA PÁGINA /table.html (CRIE UM HTML PARA ISSO)
@app.route('/table')
def table():
    tbHtml = df.to_html(index=False) # TRANSFORMANDO O DF EM HTML PARA SER RENDERIZADO NA PÁGINA TABLE, COLOQUEI INDEX FALSE PARA NÃO APARECER O INDICE NA TABELA

    return render_template('table.html', table=tbHtml)

if __name__ == '__main__': # VERIFICANDO SE ESTÁ NA MAIN PARA ASSIM ADICIONAR O COMANDO RUN DO FLASK E RENDERIZAR AS TELAS.
    app.run(debug=True)