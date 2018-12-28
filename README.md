# pyrweb
Poor Yorick

## Preparing
```sh
$ pip3 install -r requirements.txt
```

## Run
```sh
$ python3 yorick.py
```

## Test upload API
```sh 
$ curl -H "Content-type: application/json" -d '{"comand" :"play_song","url":"http://next.2yxa.mobi/users/2yxa_ru_speak_imp396692_774694.mp3" }' '127.0.0.1:8080/upload_by_url'
```