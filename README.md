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
1. open: [http://0.0.0.0:8080/flower/tasks](http://0.0.0.0:8080/flower/tasks)

   **table does not load and eventually the request gives back a 500**

log output

```
test_app    | [2022-07-19 19:33:13 +0000] [10] [DEBUG] GET /is_authenticated
test_app    | [2022-07-19 19:33:44 +0000] [1] [CRITICAL] WORKER TIMEOUT (pid:10)
nginx       | 2022/07/19 19:33:45 [error] 33#33: *31 upstream prematurely closed connection while reading response header from upstream, client: 192.168.16.1, server: , request: "POST /flower/tasks/datatable HTTP/1.1", subrequest: "/is_authenticated", upstream: "http://192.168.16.3:5000/is_authenticated", host: "0.0.0.0:8080", referrer: "http://0.0.0.0:8080/flower/tasks"
nginx       | 2022/07/19 19:33:45 [error] 33#33: *31 auth request unexpected status: 502 while sending to client, client: 192.168.16.1, server: , request: "POST /flower/tasks/datatable HTTP/1.1", host: "0.0.0.0:8080", referrer: "http://0.0.0.0:8080/flower/tasks"
nginx       | 192.168.16.1 - - [19/Jul/2022:19:33:45 +0000] "POST /flower/tasks/datatable HTTP/1.1" 500 177 "http://0.0.0.0:8080/flower/tasks" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" "-"
test_app    | [2022-07-19 19:33:45 +0000] [1] [WARNING] Worker with pid 10 was terminated due to signal 9
test_app    | [2022-07-19 19:33:45 +0000] [13] [INFO] Booting worker with pid: 13
```

### 2. without sentry (works)

1. set `dsn` to `None` in `app.py`
1. build again
   ```
   docker-compose build
   ```
1. start containers
   ```
   docker-compose up
   ```
1. open: [http://0.0.0.0:8080/flower/tasks](http://0.0.0.0:8080/flower/tasks)

   **table loads normally**

### 3. with sentry, but without internal auth (works)

1. clear the changes
   ```
   git checkout -- .
   ```
1. remove line 20 in `nginx.conf` (`auth_request /is_authenticated;`)
1. build again
   ```
   docker-compose build
   ```
1. start containers
   ```
   docker-compose up
   ```
1. open: [http://0.0.0.0:8080/flower/tasks](http://0.0.0.0:8080/flower/tasks)

   **table loads normally**
