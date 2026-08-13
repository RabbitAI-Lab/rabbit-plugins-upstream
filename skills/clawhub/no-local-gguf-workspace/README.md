# 🪶 no-local-gguf-workspace

Full carminic-acid Arena workspace operation **without** llama.cpp and **without** offline Qwen / DeepSeek GGUF models.

## What it does

This skill records the 2026-08-12 owner directive: rebuild every workspace subsystem except local GGUF inference. It documents the environment flags, the expected self-grade pattern, the capable-model answer path, and the 2 GB RAM coexistence rule with TencentDB Agent Memory.

Functionality:

- Sets `SKIP_LOCAL_MODELS=1` and `ENSURE_SKIP_LLAMA_BUILD=1` before `ensure_workspace.sh`.
- Confirms llama.cpp is absent and `out/models/` contains no `.gguf` files.
- Routes every final answer through `tools/router.py` using only stored keys in `secrets/api_credentials.json`.
- Marks self_grade T1–T5 as expected FAIL and T6–T12 as the real health gate.
- Stops TDAI containers before any torch-class Python import on the 2 GB sandbox.

## 🔐 Permissions / requirements

- Reads `/home/user/ensure_workspace.sh`, `/home/user/tools/router.py`, `/home/user/secrets/api_credentials.json`.
- Runs `bash`, `python3`, and optionally `docker` via `tools/start_tdai.sh`.
- Does **not** request new API keys. Uses only keys already stored in the private workspace secret store.
- Network: outbound calls only to providers already listed in `tools/router.py` when answering questions.
- Does **not** write models into `/home/user`. Models, if ever enabled later, stay in `/home/user/out/models`.

## 🔒 Security & Privacy

- Data read: workspace scripts, healer flags, router health. No user documents are uploaded by this skill itself.
- Data sent: only if the operator then runs `orchestrate_answer.sh` / `router.py`, which send the prompt to a stored free-tier provider. This skill does not add extra telemetry.
- Secrets: never logged. Runtime credential copies stay chmod 600 under `.config/` and `.clawhub/`.
- Risks: leaving `SKIP_LOCAL_MODELS=0` by accident would download ~2.4 GB of GGUFs and clone llama.cpp. Always export the skip flags in this mode.
- Review before install: read `SKILL.md` in full. There are no executable payloads besides documented shell commands.

## ✅ Verification hash

SHA-256 of `SKILL.md`:

```
92a68c60c22f551a2d599a9e5c3c151598bb7bc5a72cfab528076d5fa3ba4423
```

Verify locally:

```bash
sha256sum SKILL.md
# expected: 92a68c60c22f551a2d599a9e5c3c151598bb7bc5a72cfab528076d5fa3ba4423
```
