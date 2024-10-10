# Use official Python image from the DockerHub
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY ./requirements.txt /app/requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy everything to the container
# COPY . .
COPY ./main.py /app/main.py
COPY ./api_v1.py /app/api_v1.py
COPY ./utility_v1.py /app/utility_v1.py

# Add folders as data mount points
ADD data /code/data/
# ADD cred /code/cred/



# -----------------------------------------------
# -----------------------------------------------

# # Use official Python image from the DockerHub
# FROM python:3.9

# # Set working directory inside the container
# WORKDIR /app

# # -----------------------------------------------
# # Common apt commands
# # RUN apt update

# # Few necessary libraries on any Linux system
# # RUN apt-get install ffmpeg libsm6 libxext6  -y
# # RUN apt-get install poppler-utils -y

# # -----------------------------------------------
# # Common pip commands
# # RUN pip install --upgrade pip
# # RUN pip install python-multipart

# # -----------------------------------------------
# # Copy the requirements file to the container
# COPY ./requirements.txt /app/requirements.txt

# # Install the Python dependencies
# RUN pip install --no-cache-dir -r /app/requirements.txt

# # -----------------------------------------------
# # Copy everything to the container
# # COPY . .
# COPY ./api_v1.py /app/api_v1.py
# COPY ./utility_v1.py /app/utility_v1.py


# # -----------------------------------------------
# # Add folders as data mount points
# ADD data /code/data/
# # ADD cred /code/cred/

# # -----------------------------------------------

# # Alternative: If command is not provided in "docker-compose.yml" and "__main__" function is not defined in api script:

# # # Expose the port FastAPI will run on
# # EXPOSE 8000

# # # Command to run the FastAPI app using Uvicorn
# # CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
