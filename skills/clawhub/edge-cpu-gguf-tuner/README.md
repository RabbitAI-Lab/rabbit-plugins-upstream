# ⚙️ Edge Cpu Gguf Tuner

**Category:** automation, productivity, research

## ✨ What This Skill Does
Tunes llama.cpp GGUF inference on CPU-only / edge machines (1-4 cores, low RAM) for maximum tokens/sec, with measured CPU-specific findings for flash attention, KV-cache quantization, batch size, and quant choices.

## 🔐 Permissions & Requirements
• Runs llama.cpp binaries locally
• Loads GGUF model files (read)
• No network calls except optional model downloads
• Requires: cmake/g++ if building llama.cpp

## 🔒 Security & Privacy
  - Runs local inference only; your prompts stay on-machine.
  - Model files are loaded locally; nothing is sent to the cloud.
  - No secrets are involved.

## ✅ Verification Hash
Installers can verify this skill matches the published artifact by hashing the
skill files and comparing to the digest below:

- **SHA-256:** `9d210d612c7b6c304d75988227b374bce6fd9ef002fb46c04e05c5862aba2a0a`

Verify locally:

```bash
sha256sum SKILL.md README.md
# compare the output to the SHA-256 above.
```

---
*Generated under the Skill Publishing Standard. See SKILL_PUBLISHING_STANDARD.md.*
