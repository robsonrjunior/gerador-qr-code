# Gerador de QR Code

API simples para gerar QR Codes a partir de um texto ou URL. O serviço recebe o
conteúdo em texto puro e retorna a imagem do QR Code no formato SVG.

## Tecnologias

- Python 3.12+
- FastAPI
- `qrcode`
- Pillow
- uv

## Pré-requisitos

- Python 3.12 ou superior
- [uv](https://docs.astral.sh/uv/)

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone <URL_DO_REPOSITORIO>
cd gerador-qr-code
uv sync
```

O comando `uv sync` cria ou atualiza o ambiente virtual e instala as versões
definidas no `uv.lock`.

## Executando a API

Inicie o servidor de desenvolvimento com:

```bash
uv run --with uvicorn uvicorn gerador_qr_code.main:app --reload --app-dir src
```

Por padrão, a API ficará disponível em `http://127.0.0.1:8000`.

## Uso

Envie o conteúdo desejado no corpo da requisição `POST /qr-code` como
`text/plain`:

```bash
curl -X POST http://127.0.0.1:8000/qr-code \
  -H "Content-Type: text/plain" \
  --data "https://example.com" \
  -o qr-code.svg
```

O arquivo `qr-code.svg` conterá o QR Code gerado. A resposta possui o tipo de
conteúdo `image/svg+xml`.

### Documentação interativa

Com o servidor em execução, acesse:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Estrutura do projeto

```text
.
├── pyproject.toml
├── uv.lock
└── src/
    └── gerador_qr_code/
        ├── __init__.py
        └── main.py
```

O objeto FastAPI está disponível em `gerador_qr_code.main:app` e o endpoint de
geração está implementado em `gerador_qr_code.main:generate_qr_code`.
