# Aku-aku 
Микросервис ответственный за обработку  
отсеяных картинок и последующую вставку их же

# Запуск

```
docker run -e RMQ_HOST=localhost \ 
           -e RMQ_USER=guest \
           -e RMQ_PASS=guest \
           -e RMQ_PORT=5672 \
           -e DB_HOST=localhost \
           -e DB_PORT=5432 \
           -e DB_NAME=postgres \
           -e DB_USER=postgres \
           -e DB_PASS=postgres \
           -e PIC_FOLDER=pics \
           -e PIC_URL='image.walld.net'\
           -e LOG_LEVEL=INFO 
```