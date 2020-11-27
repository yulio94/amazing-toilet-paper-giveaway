FROM python:3.8

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1

# Upgrade pip and install pipenv
RUN pip install --upgrade pip \
    && pip install pipenv


# Copy requirements file (Pipfile)
COPY ["./backend/Pipfile", "./backend/Pipfile.lock", "./"]

# Install project dependencies
RUN pipenv install --system --deploy

# Copy project files
COPY ./backend/ ./

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
