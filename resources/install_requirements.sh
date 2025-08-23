#!/bin/bash

# Ativa o ambiente virtual, se existir
if [ -d ".venv" ]; then
  source .venv/bin/activate
fi

# Instala as dependências do requirements.txt
pip install -r ../requirements.txt