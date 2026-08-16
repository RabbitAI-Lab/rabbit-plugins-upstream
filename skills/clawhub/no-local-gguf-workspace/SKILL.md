---
name: no-local-gguf-workspace
description: Operate the carminic-acid Arena workspace at full capability without cloning llama.cpp, building llama binaries, or downloading offline Qwen/DeepSeek GGUF models. Final answers come only from stored capable-model API keys.
version: 1.0.0
categories: [operations, agents, development]
topics: [workspace, llama.cpp, gguf, routing, snapshot-budget]
metadata:
  openclaw:
    emoji: "🪶"
    requires:
      bins: [bash, python3]
---

# 🪶 no-local-gguf-workspace

## When to use

Use this skill when the human asks for a **full workspace rebuild** and also says **do not install llama.cpp** and **do not download offline Qwen / DeepSeek GGUF models**.

## What it does

1. Rebuilds every workspace surface except local inference:
   scripts, tools, secrets, 3 always-on skills, RAG frameworks, TDAI, OpenClaw, micromamba docking env, Colab CLI wrapper, GitHub job token.
2. Sets `SKIP_LOCAL_MODELS=1` and `ENSURE_SKIP_LLAMA_BUILD=1` so `ensure_workspace.sh` does not clone, build, or download GGUFs.
3. Routes every final answer through `tools/router.py` / `orchestrate_answer.sh`.
4. Treats self_grade T1–T5 FAIL as **expected**, not as a broken workspace.
5. Keeps TDAI stopped while importing heavy Python stacks on the 2 GB box.

## Commands

```bash
export SKIP_LOCAL_MODELS=1
export ENSURE_SKIP_LLAMA_BUILD=1
bash /home/user/ensure_workspace.sh
python3 /home/user/tools/router.py --check
bash /home/user/orchestrate_answer.sh "QUESTION" --task general
```

## Never

- Never present swarm / local-model text as the final answer.
- Never download the four STEP-9 GGUFs when this skill is active.
- Never clone `ggerganov/llama.cpp` when this skill is active.
- Never run `rag_tool.py --status` via `__import__` of torch-class packages on a 2 GB box with TDAI up.

## Verification

- `test ! -e /home/user/llama.cpp && test ! -e /home/user/out/llama.cpp`
- `find /home/user/out/models -name '*.gguf' | wc -l` equals 0
- `python3 tools/router.py --check` shows reachable providers
- `self_grade.sh` T6–T12 PASS; T1–T5 FAIL expected
