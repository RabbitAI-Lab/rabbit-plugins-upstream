---
name: file-hasher
description: Compute file checksums (MD5, SHA-1, SHA-256) and verify file integrity. Use when you need to verify file integrity, detect duplicates, or generate hash identifiers for digital assets.
metadata: { "openclaw": { "emoji": "🔐" } }
---

# File Hasher

Quickly compute and verify file hashes. Supports MD5, SHA-1, and SHA-256.

## Prerequisites

- `sha256sum`, `sha1sum`, `md5sum` available on PATH (standard on Linux/macOS)

## Usage

### Compute a single hash

```bash
bash scripts/hash.sh <file> [algorithm]
```

- `algorithm`: `sha256` (default), `sha1`, or `md5`

### Compute all algorithms at once

```bash
bash scripts/hash-all.sh <file>
```

### Verify a hash

```bash
bash scripts/verify.sh <file> <expected-hash> [algorithm]
```

Exit code 0 = match, 1 = mismatch.

## Examples

```bash
# SHA-256 of a file
bash scripts/hash.sh ./photo.jpg sha256

# All hashes
bash scripts/hash-all.sh ./document.pdf

# Verify MD5
bash scripts/verify.sh ./data.zip abc123def456 md5
```
