from flask import Flask, render_template, request, redirect, url_for, session, flash


app = Flask(__name__)
app.secret_key = 'asd0uas03430d0i3aidu30du0a33434'

app.config['PRODUTOS'] = {
    100: {'id': 100, 'nome': 'Produto 1', 'preco': 10.00, 'imagem_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Product_sample_icon_picture.png/640px-Product_sample_icon_picture.png'},
    200: {'id': 200, 'nome': 'Produto 2', 'preco': 20.00, 'imagem_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Product_sample_icon_picture.png/640px-Product_sample_icon_picture.png'},
    300: {'id': 300, 'nome': 'Produto 3', 'preco': 30.00, 'imagem_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Product_sample_icon_picture.png/640px-Product_sample_icon_picture.png'},
}

@app.route('/')
def index():
    produtos = app.config['PRODUTOS']
    return render_template('index.html', produtos=produtos)

@app.route('/adicionar/<int:produto_id>', methods=['POST'])
def adicionar_ao_carrinho(produto_id):
    produtos = app.config['PRODUTOS']
    carrinho = session.get('carrinho', [])
    carrinho.append(produtos[produto_id])
    session['carrinho'] = carrinho
    flash('Produto adicionado ao carrinho!')
    return redirect(url_for('index'))

@app.route('/carrinho')
def carrinho():
    carrinho = session.get('carrinho', [])
    total = 0
    for item in carrinho:
        total += item['preco']
    return render_template('carrinho.html', carrinho=carrinho, total=total)

@app.route('/remover/<int:produto_id>', methods=['POST'])
def remover_do_carrinho(produto_id):
    carrinho = session.get('carrinho', [])
    for produto in carrinho:
        if produto['id'] == produto_id:
            carrinho.remove(produto)
            session['carrinho'] = carrinho
            flash('Produto removido do carrinho!')
            break
    else:
        flash('Produto não encontrado no carrinho.')
    return redirect(url_for('carrinho'))

if __name__ == '__main__':
    app.run(debug=True)