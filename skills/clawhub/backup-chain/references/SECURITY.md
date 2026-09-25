# SECURITY — backup-chain

## Secrets in archives

The tool hashes and archives member files verbatim. If your member list
includes credentials, tokens, or keys, **every copy of every archive contains
them**, and so does every place you distribute archives to.

- `build`, `status`, and `verify` print a `SECRET-WARN` line for members whose
  basename looks credential-like (`credential*`, `*token*`, `*.pem`, `id_rsa`,
  `api_key`, …). The heuristic is a courtesy, not a guarantee — absence of a
  warning is not an audit.
- If you back up secrets: keep distribution targets **private**, prefer
  excluding secrets from members entirely (rotate what you cannot afford to
  lose), and consider a separate secret store with its own chain.
- Worklogs and notes are secrets too, more often than people expect — they
  quote endpoints, handles, and half a credential before anyone thought to
  redact. Review the member list (`status`) with that in mind.

## Ledger command adapter

`--ledger command` executes **your** commands — read via stdout, append
with the entry piped to stdin. This is the git-hook trust class:

- Commands run from the user's own config file, as argv vectors (`shlex`-split,
  `shell=False`) — never through a shell. Pipes, redirects and globs are inert
  unless the config names a shell itself (`sh -c '…'`), in plain sight in the
  WARN preview. Anyone who can write that config can run the program it names.
  Treat `.vault/config.json` as code.
- **Refuse-by-default (since 1.0.4, audit T09 round 3):** a warning is not
  consent. Every invocation that would execute a configured command must pass
  `--allow-cmd-ledger`. Without it, the read path is reported unreachable with
  guidance (status/check degrade to the marked-skip fencing semantics) and
  `build --register` fails loudly — a workspace-contributed config can no
  longer fire on a routine subcommand. The flag is per-invocation by design:
  automation passes it only inside scripts the operator has reviewed.
- **Runtime visibility (since 1.0.3):** every adapter execution prints a `WARN`
  line to stderr naming the executed command (`read_cmd` / `append_cmd`) and a
  truncated preview, once per command per process (since 1.0.4 it fires only
  after the opt-in). Warnings go to stderr only — stdout (JSON checks, ledger
  parsing) stays clean. If you see this warning in a workspace whose
  `.vault/config.json` you did not review, treat the workspace as hostile and
  stop.
- The tool adds no environment, no secrets, no network. Whatever your commands
  can reach, the adapter can touch; nothing more, nothing less.
- Review commands at `init` and after any config edit. On shared channels,
  filter for your identity inside the read command — the ledger parser trusts
  any line shaped like an entry, so one-issuer depends on your filter.

## Restore discipline

- Restore **refuses** to overwrite differing files without `--overwrite`, and
  refuses fencing-refused archives without `--force`. Both refusals print why;
  both are the tool working.
- Restore targets are validated: `/` and the home directory are refused outright.
- Every extracted file is verified against the manifest's member map before it
  is renamed into place; a failed member leaves the workspace **not** healed
  and exits non-zero. Do not build on a partial heal.

## Trust boundaries

- **No network.** No sockets anywhere in the script. Off-site copies are made
  by the user; verification of those copies is the roundtrip pattern in
  `references/PROTOCOL.md`.
- **No content inspection.** Member bytes are hashed and streamed. Nothing is
  parsed, logged, or transmitted. Worklog-style metadata (manifest `carries`
  notes) is the only text the tool handles beyond paths and hashes — keep
  secrets out of the notes.
- **Archive path safety.** Names are validated on every read (absolute paths,
  `..`, NUL, backslash-normalized members). Extraction is bounded to
  `--target` in both senses: the names, and the filesystem — a pre-existing
  symlinked directory beneath the target would redirect writes outside it,
  so restore refuses (exit 2, unconditional) when any destination component
  under the target is a symlink, and a symlink at the final component is a
  conflict replaced only via `--overwrite` (which swaps the link itself,
  never the link target).
- **Symlinks** given directly as a member path are skipped (warned) — you are
  told, and nothing is silently dereferenced at the top level. A symlinked
  *file* found while walking a directory member is dereferenced **only if
  its resolved target stays inside the project root** (checked with
  `realpath` + `commonpath`, never string prefixes): the archive stores the
  link target's current content, and the manifest hash is computed over that
  same content — both must agree, or every restore drill on that member
  would fail. A link resolving *outside* the root is skipped with a warning
  and never enters the manifest — whatever backs it was not part of what
  you selected, and no archive content can escape the declared read boundary
  through a link planted inside a member directory. A *broken* symlink found
  the same way is skipped with a warning and never enters the manifest at
  all, so there is no member for the listing check to flag — it is absent by
  exclusion, not by silent corruption.
- **Non-regular files** (FIFOs, sockets, devices — including symlinks pointing
  at them) are skipped with a warning: hashing them would hang the build or
  crash it, and no archive format here would represent them honestly anyway.

## Known limitations (stated, not hidden)

- The symlink boundary checks validate a path, then use it: a process that
  swaps the link between the check and the read/write (TOCTOU) is not
  defended against. That would require O_NOFOLLOW / descriptor-relative
  I/O throughout, which the threat model here does not call for — the
  adversary is infrastructure amnesia, not a local process racing the
  backup. Stated so you can decide differently for your own deployment.

- The manifest is inside the archive and the chain is hash-linked, but nothing
  signs anything: an attacker who controls the machine at build time controls
  the archive. The protocol detects accidents and infrastructure amnesia, not
  malice with build-time access.
- The `file` ledger inside the workspace dies with the workspace by design —
  use `--ledger-file` outside the machine for real protection, and treat the
  in-workspace ledger as a test convenience.
- Generation uniqueness across **different machines/chains** requires distinct
  ledger channels; two chains sharing one ledger will fight over the counter
  (and, being append-only, will be visible doing it).
