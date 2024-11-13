para instalar el entorno virtual: 
- python3 -m venv env
- env\Scripts\activate

- pip install django

Para iniciar el proyecto ESTAR DENTRO DE LA CARPETA PROYECTO:
-   python manage.py runserver




PASOS PARA CONFIGURAR LA BASE DE DATOS

-Escribir en cmd "mariadb --version" para comprobar si ya teneis mariadb instalado y no teneis que seguir con los demas pasos, si es asi pasar a seeds
- Descargar mariadb desde la pagina web
- Abrir el instalador y seguir los pasos poniendo
    - Contraseña "root"
- Abrir las variables de entorno y poner en variables del sistema "C:\Program Files\MariaDB 11.5\bin"
- Escribir en el cmd "mariabd --version"
- Si no os da una version reiniciar el ordenador

Ahora dentro del entorno virtual
- mariadb -u root -p
-   CREATE DATABASE dbpgpipaas CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

    CREATE USER 'pgpipaas_user'@'localhost' IDENTIFIED BY 'pgpipaas_password';
    GRANT ALL PRIVILEGES ON dbpgpipaas.* TO 'pgpipaas_user'@'localhost';
    FLUSH PRIVILEGES;


MIGRATION
python manage.py makemigrations
python manage.py migrate




SEEDS
- Escribir el codigo para introducir en los seeds
- Para hacer el seed "python seed_data.py"

