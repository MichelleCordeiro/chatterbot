from urllib import response
from hello import app


def test_hello():
  response = app.test_client().get("/hello_rota")

  # import pdb; pdb.set_trace()
  assert response.status_code == 200    # código 200 a página existe
  assert response.data == b"Testando hgnfghnfhngf"  # o 'b' é p informar q pode conter caracteres especiais, pq está vindo do html
