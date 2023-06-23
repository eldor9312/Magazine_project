# This is project based on Django for magazine news and articles
This project has:
 * user authorization 
 * ability to send emails 
 * Timezones
 * Translation abilities
 * logs and much more
---
## How to start
1. Download all files and requirements
2. Create accounts in redis and celery
3. Change next things in settings.py:  
   *  ```
      SECRET_KEY = '#' #it is private for everyone
      ```
   * ````
     LANGUAGE_CODE = 'ru' #change for the language you are planning to use as main
     ````
   * ```
     DEFAULT_FROM_EMAIL = "##" #your full email
     EMAIL_HOST = 'smtp.yandex.ru'  # server adress of Yandex is the same for everyone
     EMAIL_PORT = 465  # port smtp is also the same
     EMAIL_HOST_USER = '###'  # username, if your email is user@gmail.com just write everything from it before @
     EMAIL_HOST_PASSWORD = '###'  # password from email
     EMAIL_USE_SSL = True
     ```
   * ```
     CELERY_BROKER_URL ='##' #change to yours
     CELERY_RESULT_BACKEND = '##' #change to yours
     ```
     
