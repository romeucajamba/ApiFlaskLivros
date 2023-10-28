from flask import Flask
from flask import jsonify # para retornar a nossa api em formato json
from flask import request # nos permite acessar os dados que estão indo e vindo das requesições.

app = Flask(__name__) # Desse jeito estou criando uma aplicação flask com o nome do arquivo atual

# minha lista de dados

books = [
    {
        'id': 1,
        'titulo': 'O senhor dos aneis',
        'autor': 'Romeu',
    },
     {
        'id': 2,
        'titulo': 'Hora de Aventura',
        'autor': 'Rbert',
    },
     {
        'id': 3,
        'titulo': 'Herry Potter',
        'autor': 'Cajamba',
    },
]
#EndPoints
 # Criar api que nos permite consultar(Todos),consultar(por id), excluir e editar.

 #Consultar Todos
@app.route('/livros', methods=['GET'])
def get_books():
    return jsonify(books)


# - Consultar livors por id
@app.route('/livros/<int:id>', methods=['GET'])
def get_books_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)


# Editar livro
@app.route('/livros/<int:id>', methods=['PUT'])
def change_book(id):
    # Obter informações enviadas pelo usuário para a API
    book_changed = request.get_json() 
    # obter o livro pelo indece e id
    for indece, book in enumerate(books):
        if book.get('id') == id:
            books[indece].update(book_changed)
            return jsonify(books[indece])

@app.route('/livros', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)


# Excluir livros
@app.route('/livros/<int:id>', methods=['DELETE'])
def delete_book(id):
    for indece, book in enumerate(books):
        if book.get('id') == id :
            del books[indece]
            return jsonify(books)
        
if __name__ == '__main__':
    app.run(debug=True, port=3000, host='localhost')