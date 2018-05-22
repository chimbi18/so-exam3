import psutil

class Stats():

  @classmethod
  def estado_cpu():
    return "Estado de la CPU"+ str(psutil.cpu_percent(interval=1, percpu=True))

  @classmethod
  def estado_memoria():
    return "Estado de Memoria" + str( psutil.swap_memory())

  @classmethod
  def espacio_disco():
    return "Espacio de Disco" + str(psutil.disk_usage('/'))

