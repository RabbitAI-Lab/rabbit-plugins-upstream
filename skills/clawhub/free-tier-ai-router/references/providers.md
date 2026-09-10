# Pluggable providers (`~/.config/ai_router/providers.json`)

Any OpenAI-compatible endpoint becomes a routable provider — a corporate gateway,
Together/Fireworks/Grok/DeepSeek, or a **local Ollama / llama.cpp / vLLM server**
(free, unlimited capacity the router will happily spend first if you tier it `cheap`).

```json
{
  "providers": {
    "my-lab-gateway": {
      "base_url": "http://127.0.0.1:18321/v1/",
      "auth": "none",
      "models": [
        {"id": "big-70b", "quality": 5, "rpm": 600, "rpd": null, "tier": "cheap", "tags": "best-value"},
        "tiny-1b"
      ]
    }
  }
}
```

- `auth`: `bearer` (default) · `x-api-key` · `none` (local servers)
- keys: inline `api_key`, or `key_file`, or the usual `~/.config/<name>/credentials.json`
- `models` entries: full objects or bare ids (defaults: quality 2, rpm 30, tier
  `mid` — deliberately conservative for unmeasured routes; run `probe.py`/`quality.py` to measure)
- **user entries override built-ins** on (provider, model) conflicts; built-in
  measured routes are never shadowed by specs
- a malformed file is a WARNING, never a crash — built-in routes keep working;
  `--json` answers surface it with exit code **4**
- validate the file against `schema/providers.config.schema.json`
- `auth: "none"` on a non-local base_url prints a loud warning (unauthenticated path)

Built-in specs (active only when their credential file exists, so nothing spends
quota by surprise): **groq, llm7, huggingface, cerebras, cohere**. Local servers
are opt-in via a providers.json entry.

## `--discover [--apply]`

`GET {base}/models` for every configured provider. Lists what it finds; adds routes
**only with `--apply`** (a model list can be hundreds of entries and every route is
a potential quota spend — the user opts in). 401/403 listings (chat-scoped keys)
are skipped with a note; odd JSON shapes never crash; `--provider X` filters.

## Machine contract

`ai "q" --json`, `--status --json`, `--plan --json`, `--learn --json` emit
schema-versioned objects (`ai_router.answer.v1`, `.status.v1`, `.plan.v1`,
`.learn.v1`). JSON Schemas ship in [`schema/`](../schema/) — including
`providers.config.schema.json` for this config file. Exit codes: 0 ok · 2 all routes
quota-dead · 3 no keys configured · 4 invalid providers.json.

## Maintenance (for contributors)

`router_fixed.json` and the `#__PAYLOAD__` blob inside `get-ai-router.sh` must be
regenerated whenever `router.py` changes:

```python
import base64, hashlib, json
raw = open('router.py','rb').read()
blob = {'_comment': 'self-repair payload for integrate.sh',
        'sha256': hashlib.sha256(raw).hexdigest(),
        'router_py_b64': base64.b64encode(raw).decode()}
json.dump(blob, open('router_fixed.json','w'), indent=1)
```

Then rebuild get-ai-router.sh: `awk` the script up to the `#__PAYLOAD__` marker,
append the new JSON. Verify: `python3 -c "import json,hashlib,base64;j=json.load(open('router_fixed.json'));assert hashlib.sha256(base64.b64decode(j['router_py_b64'])).hexdigest()==j['sha256']"`.

## Limits and honesty

- **Cerebras** was unfunded at the 2026-07-30 probe (key authenticates, inference 402) —
  excluded from routing until funded. Re-run `probe.py` to re-check.
- **Kilo** paid models excluded (balance $0 at probe); only its free models are routed.
- Quality scores come from 5 objective questions — enough to catch obvious reasoning
  failures, not a substitute for a full benchmark suite.
- Rate limits were read from live headers where published (Mistral) and from error
  text elsewhere (Gemini). Providers change these; re-run `probe.py` to refresh.
- `--stream` covers OpenAI-compatible transports; the gemini transport falls back
  to a normal (non-streaming) call.
