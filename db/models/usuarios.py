from db.models.usuario_model import Usuario

lista_usuarios: list[Usuario] = [
    Usuario(
        id='1',
        nombre='jhon',
        apellido='enriquez',
        codigo_usuario='202260647',
        rol='admin',
        email='jhon.enriquez@correounivalle.edu.co',
        password='jhon123'
    ),
    Usuario(
        id='2',
        nombre='javier',
        apellido='lopez',
        codigo_usuario='202260100',
        rol='coordinador',
        email='javier.lopez@correounivalle.edu.co',
        password='javi123'
    ),
    Usuario(
        id='3',
        nombre='mauricio',
        apellido='prieto',
        codigo_usuario='202260101',
        rol='coordinador',
        email='mauricio.prieto@correounivalle.edu.co',
        password='mauro123'
    ),
]