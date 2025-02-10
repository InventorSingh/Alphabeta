This project demonstrate Security Example where client has no Security related code.

Everything is independet of the client and everything is handled at the backend. 

Run it below to start the demo!


### How to Run It (Do not change in any way unelss reviewed in a PR)

1. In the root folder of the code, run:
    ```sh
    docker compose up
    ```

2. In `authorization-service`, run:
    ```sh
    ./run.sh
    ```

3. In `gateway`, run:
    ```sh
    ./run.sh
    ```

4. In `api`, run:
    ```sh
    ./run.sh
    ```

5. In `processor` (optional), run:
    ```sh
    ./run.sh
    ```

6. In `static`, run:
    ```sh
    ./run.sh
    ```

7. Visit [http://127.0.0.1:8082](http://127.0.0.1:8082) (important: use the IP, not localhost!) in the browser.

8. Login with `preet/password`.

# 