# Credential Patterns — What to Flag

## Hardcoded API Keys (Flag: -2)

```bash
# BAD — plaintext key
API_KEY="sk_548c6868ad576b785e16ba1c391d636ab98884bb64edf216"
```

```python
# BAD — API key in source
api_key = "sk_548c6868ad576b785e16ba1c391d636ab98884bb64edf216"
```

## Acceptable Patterns (Score: +1)

```bash
# GOOD — env var reference
API_KEY="${MY_API_KEY}"
API_KEY="${OPENAI_API_KEY}"
```

```python
# GOOD — os.environ lookup
import os
api_key = os.environ.get("API_KEY")
```

```bash
# GOOD — interactive prompt
read -s -p "Enter API key: " API_KEY
```

## Placeholder Keys (Flag: review manually)

Common placeholder patterns that look real but aren't:
- `sk_0123456789abcdef...` (fake test keys)
- Keys matching `[A-Z0-9]{32,}` with no provider context
- Keys stored in variables named `KEY`, `SECRET`, `TOKEN` with no documentation

## Credential Storage Locations to Check

- `*.sh` — shell scripts
- `*.js` — JavaScript/Node scripts
- `*.py` — Python scripts
- `SKILL.md` — skill metadata (should never contain real keys)
- `config.json` — configuration files
- `.env` — environment files (flag if committed to repo)

## Safe Practices

1. Keys stored in `~/.openclaw/credentials/` or equivalent
2. Env var references in scripts: `${VAR_NAME}`
3. No `echo $API_KEY` or print statements with real values
4. `gitignore` presence in skill directory
5. `README.md` mentions credential setup without storing actual values