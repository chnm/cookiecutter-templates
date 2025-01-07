FROM python:{{ cookiecutter.python_min_version }}

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy project
COPY . /app/

# Install dependencies with Poetry
RUN pip3 install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root

# generate front end assets
RUN poetry run python manage.py collectstatic --no-input
