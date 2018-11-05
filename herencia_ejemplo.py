
class persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.pais = 'cr'

class empleado(persona):
    def __init__(self, nombre_empleado,
                 apellido_empleado
                 , id):
        super().__init__(nombre=nombre_empleado,
                         apellido=apellido_empleado,
                         )
        self.id = id
        self.pais = 'At'
    def __repr__(self):
        return f'soy un empleado. Mi nombre es  {self.nombre} {self.apellido}'
yo = empleado(nombre_empleado='erick',
              apellido_empleado='salas',
              id=314)
pass