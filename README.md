### 1. with sentry (does not work)

1. add sentry `dsn` to `app.py`

1. build and pull images
   ```
   docker-compose build
   ```
1. start containers
   ```
   docker-compose up
   ```
1. open: [http://0.0.0.0:8080/](http://0.0.0.0:8080/)

   **table does not load and eventually the request gives back a 500**

log output

```
nginx    | 2022/07/20 14:14:41 [notice] 1#1: start worker process 29
app      | [2022-07-20 14:14:56 +0000] [7] [DEBUG] GET /
nginx    | 172.21.0.1 - - [20/Jul/2022:14:14:56 +0000] "GET / HTTP/1.1" 200 1001 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" "-"
app      | [2022-07-20 14:14:57 +0000] [7] [DEBUG] GET /is_authenticated
nginx    | 172.21.0.1 - - [20/Jul/2022:14:14:58 +0000] "POST /ajax_route HTTP/1.1" 499 0 "http://0.0.0.0:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" "-"
app      | [2022-07-20 14:14:58 +0000] [7] [DEBUG] Ignoring EPIPE
```

### 2. without sentry (works)

1. set `dsn` to `None` in `app.py`
1. (re)start containers
   ```
   docker-compose up
   ```
1. open: [http://0.0.0.0:8080/](http://0.0.0.0:8080/)

   **table loads normally**

### 3. with sentry, but without internal auth (works)

1. set the `dsn` back to a proper url
1. remove/comment out line 21 in `nginx.conf` (`auth_request /is_authenticated;`)
1. (re)start containers
   ```
   docker-compose up
   ```
1. open: [http://0.0.0.0:8080/](http://0.0.0.0:8080/)

   **table loads normally**
