# End-to-End Service Setup

## A. Set Up a Conda Environment

1. Follow basic conda commands for environment management [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
2. Create and activate a new conda environment:

    ```bash
    conda create -n end-to-end python=3.9
    conda activate end-to-end
    ```

## B. Write Basic Functionality

1. **Always use functions for repetitive tasks.**
2. Create two scripts:

    - **main.py**: Holds the main functionality and calls the necessary functions from `utility_v1.py`.
    - **utility_v1.py**: Contains reusable functions.

## C. Create the API

1. Install required libraries:

    ```bash
    pip install fastapi uvicorn
    ```

2. Create an API script with a POST endpoint and functionality to process input and return a JSON response.

3. Example of API startup:

    ```bash
    uvicorn api_v1:app --reload
    ```

    Or, include the following in your script:

    ```python
    if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=5001)
    ```

    Run the script:

    ```bash
    python api_v1.py
    ```

4. **Test the API**:

    Using curl:

    ```bash
    curl -X 'POST' 'http://127.0.0.1:5001/echo/' -H 'Content-Type: application/json' -d '{"message": "Hello World"}'
    ```

    Or use Postman.

## D. Dockerization

1. Export the environment libraries:

    ```bash
    conda list --export > requirements.txt
    ```

2. **Clean unnecessary library versions** in `requirements.txt` (recommended).

3. **Dockerize the application**:

    - **Dockerfile**: Copy necessary files and set up the environment.
    - **docker-compose.yml**: Automate Docker setup and start the service.

4. Build and run the service:

    ```bash
    docker-compose build
    docker-compose up -d
    ```

    Or combine the steps:

    ```bash
    docker-compose up -d --build
    ```

5. **Check container logs**:

    ```bash
    docker logs <container_id>
    ```

    Example:

    ```bash
    docker logs 07c91a7f6c40
    ```

6. **Test using curl** or Postman as mentioned in step **C**.

## E. Access and Interact with the Docker Container

1. **List running containers**:

    ```bash
    docker ps
    ```

2. **Access the container shell**:

    ```bash
    docker exec -it <container_id> /bin/bash
    ```

    Example:

    ```bash
    docker exec -it 07c91a7f6c40 /bin/bash
    ```

3. **Run Python scripts inside the container**:

    ```bash
    python main.py
    ```

4. **Run one-time commands** without entering the container shell:

    ```bash
    docker exec <container_id> python main.py
    ```
