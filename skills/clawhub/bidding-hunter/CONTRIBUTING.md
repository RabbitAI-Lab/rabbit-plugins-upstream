# Contributing to Bidding Hunter

Thanks for your interest in contributing! This project automates government procurement bid discovery — every new platform adapter helps more people find relevant opportunities.

## Ways to Contribute

### 🔌 Add a New Platform Adapter

This is the most valuable contribution! Adding support for a new regional procurement platform.

1. **Check existing platforms**: See `src/platforms/` for examples
2. **Use the exploration tool**: `node scripts/explore-platform.js --url <url> --recon`
3. **Create from template**: `bidding-hunter create-adapter --name <id>`
4. **Implement the adapter**:
   - `meta` — Platform metadata
   - `scan(context, config)` — Main scanning logic
   - `extractItems(page, { today, fromDate })` — DOM extraction
5. **Test**: `bidding-hunter test-platform --name <id>`
6. **Submit PR** with:
   - The adapter file in `src/platforms/`
   - Updated README platform list
   - Brief description of the platform

### 🐛 Bug Reports

- Check existing issues first
- Include: platform name, error message, steps to reproduce
- If possible, include browser console output or page structure changes

### 💡 Feature Requests

Open an issue with:
- What you want to achieve
- Why the current system doesn't support it
- How you envision it working

### 🧪 Testing

```bash
# Run unit tests
npm test

# Test a specific platform
bidding-hunter test-platform --name <id>

# Run a dry-run scan
bidding-hunter scan --dry-run
```

## Development Setup

```bash
git clone https://github.com/user/bidding-hunter.git
cd bidding-hunter
npm install
npx playwright install chromium

# Create test config
bidding-hunter init
```

## Platform Adapter Guidelines

A good platform adapter:

1. **Is defensive**: Handles network timeouts, changed selectors, no-data states
2. **Uses retry stairs**: 30s → 45s → 60s with `gotoWithRetry`
3. **Respects rate limits**: Uses delays between actions
4. **Extracts clean data**: Returns `{ site, region, title, date, url }`
5. **Is self-contained**: One file, no external dependencies beyond Playwright
6. **Has clear logging**: Console messages in `site [query]` format
7. **Handles pagination**: Button-based or URL-based with max page limit
8. **Filters by date window**: Only returns items within `fromDate ~ today`

### Adapter Checklist

- [ ] `meta.id` is lowercase, no spaces, unique
- [ ] `meta.url` points to the listing page (not detail page)
- [ ] `scan()` creates its own browser context + page
- [ ] Uses `this.gotoWithRetry()` for navigation
- [ ] `extractItems()` uses `page.$$eval()` with serialized options
- [ ] Date extraction handles multiple formats (YYYY-MM-DD, YYYY/MM/DD, etc.)
- [ ] Returns items with all required fields
- [ ] Closes browser context in `finally` block
- [ ] Tested with `bidding-hunter test-platform`

## Code Style

- ES6+ with `'use strict'`
- 2-space indentation
- Single quotes for strings (except template literals)
- `async/await` for all async operations
- Descriptive variable names
- Chinese comments for platform-specific logic

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
