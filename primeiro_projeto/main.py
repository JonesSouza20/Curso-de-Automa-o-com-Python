import logging
from dotenv import load_dotenv
import os

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Carregar variáveis do .env
load_dotenv()

# Exemplo: variável de ambiente
API_KEY = os.getenv("API_KEY", "sem_chave")

def main():
    logging.info("Iniciando projeto de automação")
    logging.info(f"API_KEY carregada: {API_KEY}")

if __name__ == "__main__":
    main()