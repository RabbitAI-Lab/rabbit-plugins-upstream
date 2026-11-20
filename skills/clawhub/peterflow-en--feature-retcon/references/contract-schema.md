# Contract, journal and recovery

One `RECONCILIATION.md` per authoritative topic marks an active round. Read its confirmed assertions, current state and journal before resuming. Preserve the template sections and machine-delimited JSON block. Normal states are `executing`, `paused`, `blocked`, `restoring`, `restored` and `ready_to_close`.

The frontmatter contains integer `schema_version` (1), `round_id`, `status`, absolute `authority_root`, `target_stage`, `completion_stage`, `created_at`, `confirmed_at`, `version_control` (`git` or `none`) and `baseline_ref` (a frozen commit SHA or null). The journal records writable roots and ordered entries. Treat legacy missing completion stages as unknown until the original decision is established. They can be inspected and restored. A legacy ready state without registered closure evidence needs fresh evidence.

## Commands

Run the helper from the installed skill directory. Substitute actual values for the arguments in angle brackets. Pass repeated writable roots when authorized.

```text
python3 scripts/contract.py init <topic> --target-stage <stage> --completion-stage <stage> --version-control <git|none> --writable-root <root> [--baseline-ref <ref>]
python3 scripts/contract.py prepare <contract> --path <file> [--recovery-mode <embed|git>] [--allow-sensitive] [--allow-large]
python3 scripts/contract.py applied <contract> --path <file>
python3 scripts/contract.py status <contract> [--set <executing|paused|blocked|restoring>]
python3 scripts/contract.py scope <contract> --target-stage <stage> [--completion-stage <stage>] [--writable-root <root>] --confirmation <decision>
python3 scripts/contract.py verify <contract>
python3 scripts/contract.py restore <contract>
python3 scripts/contract.py verify <contract> --mark-ready --evidence <closure.json>
python3 scripts/contract.py close <contract> --archive <recovery.json>
python3 scripts/contract.py inspect-recovery <recovery.json>
python3 scripts/contract.py reopen <recovery.json> --confirmation <current-undo-instruction> --writable-root <root>
```

`scope` records existing authorization, retains the same round and journal and can extend writable roots. The completion stage can stay the same or deepen. Resume a paused round explicitly using `status --set executing` after its blockers or authorization gaps are resolved.

## Before and after every edit

Use a single writer and stop relevant background jobs. `prepare` validates existing entries, resolves the target within authorized roots, screens for sensitive content, then persists the original bytes or recovery source, digest and mode. Edit the regular file. `applied` checks the result and records its state and reverse diff. `verify` checks the chain and current contents. A second write to the same file gets its own entry. Record each file involved in a directory reorganization. A file journal provides no cross-system or arbitrary concurrency isolation.

Embedded recovery stores gzip-compressed, base64-encoded bytes, including uncommitted work. The data is recoverable by anyone with access. The Git alternative requires a pinned commit whose file bytes match the actual starting state; its objects must remain available. If no HEAD exists, use embedding. When a payload exceeds 10 MiB, narrow the scope, use an eligible Git baseline, or obtain specific approval for `--allow-large`.

Sensitive candidates require per-file approval before `--allow-sensitive`. Suppressing a readable diff does not remove secrets from an embedded preimage. If sensitivity first appears after the write, `applied` records the state and blocks the round. Resolve it before resuming. Preserve permissions 0600, use a private directory, leave the contract and archive untracked, and never publish payloads. Read failures from Git must remain visible.

## Pause or recover

Pause keeps the active round, synchronization point, remaining work and required next authorization. On an explicit undo, simulate the complete reverse sequence before writing any target. Any drift, redirected path, unavailable object or corrupt payload blocks restoration. The helper records `restore_pending` before each restore write and clears it when complete. Only that recorded interruption allows an idempotent retry on an exact preimage. A later user edit that happens to match an intermediate version is still drift. If a prepared write lacks its applied record, establish ownership and actual state before continuing.

For a file move, `restore` checks the old parent paths before changing any file. It recreates missing directories under the authorized roots with mode 0700. If a file occupies a required directory, resolve the conflict before retrying. Restored files retain their recorded modes.

After `restore` verify hashes, run baseline checks, inspect active references and account for unique requirements in the contract. Close with independent restored evidence and a fresh archive.

## Close and reopen

Follow [closure evidence](closure-evidence.md). `valid` checks structure, journal, hashes, permissions and Git state. `close_ready` also requires the same round's closure evidence and current inputs. Examine both fields; a successful verify exit alone does not mean the feature is done. A completed round must reach its completion stage. A paused or blocked round stays active.

`close` verifies current inputs, saves a private archive without overwriting a different file, checks again and removes the active contract only on success. Select a path under the authorized roots with an existing parent, outside target and tracked paths. An identical archive permits retry after interruption. A mismatch keeps the active contract. Treat recovery archives as control data, never as task progress.

To undo a closed round inspect the archive identity and affected paths, record the current authorization and roots with `reopen`, then `restore`. Reopen recreates only the control record and refuses to replace a current active round. Paths remain bound to their original locations. Complete baseline and reference checks and close to a separate archive. The tool can detect drift and evidence existence; the person or agent must actually read the evidence for semantic acceptance.
