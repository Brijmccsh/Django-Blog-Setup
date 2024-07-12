# first-principles-publishing-take-home

# Flask Blog API

A simple RESTful API for a blogging platform built with Flask. Features user authentication, CRUD operations for blog posts, and SQLite database integration.

## Quick Start

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies: `pip install flask flask-sqlalchemy flask-jwt-extended pytest`
4. Run the application: `python run.py`
5. Test the API using Postman(refer to postman collection)

## API Endpoints

- POST /signup - Create a new user
- POST /login - Authenticate and receive JWT
- GET /posts - Retrieve all posts
- POST /posts - Create a new post (requires authentication)
- GET /posts/<id> - Retrieve a specific post
- PUT /posts/<id> - Update a post (requires authentication)
- DELETE /posts/<id> - Delete a post (requires authentication)

---

## Design Principles & Trade-offs

1. **Simplicity**: Chose Flask for its lightweight nature and ease of use.
   Trade-off: May lack some built-in features of larger frameworks.

2. **SQLite**: Used for simplicity and portability.
   Trade-off: May not scale well for high-traffic applications.

3. **JWT Authentication**: Stateless authentication for API security.
   Trade-off: Requires secure storage and transmission of tokens.

4. **Modular Structure**: Separated concerns (routes, models, auth) for maintainability.
   Trade-off: Slightly more complex file structure for a small project.

---

## Future Improvements

- Input validation
- Pagination for post listing
- User roles and permissions
- API rate limiting
- Swagger documentation

---
