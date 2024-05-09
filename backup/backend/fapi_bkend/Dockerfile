FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POSTGRES_USER='postgres'
ENV POSTGRES_PASSWORD='postgres'
ENV POSTGRES_HOST='bmt-postgres'
ENV POSTGRES_DB='bmtbkenddb1'

WORKDIR /app

COPY . .

RUN apt update
RUN python -m pip install --upgrade pip
# RUN apt install cargo -y
RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev
# RUN apt-get update && \
#     apt-get install -y build-essential libssl-dev libffi-dev python3-dev curl && \
#     curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
#     export PATH="$HOME/.cargo/bin:$PATH" && \
#     rustup default stable
# Install system dependencies

# RUN apt-get update && \
#     apt-get install -y build-essential libssl-dev libffi-dev python3-dev curl && \
#     curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
#     export PATH="$HOME/.cargo/bin:$PATH" && \
#     rustup default stable

# Set PATH environment variable
ENV PATH="/root/.cargo/bin:${PATH}"

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

EXPOSE 8005

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8005" ]