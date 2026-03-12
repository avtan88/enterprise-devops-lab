FROM enterprise/python-runtime:1.0.1

WORKDIR /app

COPY --chown=appuser:appuser requirements.txt /app/requirements.txt
RUN python3 -m pip install --no-cache-dir --user -r /app/requirements.txt

COPY --chown=appuser:appuser app/ /app/

ENV PATH="/home/appuser/.local/bin:${PATH}"

EXPOSE 8080

CMD ["python3", "/app/app.py"]
