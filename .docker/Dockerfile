ARG VARIANT="3.9-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Poetry
ARG POETRY_VERSION="none"
RUN if [ "${POETRY_VERSION}" != "none" ]; then su vscode -c "umask 0002 && pip3 install poetry==${POETRY_VERSION}"; fi

# Install Starship https://starship.rs/ for pretty prompt
RUN curl -fsSL https://starship.rs/install.sh | sh /dev/stdin --yes \
    && echo 'eval "$(starship init zsh)"' >> /root/.zshrc

# Install the Pulumi SDK, including the CLI and language runtimes.
RUN curl -fsSL https://get.pulumi.com/ | bash -s -- --version $PULUMI_VERSION && \
  mv ~/.pulumi/bin/* /usr/bin

# Install Terraform
ENV TERRAFORM_VERSION=1.3.3
RUN wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
RUN unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin
RUN terraform --version

ENTRYPOINT [".docker/entrypoint.sh"]