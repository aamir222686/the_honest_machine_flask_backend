# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory to "app"
WORKDIR /app

# Copy the requirements.txt file to the image
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the files in the current directory to the image
COPY . .

ENV PORT=8080

EXPOSE 8080

# Command to run when the container starts docker build -t aamir222686/thm_server:1.0 .   || docker run -p 8080:8080 --env-file=.env
CMD ["uvicorn", "main:app", "--port", "8080", "--host", "0.0.0.0"]