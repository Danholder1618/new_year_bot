
# Use the official Python image
FROM python:3.10-slim

# Copy the requirements file
COPY requirements.txt /requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r /requirements.txt

# Copy the bot script and images
COPY . .

# Set the command to run the bot
CMD ["python", "bot.py"]