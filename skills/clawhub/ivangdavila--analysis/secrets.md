# Exposed Credentials — Finding Them, Rotating Them, Proving They Are Dead

**Before scanning**, read `## Credential Inventory` in `~/Clawic/data/analysis/memory.md` — or the file its `## Boxes` line points to. A credential already inventoried with a pointer and an expiry is not a new finding; a credential in a file that the inventory says should be in a store *is*.

**Contents:** [Where Credentials Actually Leak](#where-credentials-actually-leak) · [Detection Ladder](#detection-ladder) · [Prefix Families](#prefix-families) · [Entropy, And Why It Is Second](#entropy-and-why-it-is-second) · [File Permissions](#file-permissions) · [Git History](#git-history) · [Blast Radius Before Panic](#blast-radius-before-panic) · [The Rotation Runbook](#the-rotation-runbook) · [Expiry Calendar](#expiry-calendar) · [What Is Not A Secret](#what-is-not-a-secret) · [Write It Down](#write-it-down)

## Where Credentials Actually Leak

Ranked by how often the audit finds something, not by how interesting the vector is.

| Place | Why it happens | Cheapest check |
|---|---|---|
| `.env` and `.env.*` outside `.gitignore` | Written once during setup, never revisited | `git check-ignore -v .env`; if it exits non-zero the file is tracked or ignorable-but-tracked |
| Config files with an inline value | A YAML/JSON/TOML field that takes either a value or a reference, and the value was faster | Prefix scan over config extensions |
| Notes and memory files | The agent was told a key and helpfully wrote it down where it writes everything else | Prefix scan over the whole memory tree — this is the one people forget to scan |
| Session transcripts and job output | The value was printed by a command whose output was captured | Prefix scan over log and transcript directories, then set a retention (`workspace.md`) |
| Git history | Removed from the file, still in every clone and every fork | Pickaxe search below |
| Shell history | `export TOKEN=...` typed once | Prefix scan over `~/.*history` files, reported never quoted |
| Editor and backup residue | `.env.bak`, `.env.save`, `config.yml~`, `.swp`, `#file#` | Glob those suffixes before scanning content |
| Backups and archives of the workspace | The tarball predates the cleanup | Scan the archive listing for the filenames above; do not extract |

Any hit in the last three is still a finding even if the live file is clean: a credential's exposure is the union of every copy.

## Detection Ladder

1. **Names** — glob for `.env*`, `*credential*`, `*secret*`, `*.pem`, `*.key`, `*.p12`, `id_*` without `.pub`, plus the residue suffixes. Free, and it tells you where to look.
2. **Prefixes** — the table below over those files plus every config, note, and log file. Near-zero false positives; this is the workhorse.
3. **Entropy** — only over files that step 1 named or step 2 touched.
4. **History** — pickaxe over the repo, only when steps 2-3 hit or the repo is or ever was public.

Excluded from content scanning at every step, because they generate nothing but noise: lockfiles (`*.lock`, `package-lock.json`, `*.sum`), minified and map files, `.git/objects`, checksum manifests, binary blobs, and anything matched by `excluded_paths`. Report the exclusion count in the run so a scan of nothing is not mistaken for a clean scan.

## Prefix Families

Provider-prefixed tokens are self-identifying, which makes both detection and triage exact — the prefix names the issuer, so you know where to rotate before you know whose it is.

| Pattern | Issuer class | Rotation is |
|---|---|---|
| `AKIA…` / `ASIA…` | Cloud access key id (`ASIA` = temporary, expires on its own) | Deactivate then delete the key pair; `ASIA` may need only a session end |
| `ghp_`, `gho_`, `ghs_`, `github_pat_` | Code host personal/OAuth/server token | Revoke in developer settings; check org audit log |
| `glpat-` | Code host project or personal token | Revoke; scoped tokens list their scopes on the token page |
| `sk-`, `sk-ant-`, `sk-proj-` | Model provider API key | Revoke and reissue; usage dashboards show whether it was used |
| `xoxb-`, `xoxp-`, `xapp-` | Chat platform bot/user/app token | Rotate in the app config; bot tokens invalidate every webhook using them |
| `AIza…` | Cloud API key, often unrestricted by default | Rotate *and* add an API restriction; an unrestricted key is a second finding |
| `shpat_`, `dop_v1_`, `SG.`, `npm_`, `pypi-AgEI`, `rk_live_`, `sk_live_` | Commerce, hosting, mail, package, payment | Rotate at the issuer; payment keys are always CRITICAL |
| `-----BEGIN … PRIVATE KEY-----` | Private key material | Generate a new pair, replace every authorized copy, then delete the old |
| `eyJ` followed by base64 | JWT — may be a session, an id token, or a long-lived service token | Decode the header and `exp` claim *offline* to tell which; never send it anywhere to inspect it |

An expired JWT is INFO. A JWT with no `exp` or an `exp` years out is a bearer credential and follows the runbook.

## Entropy, And Why It Is Second

Heuristic: a run of 32+ characters from a base64/hex alphabet, with at least three character classes, no whitespace, and no dictionary word longer than 6 characters. On a real repository this fires on lockfile digests, UUIDs, git object ids, base64 images, and test fixtures at a rate that will exhaust anyone's patience in the first hundred hits.

Rules that keep it useful: run it only on files under ~256 KB, only in config-shaped or note-shaped files, and require a second signal to raise severity — an assignment (`=`, `:`), a key name containing key/token/secret/password/auth, or a `.env`-shaped filename. Entropy alone with no second signal is INFO with the line reference; entropy plus a second signal is treated as real until the user says otherwise.

## File Permissions

| Target | Passing | Detection |
|---|---|---|
| Private keys, `.env`, credential files | mode 600 (owner rw only) | `stat -c '%a %n'` (GNU) or `stat -f '%Lp %N'` (BSD) |
| Directories holding them (`~/.ssh`, config dirs) | mode 700 | same, on the directory |
| Anything group- or world-readable containing a prefix hit | never | mode ends in a digit other than 0 |

On a single-user laptop a 644 `.env` is WARNING; on a shared or multi-user host it is CRITICAL, because the exposure test in the rubric is "can someone else act with your authority". Ask nothing — infer from whether the machine has other human accounts with a home directory.

## Git History

- Present in the current tree: `git grep -n -I -e '<pattern>'`.
- Present in any past commit: `git log -p --all -S'<pattern>' --pickaxe-regex` — `-S` finds commits where the count of matches changed, which is exactly "added or removed".
- When it was added, for the access-log window: `git log --diff-filter=A --format='%H %ad' -- <path>`.
- Whether it left the machine: `git remote -v`, then whether the containing commit is an ancestor of any remote branch (`git branch -r --contains <sha>`). A secret committed and never pushed is a different severity from one that reached a shared remote, and a public remote makes it CRITICAL with compromise assumed.

Rewriting history is never automatic: it invalidates every clone, breaks open pull requests, and does nothing about the copies already fetched. Propose it with the rotation attached, never instead of it.

## Blast Radius Before Panic

Before ranking a finding, answer three questions from the credential itself: what can it do (scopes, or the role it assumes), where can it be used from (IP restriction, allowlist, VPN-only), and how long does it live (fixed expiry, rotation policy, or forever). A read-only token scoped to one public repository, restricted by IP, is WARNING. An unscoped, unrestricted, non-expiring key to a payment or cloud account is CRITICAL even in a private file, because the private file is one accidental push away.

## The Rotation Runbook

The order is not negotiable (SKILL.md Rule 4):

1. **Revoke or rotate at the issuer.** New value first if there is a live consumer; overlap the two for the shortest window that avoids an outage, then kill the old one.
2. **Prove the old one is dead** — one authenticated call that must return 401/403. A rotation nobody verified is a rotation that half happened; the console often keeps the old key active until it is explicitly deleted rather than merely "rotated".
3. **Replace the value in place with its pointer** — `env:NAME`, `keychain:id`, `1password:Vault/Item`, `ssm:/path`, `profile:name`, `file:~/path`. Match whatever the setup already uses (`secret_store`).
4. **Purge the copies** — the residue files, the log lines, the transcript, the backup, the shell history entry. Each one is its own line in the finding.
5. **Scrub history** if it was committed, and only after step 1.
6. **Check for use** between the add timestamp and the revocation, in the issuer's access or audit log. This is the step that decides whether this was a hygiene finding or an incident.
7. **Write the incident** to `~/Clawic/data/analysis/artifacts/incident-<kebab>.md` — what leaked, its scopes, exposure window, whether it was used, what changed — and add its `## Boxes` line. Nobody reconstructs this three months later from memory, and the next audit needs to know why that key is missing.

## Expiry Calendar

Tokens that expire cause an outage on a date that was knowable. When a credential is created or first inventoried, write its kind, its pointer, its owner, and its expiry if it has one into `## Credential Inventory` in `memory.md`. Warn at 14 days for anything self-service, 30 for anything that needs another human or an approval to reissue. A credential with no expiry and an age above `secret_rotation_days` is a WARNING whose action is "set a rotation date", not "rotate now".

## What Is Not A Secret

**Keep these — they are the working data of the audit:** account ids, project and org names, ARNs and resource ids, bucket, queue and repo names, usernames and emails, profile names, hostnames, region ids, the *name* of an environment variable, the last four characters of a card, public keys, key fingerprints, and a token's kind and expiry date.

**Strip these — always, everywhere:** access keys and secret keys, session tokens, passwords and passphrases, private keys and their PEM bodies, JWTs, OAuth client secrets, refresh tokens, webhook signing secrets, database connection strings containing a password, external-id values, and one-time codes.

## Write It Down

At the end of any pass here, in the same turn:

- Each credential found, with its kind, its location as a pointer, its owner, its expiry, and its rotation date → `## Credential Inventory` in `memory.md` (splits to `credentials.md`; format in `memory-template.md`).
- Each unresolved exposure → `## Open Findings`, with severity and the action from the runbook.
- Anything the user declares intentional (a demo key, a fixture) → `## Accepted`, with a scope glob and a review date.
- A real leak with an exposure window → `artifacts/incident-<kebab>.md`, plus its `## Boxes` line.
