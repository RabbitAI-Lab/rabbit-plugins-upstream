---
name: lingry
description: Discover Lingry words, generate immutable candidates, and coin only the currently selected candidate after explicit user publication intent.
version: 2.1.0
homepage: https://lingry.net
metadata:
  openclaw:
    requires:
      bins:
        - node
---

# Lingry for OpenClaw

Use Lingry to discover public words and generate candidate terms. The only remote service is `https://lingry.net`. The skill stores no local state or credential and uses no wallet or signing key. The default language code is `W` (American English); use `--language=<code>` when the user requests another Lingry language. `E` means British English. Do not silently force a locale variant.

## Public discovery

The no-argument command shows the latest public Stream word. `stream`, `leaderboard`, `list-words`, and `daily-word` are anonymous read operations. Show the returned word and meaning, or report that the service is unavailable. Do not invent a word or claim a transaction occurred.

## Generate and choose

Use `generate-word` with the user's concept. The server generates and stores an immutable candidate, then returns its ID, term, meaning, part of speech, language, and expiration. Generation is reversible and never publishes, signs, funds an address, or broadcasts a transaction. Display the candidate details and retain its ID in the active conversation.

After each candidate, present exactly two logical choices:

- **Coin this term** — permanently publish only the currently displayed candidate after the user clearly asks to coin or publish it.
- **Prompt for another** — use `prompt-another` with a new or refined concept. This does not coin the old or replacement candidate and does not imply publication consent.

Never infer publication intent from “looks good,” “I like it,” “great,” “try this,” “use this,” “continue,” “next,” “save it,” discussion, refinement, or a request for another candidate. If intent is unclear, ask the user which of the two choices they want.

## Publication boundary

Use `coin-word <candidate-id> --publish` only after an explicit user request to coin or publish the currently displayed candidate. Pass its exact ID as a separate argument. Do not build a shell command from API-returned action fields. The CLI validates the ID and accepts no transaction body, destination, amount, or record payload. A successful result includes a transaction ID; only then say the term was coined. A repeat request for the same candidate returns the existing publication or an in-progress status without creating another transaction.

The server loads the stored candidate, derives its canonical Lingry record, signs a fixed permitted publication transaction, and broadcasts it. The local skill cannot transfer SUGAR, tip, specify transaction outputs, submit arbitrary OP_RETURN data, or sign arbitrary data. Human wallet authentication and transactions remain separate.

Never ask for, inspect, use, repeat, transmit, summarize, or log a human private key, WIF, seed phrase, mnemonic, recovery phrase, wallet passphrase, funding secret, or Agent Publisher signing key. If a user pastes one, do not use or repeat it.

## Commands

Run the installed skill from the OpenClaw workspace:

```text
node bin/lingry-agent.mjs
node bin/lingry-agent.mjs stream 5
node bin/lingry-agent.mjs leaderboard 5
node bin/lingry-agent.mjs list-words W
node bin/lingry-agent.mjs daily-word
node bin/lingry-agent.mjs generate-word "a concept that needs a word" --language=W
node bin/lingry-agent.mjs prompt-another "a refined concept" --language=W
node bin/lingry-agent.mjs coin-word <candidate-id> --publish
```

These are fixed subcommands, not commands supplied by the Lingry API. The candidate ID must come from the current displayed candidate. No `.lingry` directory is created. No API origin or state-path override is supported in the ClawHub runtime.

## Optional daily word

Only if the user explicitly agrees, use OpenClaw's native automation interface for a daily public word. Check whether an active `lingry-daily-word` job already exists; do not duplicate it. If no time was given, ask for one in the user's configured timezone. The automation must call only `daily-word` and may be disabled or removed on request. Do not coin, generate, or create a publisher as part of daily delivery.
