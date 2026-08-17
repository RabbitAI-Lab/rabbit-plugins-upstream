---
name: pytest-generator-pro
version: "1.0.0"
category: testing
tags:
  - testing
  - pytest
  - python
  - unit-test
  - fixture
  - mock
  - coverage
  - tdd
model: claude-sonnet-4-20250514
trigger_keywords:
  - pytest
  - test generator
  - unit test
  - test coverage
  - fixture
  - mock
  - test suite
  - Python testing
  - conftest
  - parametrize
  - coverage report
pricing: "$7.99 one-time"
---

# pytest Test Generator Pro

> **Framework-aware pytest test generation that matches your team's conventions.** Auto-detects fixtures, mocking patterns, naming conventions, and test structure from existing tests — generates comprehensive tests with edge cases, parametrization, and coverage gaps.

## Why This Skill Exists

Generic AI test generation produces tests that don't match your project's conventions, miss edge cases, and fail to use existing fixtures. This skill reads your existing test suite, learns your patterns, and generates tests that look like your team wrote them.

## When to Activate

Activate when the user:
- Asks to generate tests, write tests, or add test coverage
- Mentions pytest, conftest, fixtures, parametrize, or coverage
- Says "test this function" or "what edge cases am I missing"
- Runs pytest and wants to improve coverage
- Creates a new Python module and needs tests

## Workflow

### Step 1: Learn Project Conventions

Scan existing test files to learn:
- **Naming**: `test_*` vs `*_test`, class-based vs function-based
- **Fixture patterns**: shared fixtures in conftest.py, factory patterns, builder patterns
- **Mocking style**: `unittest.mock`, `pytest-mock` (mocker fixture), `responses`, `httpx-mock`
- **Assertion style**: plain `assert` vs `pytest.raises` vs `assertthat`
- **Parametrization**: how existing tests use `@pytest.mark.parametrize`
- **Markers**: custom markers (`@pytest.mark.slow`, `@pytest.mark.integration`)
- **Coverage config**: `.coveragerc`, `pytest.ini`, `pyproject.toml [tool.pytest]`
- **Import style**: relative vs absolute, `from app import` vs `from src.app import`

Output: Convention summary (stored for this session)

### Step 2: Analyze Target Code

For each function/class to test:
- Parse signature: parameters, types, return type, defaults, *args/**kwargs
- Identify external dependencies: DB calls, HTTP requests, file I/O, env vars, time
- Map decision branches: if/else, try/except, loops, early returns
- Identify edge cases: None, empty string, empty list, negative numbers, unicode, very large inputs
- Detect async: `async def` requires `pytest-asyncio`
- Detect dataclasses/Pydantic models: need valid construction

### Step 3: Generate Test Suite

For each function, generate:

#### A. Happy Path Tests
```python
def test_create_user_creates_user_with_valid_data(db_session):
    """Creating a user with valid data returns a User object."""
    user = create_user(email="test@example.com", name="Test User")
    
    assert user.id is not None
    assert user.email == "test@example.com"
    assert user.name == "Test User"
    assert user.created_at is not None
```

#### B. Edge Case Tests
```python
@pytest.mark.parametrize("email,expected_valid", [
    ("user@example.com", True),
    ("user.name+tag@example.com", True),
    ("", False),
    (None, False),
    ("not-an-email", False),
    ("a" * 500 + "@example.com", False),  # Too long
    ("user@example.com", True),
    ("用户@例子.com", True),  # Unicode
])
def test_validate_email_handles_edge_cases(email, expected_valid):
    assert validate_email(email) == expected_valid
```

#### C. Error/Exception Tests
```python
def test_create_user_raises_on_duplicate_email(db_session):
    """Creating a user with existing email raises DuplicateEmailError."""
    create_user(email="test@example.com", name="First User")
    
    with pytest.raises(DuplicateEmailError) as exc_info:
        create_user(email="test@example.com", name="Second User")
    
    assert "already exists" in str(exc_info.value)
```

#### D. Mock External Dependencies
```python
def test_send_welcome_email_calls_email_service(mocker):
    """send_welcome_email calls EmailService.send with correct params."""
    mock_send = mocker.patch("app.services.email.EmailService.send")
    
    send_welcome_email(user_id=123, email="test@example.com", name="Test")
    
    mock_send.assert_called_once_with(
        to="test@example.com",
        template="welcome",
        context={"name": "Test", "user_id": 123},
    )
```

#### E. Fixtures (if needed)
```python
@pytest.fixture
def sample_user(db_session):
    """Create a test user for tests that need an existing user."""
    return create_user(email="fixture@example.com", name="Fixture User")

@pytest.fixture
def auth_client(client, sample_user):
    """API client with authentication headers for sample_user."""
    token = generate_token(sample_user.id)
    client.headers.update({"Authorization": f"Bearer {token}"})
    return client
```

### Step 4: Coverage Gap Analysis

After generating tests, identify:
- Which branches are now covered
- Which branches are still uncovered
- Which edge cases are impossible to test (require integration)
- Recommend: integration tests vs unit tests for remaining gaps

Output:
```markdown
## Coverage Analysis

| Function | Branches | Covered | Gaps |
|----------|----------|---------|------|
| create_user | 8 | 7 | Error path when DB connection fails (integration) |
| validate_email | 12 | 12 | ✅ Fully covered |
| send_welcome_email | 5 | 4 | Retry logic on timeout (needs async mock) |
```

### Step 5: Generate conftest.py Additions

If new shared fixtures are needed:
```python
# conftest.py additions
import pytest
from app.test_factories import UserFactory, ProductFactory

@pytest.fixture
def db_session():
    """Rollback-only DB session for test isolation."""
    session = create_test_session()
    yield session
    session.rollback()
    session.close()

@pytest.fixture
def factory():
    """Access to test data factories."""
    return FactoryContainer(UserFactory, ProductFactory)
```

## Output Constraints

- Match existing project naming conventions exactly
- Every test function must have a docstring explaining what it tests and why
- Use `mocker` (pytest-mock) if project uses it, otherwise use `unittest.mock`
- Parametrize edge cases instead of writing 10 separate test functions
- Never test implementation details (private methods, internal state) — test behavior
- Async tests must use `@pytest.mark.asyncio`
- Test file goes in mirror directory: `src/app/users.py` → `tests/app/test_users.py`

## What This Skill Does NOT Do

- Does not run tests (generates code only)
- Does not test non-Python code
- Does not generate integration tests for external services (recommends them)
- Does not modify production code to make it testable (suggests refactors)
