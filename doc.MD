Для запуска проекта:

    docker-compose up -d --build

    дополнительные инструкции:
        docker-compose exec web sh
        python manage.py migrate
    
        python manage.py createsuperuser
        
        apt-get update
        apt-get install python3-tk