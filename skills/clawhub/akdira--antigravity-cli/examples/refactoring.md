# Example: Refactoring

## Scenario
Refactor authentication module from session-based to JWT tokens.

## Command

```bash
cd /path/to/project

agy -p "Refactor the authentication system from session-based to JWT tokens:

Current implementation:
- Session stored in database
- Middleware checks session validity
- Login/logout endpoints exist

Requirements:
1. Replace session storage with JWT tokens
2. Update middleware to validate JWT
3. Add token refresh mechanism
4. Update all tests to work with JWT
5. Maintain backward compatibility during transition
6. Add proper error handling for expired/invalid tokens

Files to modify:
- src/auth/middleware.js
- src/auth/controller.js
- src/auth/service.js
- src/models/session.js → src/models/token.js
- tests/auth/*.test.js

Keep the same API interface. Generate migration script for existing sessions." --mode accept-edits --add-dir ./src --add-dir ./tests
```

## Expected Workflow

1. Agent analyzes current implementation
2. Proposes refactoring plan
3. Modifies files one by one
4. Updates tests
5. Generates migration script
6. Provides summary of changes

## Verification

```bash
# Run tests
npm test

# Check for breaking changes
npm run lint

# Manual testing
curl -X POST http://localhost:3000/login -d '{"email":"test@example.com","password":"test"}'
```

## Tips

- Use `--mode accept-edits` to auto-apply changes
- Use `--mode plan` first to see proposed changes without applying
- Use `--effort high` for complex refactoring
- Always run tests after refactoring
