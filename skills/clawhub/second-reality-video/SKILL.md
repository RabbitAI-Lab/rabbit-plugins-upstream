---
name: second-reality-video
slug: second-reality-video
version: 1.0.1
displayName: Second Reality Video · Open Client
description: Open client and wire protocol for a deterministic world-state video service. A persistent simulated world evolves under its own rules while the camera only chooses framing, so the same seed and shot plan always produce byte-identical frames that any third party can recompute and verify. This package ships the client, the API contract and a local protocol simulator: it calls a compatible render service over HTTP, receives a 402 Payment-Needed bill, hands that bill to the official Alipay payment capability, then retries the very same request with Payment-Proof and collects the film, per-frame hashes, a signed reproducibility manifest and a 25-dimension constitutional audit report. The rendering engine itself is NOT included and never ships here.
required_commands:
  - node
---

# Second Reality Video · Open Client

> A deterministic video pipeline. Persistent world state becomes film; the camera picks framing, never story:
> `frame = render(state, shot)`. Same seed and shots give byte-identical pixels anyone can recompute.

**Scope, stated up front.** This package is the **open client** for a deterministic world-video
service: the protocol, the orchestration script, the API contract and a local protocol simulator.
The **rendering engine is not included** — it runs on a compatible service you point this client at
(`--api-base` / `SRV_API_BASE`). If you want to host the engine yourself, that is a separate
commercial engagement with the rights holder.

## What is in the box

| | |
|---|---|
| ✅ Included | `scripts/second-reality-video-client.mjs` (probe / pay / complete / status / pricing), `scripts/mock-service.mjs` (offline 402 protocol simulator), API contract, shot-file schema, determinism notes |
| ❌ Not included | the renderer, the world simulation, the server, any key or order state |

## The protocol in one picture

```text
probe    → POST /api/v1/render                → 402 + Payment-Needed (bill, base64url)
pay      → hand the bill to official alipay-bot → user pays
complete → same request + Payment-Proof       → 200 + content + Payment-Validation
         → GET /api/v1/render/{order}/artifacts/{name} → film + manifest + audit
```

Two rules carry the whole design:

1. **Reuse the order.** After payment, replay the *identical* request body on the *identical*
   order. Different parameters ⇒ a different order and a second bill.
2. **Never pay twice.** If the payment state is unclear, look the order up first
   (`status`), instead of ordering again.

## Try it offline, in 30 seconds

The bundled simulator speaks the same protocol and never touches money:

```bash
# terminal 1 — protocol simulator (not a renderer)
node scripts/mock-service.mjs

# terminal 2 — the client
node scripts/second-reality-video-client.mjs probe \
  --api-base http://127.0.0.1:8788 --ticks 0-149 --state-dir .state --session-id demo
# → HTTP 402, exit code 2, state saved to .state/demo.json

node scripts/second-reality-video-client.mjs pay --state-dir .state --session-id demo
# → prints the bill as a structured payment request (it does not pay)

node scripts/second-reality-video-client.mjs complete \
  --state-dir .state --session-id demo \
  --payment-proof mock.<order_id> --out-dir ./out
# → 202 → job ready → artifacts written to ./out with sha256 verified
```

Replace `mock.<order_id>` with the value from the 402 response's `mock_proof_hint`.

## Against a real service

```bash
# buyer-side official payment capability (install once)
npx -y @alipay/agent-payment@latest install

export SRV_API_BASE=https://api.example.com
node scripts/second-reality-video-client.mjs probe \
  --ticks 0-599 --resolution 1280x720 --fps 30 --shot demo \
  --state-dir .state --session-id demo-001
```

Payment itself always goes through the official capability — this client never holds a key and
never signs a payment. On the success path the result *is* the receipt: do not append a separate
"payment successful" message.

## Parameters

| Flag | Default | Meaning |
|---|---|---|
| `--api-base` | `$SRV_API_BASE` | base URL of a compatible render service |
| `--world-id` | `sr-video-demo` | world identifier (part of the reproducibility key) |
| `--seed` | `42` | genesis seed |
| `--agents` | `10` | number of souls in the world |
| `--ticks` | `0-599` | tick range; 10 ticks = 1 s of film |
| `--resolution` | `1280x720` | output resolution |
| `--fps` | `30` | must be an integer multiple of 10 (the engine's fixed time base) |
| `--shot` | `demo` | shot-plan preset name |
| `--samples` | `3` | how many still frames are dumped for review |
| `--service-id` | auto | force a pricing tier (read from `/api/v1/pricing`) |
| `--state-dir` | `.state` | session state directory (bill + original request) |
| `--session-id` | `default` | session key |
| `--payment-proof` | — | credential returned by the official payment capability |
| `--out-dir` | `./out` | where artifacts are written |

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/health` | liveness |
| POST | `/api/v1/render` | the resource endpoint (402 → pay → retry with `Payment-Proof` → 200) |
| GET | `/api/v1/render/{out_trade_no}/artifacts/{name}` | download one delivered artifact |

There is **no** order-lookup endpoint in this protocol: when the payment state is unclear, replay the
**same** request with the **same** `Payment-Proof` — the service is idempotent per order, so it
neither charges twice nor delivers twice.

Full request/response shapes, bill and proof structures, and error codes: `references/api.md`.

## Artifacts you get back

| File | Contents |
|---|---|
| `world.mp4` | the H.264 film |
| `hashes.txt` | one sha256 per frame — the pixel-layer reproduction anchor |
| `frames.jsonl` | per-frame backing record |
| `identity_assets.json` | `soul_hash` → appearance asset evidence |
| `manifest.json` | Ed25519-signed `RenderManifest` (world params, digests, renderer provenance, audit verdict) |
| `audit_report.txt` | 25-dimension constitutional audit, one verdict per dimension |

## Reproducibility, stated precisely

| Layer | Anchor | Nature |
|---|---|---|
| State | `content_digest` sequence | deterministic, byte-verifiable |
| Pixels (R1) | per-frame `sha256` | deterministic, byte-verifiable |
| Container | `world.mp4` sha256 | **corroborative only** — not stable across ffmpeg versions |
| Pixels (R2) | weights / sampling seed / hardware | not implemented |

`world.mp4`'s hash is not a reproducibility claim: H.264 containers are not bit-stable across
ffmpeg builds. The **frame hashes** are the anchor. Details: `references/determinism.md`.

## Files

- `scripts/second-reality-video-client.mjs` — the client (`probe` / `pay` / `complete` / `status` / `pricing`)
- `scripts/mock-service.mjs` — offline protocol simulator (no renderer, no money)
- `references/api.md` — API contract, bill and proof structures, error codes, idempotency rules
- `references/shot-files.md` — shot-plan schema, forbidden fields, hard constraints
- `references/determinism.md` — what is byte-verifiable, what is only corroborative
- `LICENSE` — MIT
- `PACKING.md` — packaging rules: what the upload may contain and what must never ship
  (`.state/`, `.env`, `node_modules/`, logs). SkillHub rejects dotfiles, so the exclusion list
  lives in a normal file.

## Safety & responsible use

- This client renders **simulated** worlds. It does not verify real-world claims and is not a
  substitute for editorial, legal or scientific review.
- The shot plan may not contain behaviour directives (see `references/shot-files.md`): a film whose
  plot was scripted into the camera file is not what this pipeline claims to produce.
- You are responsible for how the output is used and for complying with the laws and platform
  rules that apply to you.

## License

MIT for this client package (see `LICENSE`). The rendering engine is **not** licensed here; the
rights holder is NOHN AI TECHNOLOGY PTE. LTD. / 上海霖铭均华科技有限公司.
