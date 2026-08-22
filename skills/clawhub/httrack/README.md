# 🕸️ httrack

**Category:** research, knowledge

## ✨ What This Skill Does

Teaches an AI agent (or human) how to mirror websites to local disk with
**HTTrack**, the open-source offline browser / website copier. It turns a URL
into a complete offline copy — HTML, images, stylesheets, and links — usable
with no network connection. Includes ready-to-run recipes for depth-limited
crawls, single-page snapshots, incremental mirror updates, and file-type
filtering, plus a safe wrapper script (`mirror.sh`) with sane defaults.

## 🔐 Permissions & Requirements

- Requires the `httrack` binary (Debian/Ubuntu: `sudo apt install httrack`).
- Network: makes outbound HTTP/HTTPS requests **only to the site(s) you tell
  it to mirror** — no third-party relay.
- Filesystem: writes the mirrored site into the output directory you specify
  (default `./mirror`).
- No API keys, no secrets, no login required.

## 🔒 Security & Privacy

- What it reads/collects: the public (and any unauthenticated) content the
  target site serves for the URLs you request.
- Does data leave the machine? It downloads FROM the target site to your disk;
  it does not upload or transmit anything about you or your machine.
- No secrets are read, stored, logged, or transmitted by this skill.
- Known risks: a mirror can include scripts, cookies, tracking pixels, or
  pages that were not intended for you — review the downloaded files, and only
  mirror sites you are authorized to archive. Mirrored content may be
  copyrighted and subject to the site's terms of service.
- Mitigations: the wrapper obeys robots.txt (`--robots=1`), limits recursion
  depth and parallel connections (avoids hammering servers), and reminds the
  user of the legal obligations.
- Review before install: read `SKILL.md` and `mirror.sh` — they are short and
  self-contained.

## ✅ Verification Hash

Installers can verify this skill matches the published artifact by hashing the
skill files and comparing to the digests below:

- **SKILL.md SHA-256:** `4a651e78546248a3f99906b1c60f928ec46459c176f99f38f0a3b0ab5c382c75`
- **mirror.sh SHA-256:** `4e59830145b772436d9a659bd0aa1915311ba1a4f64d8ec6dbaa9ed679037d66`

Verify locally:

```bash
sha256sum SKILL.md mirror.sh
# compare the output to the SHA-256 values above.
```

---
*Published under the Skill Publishing Standard — see SKILL_PUBLISHING_STANDARD.md.*
