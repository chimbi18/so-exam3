from flask import Flask
import json


from op_stats.stats import Stats


app = Flask(__name__)

@app.route('/estadoCPU')
def estado_cpu():
  cpu_percent = Stats.estado_cpu() 
  return json.dumps({'cpu_percent': cpu_percent})
    

@app.route('/espacioDisco')
def espacio_disco():
  espacio_disco= Stats.espacio_disco()
  return json.dumps({'espacio_disco': espacio_disco})
    

@app.route('/estadoMemoria')
def estado_memoria():
  estado_memoria= Stats.estado_memoria()  
  return json.dumps({'estado_memoria': estado_memoria})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
