# https://hub.docker.com/r/rasa/rasa-sdk/tags
FROM rasa/rasa-sdk:2.3.1

COPY data /app/data

USER root
RUN pip install --upgrade pip

RUN useradd -ms /bin/bash admin
RUN chown -R admin:admin /app
RUN chmod 755 /app
USER admin
CMD ["start", "--actions", "actions"]
