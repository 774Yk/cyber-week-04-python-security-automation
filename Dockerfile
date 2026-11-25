FROM python:3.12-slim
WORKDIR /lab
COPY secauto ./secauto
COPY tools ./tools
COPY sample-data ./sample-data
USER 65532:65532
CMD ["python", "-m", "secauto.cli", "sample-data"]
