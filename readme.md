Typing Hint


# python.org/dev/peps/pep-0008/#function-and-variable-names
# python.org/3/library/typing.Union
git init; git commit -m "first commit"; git branch -M main; git remote add origin git@github.com:keepskills/alurapep8.git; git push -u origin main

Mypy - identação
pip install mypy

Usando o flake8 - força identação correta
pip install flake8

Para ignorar alguns padroes do flake8 dentro do seu projeto basta criar um arquivo .tox.ini e colocar o que quer ignorar, exemplo:

```ruby
[flake8]
ignore = F401,
```

union ajuda a identificar o que um metodo retorna