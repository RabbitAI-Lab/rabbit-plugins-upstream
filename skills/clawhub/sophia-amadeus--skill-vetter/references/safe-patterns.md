# Safe Coding Patterns

Reference for identifying trustworthy skill code.

## Good Shell Script Patterns

```bash
# Env var with fallback
API_KEY="${OPENAI_API_KEY:-}"
if [ -z "$API_KEY" ]; then echo "Error: OPENAI_API_KEY not set"; exit 1; fi

# Check for required tools before running
command -v curl >/dev/null 2>&1 || { echo "curl required"; exit 1; }
command -v jq >/dev/null 2>&1 || { echo "jq required"; exit 1; }

# Safe file creation (not overwriting)
OUTPUT="${HOME}/output.txt"
if [ -f "$OUTPUT" ]; then
  echo "Output exists, appending..."
  echo "new data" >> "$OUTPUT"
else
  echo "new data" > "$OUTPUT"
fi
```

## Safe Python Patterns

```python
import os, sys, json

# Env var with validation
api_key = os.environ.get("API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable not set")

# Safe requests pattern
import requests
response = requests.get(
    "https://api.example.com/data",
    headers={"Authorization": f"Bearer {api_key}"},
    timeout=30
)
response.raise_for_status()
data = response.json()
```

## Safe Node/JS Patterns

```javascript
const axios = require('axios');

const apiKey = process.env.API_KEY;
if (!apiKey) throw new Error("API_KEY not set");

const response = await axios.get('https://api.example.com/data', {
  headers: { 'Authorization': `Bearer ${apiKey}` },
  timeout: 30000
});
```

## Network Call Patterns

### Acceptable (local or well-known endpoints)

- `localhost:*` / `127.0.0.1:*`
- `api.openclaw.ai`
- `clawhub.com`
- `api.elevenlabs.io`
- Known providers (OpenAI, Anthropic, Deepgram)

### Suspicious (review carefully)

- Unknown third-party domains without documentation
- Phone-home patterns (unconditional outbound calls at startup)
- Data exfil to personal servers or unknown cloud services
- API calls that send user conversation history elsewhere

## Destructive Operations to Flag

- `rm -rf $DIR` — recursive delete, dangerous in scripts
- `chmod 777` — world-writable permissions
- `sudo` in non-admin contexts
- `eval $VAR` / `exec $CMD` — shell evaluation risks
- `/dev/tcp/*` — direct socket connections

## Permission Documentation Requirements

Good SKILL.md includes:
- `requires` field in metadata (tools, bins, node packages)
- Explicit statement of what the skill can and cannot access
- Clear description of data flow (where data goes, where it comes from)
- No vague "can do anything" language

## Package Manager Security

- `npm install` without `--save-dev` in scripts is fine
- Community packages with 0 downloads = suspicious
- Check npm package names against typosquatting (e.g., `request` vs `reqest`)
- Avoid `curl | bash` patterns for installing from URLs you don't trust