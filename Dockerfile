# Imagem base leve com Python 3.11
FROM python:3.11-slim

# Pasta de trabalho dentro do container
WORKDIR /app

# Envia a saída do Python direto para o terminal, sem buffer
ENV PYTHONUNBUFFERED=1

# Fuso horário usado na validação da data limite
ENV TZ=America/Sao_Paulo

# Copia apenas o código da aplicação para a imagem
COPY src/ /app/src/

# Comando executado ao iniciar o container
CMD ["python", "src/main.py"]
