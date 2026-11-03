# Example: Code Generation

## Scenario
Generate a complete Python Flask API with CRUD operations.

## Command

```bash
agy -p "Create a Python Flask API with the following requirements:

1. User model with fields: id, username, email, created_at
2. CRUD endpoints:
   - POST /api/users - Create new user
   - GET /api/users - List all users
   - GET /api/users/<id> - Get single user
   - PUT /api/users/<id> - Update user
   - DELETE /api/users/<id> - Delete user
3. Input validation for email format
4. Proper error handling with appropriate HTTP status codes
5. SQLite database for storage
6. Requirements.txt with all dependencies

Provide complete, working code with proper project structure."
```

## Expected Output

The agent will:
1. Create project structure
2. Generate `app.py` with Flask application
3. Generate `models.py` with User model
4. Generate `requirements.txt`
5. Provide setup instructions

## Follow-up

```bash
# Test the generated code
cd generated-project
pip install -r requirements.txt
python app.py
```

## Tips

- Use `--effort high` for more comprehensive code
- Use `--add-dir ./existing-project` to integrate with existing codebase
- Use `--mode accept-edits` to auto-apply generated files
