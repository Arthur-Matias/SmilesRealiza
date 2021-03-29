from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)
import random
import pandas as pd
table = pd.read_excel('datatable.xlsx')

from flask_cors import CORS, cross_origin
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

# Database user examples
import numpy as np

def create_package(table):
    de = random.randint(0,len(table))
    para = random.randint(0,len(table))
    preço_real = 750 + random.randint(-75,75) + np.random.randn()
    preço_milhas = (1000/50) * preço_real

    return {
        'de' : table.iloc[de,0],
        'para' : table.iloc[para,0],
        'preço em real' : round(preço_real,2),
        'preço em milhas': int(preço_milhas),
    }

# rascunho
Pacotes = [create_package(table = table.copy()) for _ in range(20)]

# tabela específica para o relacionamento 
MMPacotesUsuarios = [
    {
        'usuario' : "Henrique Mauler", # ID
        'pacote' : 0, # ID
        'quantidade de parcelas' : 10,
        'parcelas pagas' : 3,
        'valor das parcelas' : 5800.00,

    }
]

Usuarios = [
    {
        'name' : 'Henrique Mauler',
        'milhas' : 1200
    },
    {
        'name' : 'Arthur Matias',
        'milhas' : 2350
    },
    {
        'name' : "Eliza Wollinger",
        'milhas' : 5300
    },
    {
        'name' : 'convidado para testes',
        'milhas' : 0
    },
]

Usuarios = pd.DataFrame(Usuarios)
MMPacotesUsuarios = pd.DataFrame(MMPacotesUsuarios)
Pacotes = pd.DataFrame(Pacotes)


table = table.replace({
    'Sim' : True,
    'Não' : False,
})

# Routes
@app.route('/')
def hello_world():
    return MMPacotesUsuarios.to_html()

@app.route('/get_all_packages', methods = ['GET','POST'])
def get_packages():
    return Pacotes.to_json(orient = 'records')


@app.route('/choose_package',methods = ['GET','POST'])
@cross_origin()
def choose_package():
    data = dict(request.json)
    name = data['name']
    cpf = data.get('cpf')
    
    pacote_id = int(data['pacote_id'])
    global MMPacotesUsuarios


    preço_real = Pacotes.iloc[pacote_id,:].loc["preço em real"]
    preço_milhas = Pacotes.iloc[pacote_id,:].loc["preço em milhas"]

    # Converter tudo para milha
    preço_total = preço_milhas + preço_real * 1000/50 

    # parcelas
    preço_parcelado = preço_real / 12

 

    new = MMPacotesUsuarios.append({
        'usuario' : 'convidado', # ID para o MVP
        'pacote' : pacote_id , # ID
        'quantidade de parcelas' : 12,
        'parcelas pagas' : 3,
        'valor das parcelas' : preço_parcelado,

    },ignore_index = True)

    MMPacotesUsuarios = new.copy()

    return new.to_json(orient = 'records')


@app.route('/get_packages_user_info',methods = ['GET','POST'])
def get_packages_user_info():
    global MMPacotesUsuarios
    return MMPacotesUsuarios[MMPacotesUsuarios.loc[:,'usuario'] == 'convidado'].to_json(orient = 'records')
    
    pass
