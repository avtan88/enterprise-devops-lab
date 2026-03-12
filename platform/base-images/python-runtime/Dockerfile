FROM amazonlinux:2023

LABEL maintainer="platform-team" \
      org.opencontainers.image.title="enterprise-python-runtime" \
      org.opencontainers.image.description="Approved Python runtime base image for enterprise services" \
      org.opencontainers.image.version="1.0.0"

RUN dnf install -y python3 shadow-utils ca-certificates && \
    dnf clean all && \
    rm -rf /var/cache/dnf

RUN useradd --create-home --shell /sbin/nologin --uid 10001 appuser && \
    mkdir -p /app && \
    chown -R appuser:appuser /app

WORKDIR /app

USER appuser
