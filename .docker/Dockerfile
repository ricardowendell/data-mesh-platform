ARG VARIANT="3.9-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Poetry
ARG POETRY_VERSION="none"
RUN if [ "${POETRY_VERSION}" != "none" ]; then su vscode -c "umask 0002 && pip3 install poetry==${POETRY_VERSION}"; fi

# Install Starship https://starship.rs/ for pretty prompt
RUN curl -fsSL https://starship.rs/install.sh | sh /dev/stdin --yes \
    && echo 'eval "$(starship init zsh)"' >> /root/.zshrc

ENTRYPOINT [".docker/entrypoint.sh"]