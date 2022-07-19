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
