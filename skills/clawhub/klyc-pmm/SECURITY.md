# Security Policy — klyc-pmm

## Architecture

KLYC-PMM is designed so the server **cannot read user data**.

```
Agent (local)                    Server (cloud)
─────────────                    ──────────────
content → AES-256-GCM encrypt → ciphertext → blind store
key ─── stays local ─────────────────────────── never leaves agent
```

## Threat Model

### What we protect against
- **Server breach:** encrypted blobs, no plaintext access
- **Network sniffing:** TLS 1.2+ for all communication
- **Credential theft:** API token in chmod 600 local file, never in package
- **Replay attacks:** per-key rate limiting on server
- **Supply chain:** package contains no keys, tokens, or URLs pointing to production

### What we don't protect against
- **Full agent compromise:** if attacker owns the agent's filesystem, they own the encryption key
- **Memory dump on agent machine:** keys in process memory are extractable

## Key Management

- Encryption key derived from agent identity + random salt
- Key stored in `~/.klyc-pmm/.key` (chmod 600)
- Server never receives encryption key
- Token rotation: `pmm_watch.sh init --rotate` generates new token, old one expires

## Data Handling

| Data | Storage | Encryption |
|------|---------|:----------:|
| Memory content | Server MySQL | AES-256-GCM (client) |
| Content hash | Server MySQL | SHA-256 (plain, for dedup) |
| Tags, domain | Server MySQL | Plain (for indexing) |
| Local index | `~/.klyc-pmm/index.json` | None (local file) |
| API token | `~/.klyc-pmm/token` | chmod 600 |

## No Telemetry

Zero analytics. Zero tracking. Zero phoning home beyond explicit actions (push/search/recover are all user-initiated).

## Reporting

Security issues: contact via the Kunlun community at https://kunlunyaochi.com

## Audit History

- 2026-07-20: Full external penetration test (3 rounds), score A (8.5/10). All findings remediated.
