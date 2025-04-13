# Thai Address Parser API

A FastAPI-based API for parsing Thai addresses using the thaiaddress library.

## Features

- Simple REST API for parsing Thai addresses
- Docker and Docker Compose support for easy deployment
- Returns structured data from Thai address text

## Getting Started

### Prerequisites

- Docker and Docker Compose

### Running the API

1. Clone this repository
2. Build and start the Docker container:

```bash
docker-compose up -d
```

3. The API will be available at http://localhost:8000

## API Usage

### Parse an address

**Endpoint:** `POST /parse`

**Request Body:**

```json
{
  "text": "นายปรายุ้ด จันทร์กะเพรา 099-999-9999 25/25 ถ.พุทธมณฑล สาย 4 ต. ศาลายา อ.พุทธมณฑล จ.นครปฐม 73170"
}
```

**Response:**

```json
{
  "text": "นายปรายุ้ด จันทร์กะเพรา 099-999-9999 25/25 ถ.พุทธมณฑล สาย 4 ต. ศาลายา อ.พุทธมณฑล จ.นครปฐม 73170",
  "name": "นายปรายุ้ด จันทร์กะเพรา",
  "address": "25/25 ถ.พุทธมณฑล สาย 4",
  "location": "ต. ศาลายา อ.พุทธมณฑล จ.นครปฐม",
  "subdistrict": "ศาลายา",
  "district": "พุทธมณฑล",
  "province": "นครปฐม",
  "postal_code": "73170",
  "phone_number": "0999999999",
  "email": ""
}
```

## Testing

You can test the API using the included `test_api.py` script:

```bash
# Make sure the API is running
python test_api.py
```

## API Documentation

FastAPI automatically generates interactive API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [thaiaddress](https://github.com/425degree-developers/thaiaddress) - Thai address parsing library
- [Docker](https://www.docker.com/) - Containerization
