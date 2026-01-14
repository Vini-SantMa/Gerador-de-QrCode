from flask import Flask
from flask import render_template, request, send_file #recursos especificos do flask
import qrcode # biblioteca que gera qrcodes
from io import BytesIO 

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def home():
    # Se abrir pagina web (get), chama e retorna o html na tela
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST': #Se clicar no botao pra gerar(post), pega o texto do forms no html
        textouser = request.form.get('textouser')
        if not textouser: #se nao digitar nada, mostra o html novamente
            return render_template('index.html', erro="digite algo!")

        img = qrcode.make(textouser) #Criar o qrcode usando a biblioteca -> o make transforma texto em imagem (uma matriz)
        
        buffer = BytesIO() # representação stream do arquivo na memoria
        img.save(buffer) # salvando os bytes da imagem no buffer
        buffer.seek(0) # usando o seek pra voltar o ponteiro ao inicio dos dados
        
        return send_file( #manda a imagem de volta pro navegador
            buffer, 
            mimetype = 'image/png',
            as_attachment = False, # Se fosse true, baixa no pc, o false mostra na tela.
            download_name = 'qrcode.png'
        )

if __name__ == '__main__':
    app.run(debug = True)