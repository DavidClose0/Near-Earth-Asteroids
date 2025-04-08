# Use the official Python 3.10.2 image as the base
FROM python:3.10.2

# Copy everything not excluded by .dockerignore into the container directory /app
COPY . /app

# Set the working directory for the application
WORKDIR /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose default Streamlit port
EXPOSE 8501

# Define the default command to run when the container starts
CMD ["streamlit", "run", "src/app.py"]