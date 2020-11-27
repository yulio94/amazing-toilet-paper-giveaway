# amazing-toilet-paper-giveaway
¡Se va a sortear un abastecimiento de papel de por vida para el afortunado ganador!

# Ejecucion del proyecto
```
docker-compose up --build
```
una vez los contenedores esten corriendo ejecutar los siguientes comandos para correr las migraciones:
```
docker-compose exec raffle_api bash
./manage.py makemigrations
./manage.py migrate
```

ejectuar celery:
```
celery -A mysite worker -l info
```

# Endpoints disponibles

## Creacion de usuario:
```
/api/v1/new-user/
```
## Crear nuevo password:
Nota: esta url es usada cuando el usuario recibe un correo de validacion.
```
/api/v1/change-password/str:token/
```

## Ganador:
Busca de forma generica un ganador entre los usuarios.
```
/api/v1/winner/
```
