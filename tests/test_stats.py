import pytest

from op_stats.app import app
from op_stats.stats import Stats

@pytest.fixture
def client():
  client = app.test_client()
  return client


def testEstadoCPU(mocker,client):
  mocker.patch.object(Stats, 'estado_cpu', return_value=100)
  response =client.get('/estadoCPU')
  assert response.data.decode('utf-8')=='{"cpu_percent": 100}'
  assert response.status_code ==200

def testEstadoDisco(mocker,client):
  mocker.patch.object(Stats, 'espacio_disco', return_value=100)
  response = client.get('/espacioDisco')
  assert response.data.decode('utf-8') == '{"espacio_disco": 100}'
  assert response.status_code ==200


def testEstadoMemoria(mocker, client):
  mocker.patch.object(Stats, 'estado_memoria', return_value=100)
  response = client.get('/estadoMemoria')
  assert response.data.decode('utf-8') == '{"estado_memoria": 100}'
  assert response.status_code ==200

