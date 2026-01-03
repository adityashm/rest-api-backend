# REST API Backend with Authentication

A production-ready REST API built with FastAPI featuring JWT authentication, SQLite database, and comprehensive API documentation.

## Features

- 🔐 **JWT Authentication** - Secure token-based authentication
- 👤 **User Management** - Register, login, and user profiles
- 📦 **Product Management** - CRUD operations for products
- 🛒 **Order System** - Create and manage orders
- 📖 **Auto Documentation** - Interactive Swagger and ReDoc docs
- ✅ **Unit Tests** - Comprehensive test coverage
- 🔒 **Password Hashing** - bcrypt password security
- 🗄️ **SQLAlchemy ORM** - Modern database operations
- 🚀 **Production Ready** - CORS, logging, error handling

## Tech Stack

- **Framework**: FastAPI
- **Server**: Uvicorn
- **Database**: SQLite + SQLAlchemy
- **Authentication**: JWT (python-jose)
- **Validation**: Pydantic
- **Testing**: Pytest

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/adityashm/rest-api-backend.git
   cd rest-api-backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**
   ```bash
   python main.py
   # or with uvicorn
   uvicorn main:app --reload
   ```

5. **Access API**
   - API: `http://localhost:8000`
   - Docs: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login and get JWT token

### Products
- `GET /products` - List all products
- `GET /products/{id}` - Get product details
- `POST /products` - Create product (authenticated)
- `PUT /products/{id}` - Update product (authenticated)
- `DELETE /products/{id}` - Delete product (authenticated)

### Orders
- `GET /orders` - Get user orders (authenticated)
- `POST /orders` - Create order (authenticated)

### Health
- `GET /health` - API health check

## Example Usage

### Register User
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "aditya",
    "email": "aditya@example.com",
    "password": "securepass123",
    "full_name": "Aditya Sharma"
  }'
```

### Login
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "aditya",
    "password": "securepass123"
  }'
```

### Create Product (with token)
```bash
curl -X POST "http://localhost:8000/products" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop",
    "description": "High-performance laptop",
    "price": 999.99,
    "quantity": 10
  }'
```

## Project Structure

```
rest-api-backend/
├── main.py           # Main FastAPI application
├── models.py         # SQLAlchemy models
├── schemas.py        # Pydantic schemas
├── auth.py          # Authentication logic
├── test_main.py     # Unit tests
├── requirements.txt # Dependencies
└── README.md        # Documentation
```

## Running Tests

```bash
pytest test_main.py -v
```

## Environment Variables

Create `.env` file:
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///./api.db
```

## Database Models

### User
- id, username, email, hashed_password, full_name, disabled, created_at

### Product
- id, name, description, price, quantity, created_at, updated_at

### Order
- id, user_id, product_id, quantity, total_price, status, created_at

## Deployment

### Docker
```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Run Docker
```bash
docker build -t rest-api .
docker run -p 8000:8000 rest-api
```

### Deploy to Railway/Render
1. Push code to GitHub
2. Connect repository to Railway/Render
3. Set environment variables
4. Deploy

## Security Considerations

- ✅ Passwords hashed with bcrypt
- ✅ JWT tokens with expiration
- ✅ CORS configured
- ✅ SQL injection protection via ORM
- ✅ Input validation with Pydantic
- ⚠️ Change SECRET_KEY in production
- ⚠️ Use HTTPS in production

## License

MIT License

## Author

Aditya Sharma
- GitHub: https://github.com/adityashm
- Portfolio: https://adityashm.me
