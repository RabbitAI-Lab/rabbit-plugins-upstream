# agentlifeboat (ClawHub skill)

Source of the skill published to ClawHub as `agentlifeboat`. The agent-facing instructions are in `SKILL.md`; this file is for humans.

## Layout

- `SKILL.md`: ClawHub manifest and instructions (what the agent reads).
- `scripts/lifeboat.mjs`: the command-line entry point the agent runs through its exec tool.
- `scripts/lib.mjs`: pure helpers (key derivation identical to the sidecar, x402 paying fetch, API calls with injectable fetch).
- `package.json`: pinned dependencies. On first run the script installs them next to itself; ClawHub bundles ship without `node_modules`.

## Design choices

- The skill does not bundle a wallet. It uses `X402_PRIVATE_KEY`, the same variable the popular x402 skills use, and derives the snapshot encryption key from it exactly like the Estate sidecar does, so an agent that later moves into a room keeps the same key.
- No pricing metadata in the manifest (ClawHub forbids it); costs are documented in prose.
- Paid commands never run concurrently from the script; the instructions tell the agent not to either.

## Test locally

```
pnpm --filter @estate/skill-lifeboat test
```

Manual run against a local API (see `apps/api/README.md` to start one on port 4021 with a testnet `PAY_TO`):

```
export ESTATE_API=http://127.0.0.1:4021 X402_PRIVATE_KEY=0x... ESTATE_STATE_FILE=/tmp/estate.json
node scripts/lifeboat.mjs register --threshold 30
node scripts/lifeboat.mjs heartbeat
node scripts/lifeboat.mjs snapshot --archive some-backup.tar.gz
node scripts/lifeboat.mjs extend 2
node scripts/lifeboat.mjs status
```

## Verified 2026-09-09

- Shell run against a local API on Base Sepolia with the test wallet: `recipient`, `register` ($0.10 settled), `heartbeat`, `snapshot --archive` ($0.01 settled, 3.2 KB ciphertext stored), `extend 2` ($0.14 settled), `status` (three settled payments), plus the no-wallet and not-registered error paths (exit 2).
- Agent-driven run inside an Estate room (skill mounted into `workspace/skills/`, OpenClaw listed it as ready): the prompt "Use the agentlifeboat skill: run its register command with threshold 30, then heartbeat, then status" produced, from the agent through its exec tool, a registration paid on testnet (tx `0x8000df6f…`), a heartbeat, and this reply:

  > agentId: c3897e2b-18e5-4afb-b4be-d2510547ad45, status: covered, policy threshold 30, mode estate-restores, one settled register payment.

  The API showed the new agent with a fresh heartbeat and the state file existed in the workspace.
- Note for the room proxy: Gemini's OpenAI-compatible endpoint rejects multi-turn tool calls unless the `thought_signature` it returns is echoed back, which OpenClaw's generic client does not do. The agent-driven run used OpenClaw's native Gemini provider; the proxy will need to carry that field for Gemini upstreams (brain-failover plan).

## Publish (human step)

```
clawhub login
clawhub skill publish skills/agentlifeboat --slug agentlifeboat --name "Estate lifeboat" --version 0.1.0
```

Then, from a fresh OpenClaw: `openclaw skills install @<owner>/agentlifeboat`.
