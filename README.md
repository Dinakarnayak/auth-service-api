
# auth-service-api

## Introduction
The `auth-service-api` is a backend authentication service API that provides authentication functionality for user login, registration, and session management. It supports JWT-based authentication and integrates with various third-party services.

## Features
- **User login and registration**: Endpoints to authenticate and register users.
- **JWT authentication**: Secure authentication using JWT tokens.
- **Password hashing**: Secure storage of user passwords with hashing techniques.
- **Token-based authorization**: Authorization via JWT tokens for protected routes.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/auth-service-api.git
   ```

2. Navigate into the project directory:
   ```bash
   cd auth-service-api
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

## Usage

1. Start the server:
   ```bash
   npm start
   ```

   The API will be running on `http://localhost:3000`.

## API Endpoints

- **POST /login**: Login with email and password.
  - Request body:
    ```json
    {
      "email": "user@example.com",
      "password": "your-password"
    }
    ```
  - Response:
    ```json
    {
      "token": "JWT_TOKEN"
    }
    ```

- **POST /register**: Register a new user.
  - Request body:
    ```json
    {
      "email": "user@example.com",
      "password": "your-password"
    }
    ```
  - Response:
    ```json
    {
      "message": "User registered successfully."
    }
    ```

- **GET /user**: Get the current authenticated user's details.
  - Request headers:
    ```json
    {
      "Authorization": "Bearer JWT_TOKEN"
    }
    ```
  - Response:
    ```json
    {
      "id": 1,
      "email": "user@example.com",
      "createdAt": "2025-02-07T10:00:00Z"
    }
    ```

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them.
4. Create a pull request with a description of the changes you made.

