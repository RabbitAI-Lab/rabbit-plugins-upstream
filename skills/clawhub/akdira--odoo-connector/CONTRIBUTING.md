# Contributing to Odoo Connector

Thank you for your interest in contributing to the Odoo Connector skill. This document explains how to contribute effectively and what guidelines we follow.

## How to Contribute

### Reporting Issues

If you find a bug, error, or missing feature:

1. Check existing issues first — your problem may already be reported
2. Open a new issue with:
   - Odoo version you are using (17, 18, or 19)
   - Complete error message and stack trace
   - Minimal reproduction steps (code that triggers the error)
   - Expected behavior vs actual behavior

### Submitting Changes

1. Fork the repository
2. Create a feature branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes following the guidelines below
4. Test thoroughly — ensure your changes work with at least one Odoo version
5. Commit with a clear message explaining what and why:
   ```bash
   git commit -m "Add support for account.payment batch operations

   Previously, only single payments could be created via XML-RPC.
   This adds batch create support for bulk payment imports."
   ```
6. Push to your fork and open a pull request

## Documentation Guidelines

### Writing Style

- Use clear, simple English
- Assume the reader is a developer familiar with Python but possibly new to Odoo
- Include code examples for every new concept
- Explain the "why" not just the "how"

### Code Examples

All code examples must:

- Be runnable as-is (no missing imports or variables)
- Use only Python standard library (no `pip install` requirements)
- Include brief comments explaining non-obvious parts
- Follow consistent naming conventions

```python
# Good: Self-contained example
import xmlrpc.client

models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")

# Search for active customers
customers = models.execute_kw(
    db, uid, password,
    'res.partner', 'search_read',
    [[('customer_rank', '>', 0)]],
    {'fields': ['name', 'email'], 'limit': 10}
)
```

### Adding New Models

When documenting a new Odoo model:

1. Add the model to the [API Reference](docs/api-reference.md)
2. Include all key fields with types and descriptions
3. List model-specific methods (like `action_confirm` on sale orders)
4. Provide at least one practical code example
5. Note any version-specific field differences

### Adding New Examples

New examples should:

- Solve a real business problem (not just demonstrate API calls)
- Include complete, runnable code
- Explain prerequisites (modules, data, permissions)
- Cover common error cases and how to handle them
- Be placed in the `examples/` directory with a descriptive filename

## Testing

Before submitting, verify:

- [ ] Code examples run without errors (with valid Odoo credentials)
- [ ] Field names match actual Odoo model fields
- [ ] No credentials, passwords, or API keys appear in any file
- [ ] Markdown formatting renders correctly
- [ ] Cross-references between documents are correct

### Manual Testing

Test against a real Odoo instance when possible:

```bash
# Set up test environment
export ODOO_URL="https://test.odoo.com"
export ODOO_DB="test_db"
export ODOO_USERNAME="test_user"
export ODOO_PASSWORD="****"

# Run connection test
python3 scripts/test-connection.py
```

If you do not have access to an Odoo instance for testing, note this clearly in your pull request so maintainers can verify.

## What We Do Not Accept

- Files containing credentials, API keys, or passwords (even placeholder examples)
- Documentation that references specific private Odoo instances
- Code examples requiring non-standard Python packages without clear justification
- Changes to `SKILL.md` (published to ClawHub — must be done by maintainers)
- Promotional content or links to commercial services

## Version Compatibility

This skill supports Odoo 17, 18, and 19. When documenting features:

- Note if a field or method is version-specific
- Use the version comparison table format for differences:

| Version | Field/Behavior | Notes |
|---------|---------------|-------|
| Odoo 17 | `logo_1920` | Original field name |
| Odoo 18+ | `logo` | Simplified naming |

## Questions?

Open a GitHub issue with the `question` label. Include your Odoo version and what you are trying to accomplish.
