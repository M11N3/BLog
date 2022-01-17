# BLog

To start the application:

```sh
git clone https://github.com/M11N3/BLog
cd Blog
touch .env
```

__.env file__:

```sh
SECRET_KEY=                (django secrete_key)
USE_EMAIL_SEND=            (Use send_mail to notify ubscribers about new articles True or False)
EMAIL_HOST=                (The host to use for sending email.)
EMAIL_PORT=                (Port to use for the SMTP server defined in EMAIL_HOST)
EMAIL_HOST_USER=           (Username to use for the SMTP server defined in EMAIL_HOST. If empty, Django won’t attempt authentication.)
EMAIL_HOST_PASSWORD=       (Password to use for the SMTP server defined in EMAIL_HOST. 
                           This setting is used in conjunction with EMAIL_HOST_USER when authenticating to the SMTP server.)
EMAIL_USE_TLS=             (Whether to use a TLS (secure) connection when talking to the SMTP server.)
# For create superuser
DJANGO_SUPERUSER_PASSWORD= 
DJANGO_SUPERUSER_EMAIL=
DJANGO_SUPERUSER_USERNAME=
```



__Then__ run docker:

```sh
docker-compose up --build --no-deps
```
