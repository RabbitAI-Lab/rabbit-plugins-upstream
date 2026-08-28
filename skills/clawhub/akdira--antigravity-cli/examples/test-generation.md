# Example: Test Generation

## Scenario
Generate comprehensive unit tests for a validation module.

## Command

```bash
agy -p "Generate comprehensive unit tests for src/utils/validation.js

Requirements:
1. Use Jest testing framework
2. Cover all exported functions
3. Include test cases for:
   - Happy path (valid inputs)
   - Edge cases (empty strings, null, undefined)
   - Error conditions (invalid inputs)
   - Boundary values
4. Aim for 90%+ code coverage
5. Use descriptive test names
6. Group related tests with describe blocks
7. Include setup/teardown if needed

For each function, generate:
- At least 5 test cases
- Both positive and negative tests
- Edge case handling

Save tests to tests/utils/validation.test.js" --add-dir ./src --add-dir ./tests
```

## Expected Output

```javascript
// tests/utils/validation.test.js

const {
  validateEmail,
  validatePassword,
  validatePhoneNumber,
  validateDate
} = require('../../src/utils/validation');

describe('Validation Utilities', () => {
  
  describe('validateEmail', () => {
    test('accepts valid email', () => {
      expect(validateEmail('user@example.com')).toBe(true);
    });
    
    test('rejects email without @', () => {
      expect(validateEmail('userexample.com')).toBe(false);
    });
    
    test('rejects email without domain', () => {
      expect(validateEmail('user@')).toBe(false);
    });
    
    test('rejects empty string', () => {
      expect(validateEmail('')).toBe(false);
    });
    
    test('rejects null', () => {
      expect(validateEmail(null)).toBe(false);
    });
    
    test('rejects undefined', () => {
      expect(validateEmail(undefined)).toBe(false);
    });
    
    test('accepts email with subdomain', () => {
      expect(validateEmail('user@mail.example.com')).toBe(true);
    });
    
    test('rejects email with spaces', () => {
      expect(validateEmail('user @example.com')).toBe(false);
    });
  });
  
  describe('validatePassword', () => {
    test('accepts strong password', () => {
      expect(validatePassword('Str0ng!Pass#123')).toBe(true);
    });
    
    test('rejects password without uppercase', () => {
      expect(validatePassword('weakpass123!')).toBe(false);
    });
    
    test('rejects password without number', () => {
      expect(validatePassword('WeakPassword!')).toBe(false);
    });
    
    test('rejects password without special char', () => {
      expect(validatePassword('WeakPassword123')).toBe(false);
    });
    
    test('rejects short password', () => {
      expect(validatePassword('Sh0rt!')).toBe(false);
    });
    
    test('rejects empty password', () => {
      expect(validatePassword('')).toBe(false);
    });
  });
  
  // ... more tests
});
```

## Run Tests

```bash
# Run specific test file
npm test -- tests/utils/validation.test.js

# Run with coverage
npm test -- --coverage

# Watch mode
npm test -- --watch
```

## Tips

- Use `--effort high` for comprehensive test coverage
- Provide existing test examples if any
- Specify testing framework (Jest, Mocha, etc.)
- Ask for both unit and integration tests if needed
- Use `--add-dir` to provide full project context
