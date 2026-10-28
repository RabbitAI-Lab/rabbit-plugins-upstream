# Second Reality Video · Open Client

**Open client + wire protocol for a deterministic world-state video service.**

> `frame = render(state, shot)` — a persistent simulated world evolves under its own rules while the
> camera only chooses framing. Same seed and shots give byte-identical pixels anyone can recompute.

## What this package is

| | |
|---|---|
| ✅ Included | client script, API contract, shot-file schema, determinism notes, offline protocol simulator |
| ❌ Not included | the rendering engine, the world simulation, the server, any credentials |

The engine runs on a service you configure (`--api-base` / `SRV_API_BASE`). This repository publishes
the **client and the protocol**, so the flow can be audited, re-implemented and self-tested without
anyone's server.

## Quick start (offline, no account, no money)

```bash
# 1) start the protocol simulator
node scripts/mock-service.mjs

# 2) request a render -> HTTP 402 + Payment-Needed bill (exit code 2)
node scripts/second-reality-video-client.mjs probe \
  --api-base http://127.0.0.1:8788 --ticks 0-149 --state-dir .state --session-id demo

# 3) show the bill as a structured payment request (it does not pay)
node scripts/second-reality-video-client.mjs pay --state-dir .state --session-id demo

# 4) retry the SAME order with a proof -> job -> artifacts (sha256 verified)
node scripts/second-reality-video-client.mjs complete \
  --state-dir .state --session-id demo --payment-proof mock.<order_id> --out-dir ./out
```

`mock.<order_id>` comes from the 402 response (`mock_proof_hint`). The simulator renders nothing —
it only exercises the billing protocol.

## Against a real service

```bash
npx -y @alipay/agent-payment@latest install        # official buyer-side payment capability
export SRV_API_BASE=https://api.example.com
node scripts/second-reality-video-client.mjs probe --ticks 0-599 --state-dir .state --session-id demo
node scripts/second-reality-video-client.mjs pay    --state-dir .state --session-id demo
node scripts/second-reality-video-client.mjs complete --state-dir .state --session-id demo \
  --payment-proof '<credential from the official payment capability>' --out-dir ./out
```

## The protocol

```text
probe    → POST /api/v1/render                → 402 + Payment-Needed (bill)
pay      → hand the bill to official alipay-bot → user pays
complete → same request + Payment-Proof       → 202 + job_id
         → poll GET /api/v1/jobs/{job_id}      → ready
         → GET /api/v1/artifacts/{job}/{name}  → film + manifest + audit
```

- Same request body, same order, after payment — otherwise you get a second bill.
- Unknown payment state → query the order (`status`), never re-order.
- The client never holds a payment key and never signs; payment goes through the official capability.
- On success the result is the receipt; do not append a separate "payment successful" message.

## Reproducibility contract

| Layer | Anchor | Nature |
|---|---|---|
| State | `content_digest` sequence | deterministic, byte-verifiable |
| Pixels (R1) | per-frame `sha256` | deterministic, byte-verifiable |
| Container | `world.mp4` sha256 | **corroborative only** — not stable across ffmpeg versions |
| Pixels (R2) | weights / sampling seed / hardware | not implemented |

Frame hashes are the anchor; the container hash is not a claim.

## Layout

```
second-reality-video/
├── SKILL.md
├── README.md
├── LICENSE                             # MIT (client package only)
├── package.json
├── scripts/
│   ├── second-reality-video-client.mjs # probe / pay / complete / status / pricing
│   └── mock-service.mjs                # offline 402 protocol simulator
├── references/
│   ├── api.md                          # contract, bill/proof structures, error codes
│   ├── shot-files.md                   # shot schema, forbidden fields, hard constraints
│   └── determinism.md                  # byte-verifiable vs corroborative
└── PACKING.md                            # packaging rules (SkillHub rejects dotfiles)
```

## Install

```bash
skillhub install second-reality-video
```

## License

MIT for this package. The rendering engine is **not** included and is not licensed here; the rights
holder is NOHN AI TECHNOLOGY PTE. LTD. (international) and 上海霖铭均华科技有限公司 (China).
