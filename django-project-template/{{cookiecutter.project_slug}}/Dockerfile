{% if cookiecutter.use_tailwind %}
FROM rust AS volta-build
WORKDIR /src
RUN git clone https://github.com/volta-cli/volta.git /src
RUN git checkout tags/v2.0.2
RUN cargo build
RUN ls /src/target/debug
{% endif %}
FROM python:slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_PROJECT_ENVIRONMENT=/venv

# Set working directory
WORKDIR /app

# Copy project
COPY . /app/

RUN uv lock


{%- if cookiecutter.use_tailwind %}
# Copy over Volta binaries
RUN mkdir -p /root/.volta/bin
COPY --from=volta-build /src/target/debug/volta /root/.volta/bin
COPY --from=volta-build /src/target/debug/volta-migrate /root/.volta/bin
COPY --from=volta-build /src/target/debug/volta-shim /root/.volta/bin

# shell stuff for volta
SHELL ["/bin/bash", "-c"]
ENV BASH_ENV=~/.bashrc
ENV VOLTA_HOME=/root/.volta
ENV PATH=$VOLTA_HOME/bin:$PATH
RUN ln -s /root/.volta/bin/volta-shim /root/.volta/bin/node 
RUN ln -s /root/.volta/bin/volta-shim /root/.volta/bin/npm 
RUN ln -s /root/.volta/bin/volta-shim /root/.volta/bin/npx
RUN ln -s /root/.volta/bin/volta-shim /root/.volta/bin/pnpm 
RUN ln -s /root/.volta/bin/volta-shim /root/.volta/bin/yarn

# node installation
RUN volta install node
#RUN node -v && npm -v
RUN npm install
{%- endif %}

# generate front end assets
{%- if cookiecutter.use_tailwind %}
RUN uv run manage.py tailwind install
RUN uv run manage.py tailwind build
{%- endif %}
RUN uv run manage.py collectstatic --no-input

CMD uv run manage.py runserver 0.0.0.0:8000

{%- if cookiecutter.use_tailwind %}
# clean up
RUN rm -rf /app/node_modules
{%- endif %}
