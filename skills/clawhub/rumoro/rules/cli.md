# The CLI, the SDKs and the OpenAPI document

The same operations come packaged, with the same names. Use one when it is installed or the project already depends on it; plain HTTP with curl works everywhere.

## The `rumoro` CLI

`npm install -g @rumoro-dev/cli`, or run it without installing: `npx @rumoro-dev/cli --help`. Check with `command -v rumoro`.

- One `noun:verb` command per endpoint, such as `rumoro mentions:search --relevant true --intent buy_intent --limit 20` or `rumoro keywords:create --term "acme" --kind brand`. Every rule file names the command for each endpoint.
- It reads `RUMORO_API_KEY`, or the key `rumoro auth:login` stored in `~/.rumoro/config.json`.
- Output is JSON: compact when piped, indented on a terminal. Errors go to stderr.
- `rumoro mentions:watch` streams new mentions as they arrive, one JSON object per line (`| jq -r '.post.url'`).

Source: https://github.com/rumoro-dev/cli · Docs: https://docs.rumoro.dev/cli

## TypeScript SDK

`npm install @rumoro-dev/sdk`. One function per endpoint, generated from the OpenAPI document:

```ts
import { createRumoro } from '@rumoro-dev/sdk';
const rumoro = createRumoro({ apiKey: process.env.RUMORO_API_KEY! });
const { data, error } = await rumoro.searchMentions({ query: { relevant: true, limit: 25 } });
```

Source: https://github.com/rumoro-dev/sdk · Docs: https://docs.rumoro.dev/sdks/typescript

## Python SDK

`pip install rumoro`. Sync (`Rumoro`) and async (`AsyncRumoro`) clients:

```python
from rumoro import Rumoro
rumoro = Rumoro(api_key="ref_...")
for mention in rumoro.mentions.search(relevant=True, limit=25).data:
    print(mention.classification.relevance, mention.post.url)
```

Source: https://github.com/rumoro-dev/sdk-python · Docs: https://docs.rumoro.dev/sdks/python

## The OpenAPI document

`https://api.rumoro.dev/v1/openapi.json` lists every operation, parameter, field and error code. The SDKs, the CLI and the rule files in this skill are generated from it.
