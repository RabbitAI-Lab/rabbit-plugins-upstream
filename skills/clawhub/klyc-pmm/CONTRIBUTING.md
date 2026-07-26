# Contributing

Thanks for helping improve KLYC-PMM.

## How to Contribute

1. **Fork** the repository
2. **Create a branch** for your change
3. **Test** your change — run `./pmm_watch.sh push "test" "this is a test"`
4. **Follow conventions:**
   - Shell scripts: POSIX-compatible `#!/bin/bash`, `set -euo pipefail`
   - Documentation: English-first, Chinese translations in `description_zh` fields
   - No hardcoded URLs or tokens — use config files or environment variables
5. **Submit a PR** with a clear description

## Code Style

- Shell: `tab` indentation, `snake_case` functions, `UPPER_CASE` constants
- JSON: 2-space indent, sorted keys
- Markdown: 80-char line limit where practical

## Security

Never commit:
- API tokens or keys
- Server URLs pointing to non-public endpoints
- User data or memory content

If you find a security issue, do NOT open a public issue. Contact the Kunlun community directly.

## License

By contributing, you agree your contributions will be licensed under MIT-0.
