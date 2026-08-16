# Signing — Canonical Form, Signatures, ETags, and Hashes

One sentence explains almost every failure in this file: **a signature is over bytes, and JSON has many byte representations of the same document** (Rule 5).

**Contents:** [Sign the Bytes You Received](#sign-the-bytes-you-received) · [Capturing the Raw Body](#capturing-the-raw-body) · [Verifying a Webhook](#verifying-a-webhook) · [Canonicalization](#canonicalization) · [JWS and JWT](#jws-and-jwt) · [ETags](#etags) · [Hashing for Identity and Deduplication](#hashing-for-identity-and-deduplication) · [Idempotency Keys](#idempotency-keys)

## Sign the Bytes You Received

Re-serializing changes, at minimum: key order, whitespace, number formatting (`1.0` vs `1`, `1e3` vs `1000`), and non-ASCII escaping. Any of those changes the hash, and none of them changes the meaning — which is why the failure reads as "the sender's signature is wrong" when the sender is correct.

Consequences, in order:

1. **Verification uses the raw bytes.** Parse afterwards, for the business logic.
2. **Anything that must be re-signed later stores the original bytes**, not the parsed object. A `raw_body` column, or the object graph plus the canonical form — never a re-encode of the parsed structure.
3. **Middleware that parses and re-emits a body invalidates every signature over it.** That includes proxies that "normalize" JSON, loggers that re-encode, and clients that parse into a model and re-serialize before forwarding.
4. When you must sign something you constructed yourself, canonicalize deliberately and record which canonicalization (Canonicalization below).

## Capturing the Raw Body

The general shape in every framework: read the raw body *before or during* JSON parsing, keep it on the request, and never reconstruct it afterwards.

- Node/Express: the JSON body parser exposes a verify-style hook that receives the raw buffer — store it there. Registering the JSON parser globally and then trying to get the raw body in a route is too late; the stream is consumed.
- Python/Flask: read the raw data before touching the parsed JSON property, since accessing the parsed form may consume the stream depending on configuration.
- Go: read the body into a buffer, then hand a new reader over that buffer to the decoder — the body is a one-shot stream.
- .NET: enable request buffering so the body can be read twice, or read the raw bytes in middleware first.
- Anything behind a gateway: confirm the gateway forwards the body byte-for-byte. A gateway that re-encodes (some do, for "validation") makes downstream verification impossible, and the fix is configuration, not code.

## Verifying a Webhook

The complete procedure, in order — skipping any step is a known class of bug:

1. Read the **raw** body bytes.
2. Recompute the MAC over exactly what the sender specifies — usually `timestamp + "." + raw_body`, not just the body. Read their documentation for the concatenation, because it differs per provider.
3. Compare with a **constant-time** comparison. A byte-by-byte early-exit comparison leaks the correct prefix and is a real, exploitable timing side channel.
4. Enforce a **timestamp tolerance** (5 minutes is the common default) so a captured request cannot be replayed forever. Requires the clock to be right; a drifting clock reads as random signature failures.
5. Enforce **idempotency** by the event id: the same event will be delivered more than once, by design, and retries are how you get charged twice.
6. Only then parse and act. Return 2xx quickly and do the work asynchronously — providers retry on timeouts, and slow handlers manufacture duplicate deliveries.
7. The signing secret lives in the environment or a secret manager and is referenced by pointer in anything written down: `env:VENDOR_WEBHOOK_SECRET` (`memory-template.md`).

Symptom-to-cause for verification failures: signature never matches for any request → wrong secret or wrong concatenation. Matches locally, fails in production → a proxy or middleware altering the body. Matches for small payloads, fails for large ones → a body size limit truncating the request, or `curl -d` stripping newlines (`debug.md`).

## Canonicalization

When there is no original byte stream — you built the document, or you must compare two documents from different producers — canonical form makes serialization deterministic.

**RFC 8785 (JCS)** is the standard one: object keys sorted by their UTF-16 code units, no insignificant whitespace, ECMAScript-style number formatting, minimal string escaping, UTF-8 output. Its constraint: every number must be representable as a double, so a document with a 19-digit integer literal cannot be canonicalized — one more reason ids are strings (Rule 2).

- **`JSON.stringify` with sorted keys is not JCS.** JavaScript enumerates integer-like keys first in ascending numeric order regardless of insertion or sort order, so `{"2":…, "10":…, "a":…}` does not come out in code-unit order. Any hand-rolled "sort the keys" canonicalizer has this bug on numeric-looking keys.
- Sorting recursively means sorting **every** object in the tree, including inside arrays. Array order is data and is never sorted.
- If both sides are yours, an agreed ad-hoc form (sorted keys, compact separators, no non-ASCII escapes) works — but write the definition down in `artifacts/` and treat it as a contract; the second implementation is where the mismatch appears.
- Round-trip risk: canonicalizing normalizes `1.0` to `1` and re-escapes strings. Never canonicalize a document you also need to verify against its original signature.
- Unicode: normalize to NFC *before* canonicalizing if the two sides may differ in normalization, and state that this is part of your canonical form — JCS itself does not normalize (`encoding.md`).

## JWS and JWT

- A JWS signature covers the base64url-encoded header and payload **strings**, not the JSON structures. Canonicalization is therefore irrelevant, and re-encoding a decoded JWT invalidates it — never rebuild a token from its parsed claims.
- **Pin the algorithm.** Never take `alg` from the token header: `alg: none` and the RS256→HS256 confusion (verifying an HMAC using the public key as the secret) are both defeated by deciding the algorithm from your own configuration and rejecting anything else.
- Verify before reading. A JWT's payload is readable by anyone; only the signature makes any claim trustworthy, and expired-but-valid is a separate check (`exp`, `nbf`, `iss`, `aud`).
- A JWT is a credential end to end: it goes in logs, fixtures and error messages by accident. Treat the whole token as a secret, pointer only (`security.md`).
- Detached payloads (signature over content transmitted separately) exist for large bodies; the same "sign the exact bytes" rule applies with the same failure mode.

## ETags

- A **strong** ETag means byte equality; a **weak** one (`W/"…"`) means semantic equivalence. Choose deliberately: caches, `If-Match` and `If-None-Match` behave differently, and range requests require a strong tag.
- Do not compute an ETag from a fresh serialization of an object unless that serialization is canonical — otherwise the tag changes when nothing did (a map iteration order change is enough), and every client re-downloads.
- Cheapest correct sources, in order: a row version or `updated_at` column, the stored bytes' hash, or a hash of the canonical form.
- `If-Match` on PATCH gives optimistic concurrency for free; without it, concurrent partial updates lose data silently (`patching.md`).

## Hashing for Identity and Deduplication

- Content addressing (a document's id is the hash of its content) requires canonical form or the exact stored bytes; anything else produces two ids for one document.
- Deduplicating incoming events by hashing the body works only if the producer's serialization is stable. Prefer the producer's event id; use a hash only as a fallback and say so.
- Choose SHA-256 as the default digest for these purposes. MD5 and SHA-1 remain acceptable for non-adversarial deduplication only, and there is no reason to pick them for anything new.
- Hash the bytes, never the pretty-printed form, and record which representation was hashed alongside the digest — a digest with no stated representation cannot be reproduced.

## Idempotency Keys

- The client generates a key per logical operation (a UUID), sends it with the request, and reuses it on every retry of that same operation.
- The server stores key → (status, response body, request fingerprint) for a retention window (24 hours is typical) and returns the stored response on a repeat.
- Store a **fingerprint of the request** with the key: a retry with the same key and a *different* body is a client bug, and returning the old response silently hides it. Reject with a 4xx that says so.
- The fingerprint is a hash of the raw body — the same rule as everywhere else in this file.

**When a canonicalization or signing policy is settled** — which form, which digest, which fields are covered, what the tolerance window is — write it to `~/Clawic/data/json/artifacts/<kebab-name>.md` with its `## Boxes` line, and the one-line rule into `## Conventions` of `memory.md`. Never write the secret itself: the pointer goes in its place (`memory-template.md`).
