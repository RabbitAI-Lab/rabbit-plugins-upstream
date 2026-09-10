# Reproducible professional docking/simulation container.
# Build:
#   docker build -t pro-docking-full .
# Run:
#   docker run --rm -it -v "$PWD:/work" pro-docking-full bash
FROM mambaorg/micromamba:1.5.10
COPY --chown=$MAMBA_USER:$MAMBA_USER environment_full.yml /tmp/environment_full.yml
RUN micromamba env create -y -f /tmp/environment_full.yml && \
    micromamba clean --all --yes
SHELL ["/usr/local/bin/_entrypoint.sh", "/bin/bash", "-c"]
RUN echo "micromamba activate pro-docking-full" >> ~/.bashrc
WORKDIR /work
