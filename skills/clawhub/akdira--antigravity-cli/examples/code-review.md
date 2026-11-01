# Example: Code Review

## Scenario
Perform comprehensive code review focusing on security, performance, and best practices.

## Command

```bash
agy -p "Perform a comprehensive code review of the src/ directory. Analyze:

1. **Security vulnerabilities:**
   - SQL injection
   - XSS attacks
   - Authentication/authorization issues
   - Sensitive data exposure
   - Input validation

2. **Performance issues:**
   - N+1 queries
   - Memory leaks
   - Inefficient algorithms
   - Missing caching opportunities

3. **Code quality:**
   - Code style violations
   - Missing error handling
   - Poor naming conventions
   - Dead code
   - Missing documentation

4. **Best practices:**
   - SOLID principles
   - DRY violations
   - Separation of concerns

For each issue found, provide:
- File path and line number
- Severity (Critical/High/Medium/Low)
- Description of the issue
- Suggested fix with code example

Format output as a structured report." --effort high --add-dir ./src
```

## Expected Output

```markdown
# Code Review Report

## Critical Issues

### 1. SQL Injection Vulnerability
**File:** src/db/users.js:45
**Severity:** Critical
**Description:** User input directly concatenated into SQL query
**Fix:**
\`\`\`javascript
// Before
const query = `SELECT * FROM users WHERE id = ${userId}`;

// After
const query = 'SELECT * FROM users WHERE id = ?';
db.query(query, [userId]);
\`\`\`

## High Issues
...

## Summary
- Critical: 2
- High: 5
- Medium: 12
- Low: 8
```

## Tips

- Use `--effort high` for thorough analysis
- Use `--output-format json` for programmatic processing
- Combine with `--add-dir` for full project context
