FROM python:3.11-bullseye as base

# This flag is important to output python logs correctly in docker!
ENV PYTHONUNBUFFERED 1
# Flag to optimize container size a bit by removing runtime python cache
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /code


FROM base as dep-venv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


RUN pip install playwright fastapi uvicorn && playwright install --with-deps

COPY ./src .

EXPOSE 9000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]
