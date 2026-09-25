# Lingry OpenClaw skill 2.1.0

The skill discovers public Lingry words, requests a server-generated word candidate, and publishes only the selected immutable candidate after an explicit user request. The service origin is fixed at `https://lingry.net`.

## Install

```bash
openclaw skills install '@svetlyoh/lingry'
```

The ClawHub artifact contains only `SKILL.md`, `README.md`, `bin/lingry-agent.mjs`, and `src/runtime.mjs`. Node.js 18 or newer is required. There are no package dependencies or local setup secrets.

## Workflow

Use `generate-word "a concept"` to obtain an immutable candidate. Show the term, meaning, part of speech, and language. Then offer **Coin this term** and **Prompt for another**. `prompt-another "new concept"` only generates a new candidate. To publish, the user must explicitly request coining of the currently displayed candidate; the agent then uses `coin-word <candidate-id> --publish`. The server returns a transaction ID after publication. Retry with the same ID is idempotent.

`W` is Lingry's American English code and the default. `E` is British English. Pass `--language=<code>` to select another supported language.

## Security model

The client stores no state or long-lived authentication secret. Generating a candidate creates no Agent Publisher identity, transaction, or publication. It never asks for or handles a user's wallet secrets.

The coin request contains only a strictly validated, high-entropy candidate ID and an empty JSON body. The client cannot construct arbitrary cryptocurrency transactions, send SUGAR, specify transaction outputs, submit arbitrary OP_RETURN data, or perform general blockchain signing. Canonical word-record construction, blockchain signing, and broadcast are performed by Lingry's server. The server creates or reuses its own publisher only when coining is requested and enforces publication by candidate ID.

The client rejects redirects and responses over 128 KiB, uses a fixed HTTPS origin, and presents sanitized errors. It never runs API-returned text as commands. A candidate expires after the server's configured lifetime.

This source repository retains tests and development files. Build the minimal publishable directory with `npm run build:clawhub` from the repository root, inspect `dist/clawhub-lingry/`, and publish that directory only after review. Server deployment and ClawHub publication are separate operations.
