FROM python:3.8

# These should generally not change unless you know exactly what you're doing.
ENV APP_HOST "0.0.0.0"
ENV APP_PORT "5000"
ENV FLASK_APP "rslequip.py"
ENV DATA_PATH "/config"

# These are default values to get the container working for Development.
# You should override these for production use.
ENV DATABASE_URL "sqlite:///test.db"
ENV SECRET_KEY "Your secret is Safe"
ENV WTF_CSRF_SECRET_KEY "This is a REALLY safe secret"
ENV GOOGLE_OAUTH_CLIENT_ID "Get a Google Client ID"
ENV GOOGLE_OAUTH_CLIENT_SECRET_ID "Also get a Google Client Secret ID"

# Install Requirements and prepare 
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN chmod +x start_rslequip.sh

# Kick off the whole process
CMD ./start_rslequip.sh
