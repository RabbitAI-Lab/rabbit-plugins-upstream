---
name: dsh-unlimited-ocr-skill-setup
description: Install, launch, configure, and verify the Aidenwu0209/dsh-Unlimited-OCR-Skill native DeepSeek Harness bundle. Use when a user wants Unlimited-OCR with the DSH Settings GUI, Baidu Cloud or local-provider selection, and a native parsing tool.
license: MIT-0
metadata:
  author: Aidenwu0209
  repository: https://github.com/Aidenwu0209/dsh-Unlimited-OCR-Skill
  version: "1.0.0"
  openclaw:
    emoji: "🛠️"
    homepage: https://github.com/Aidenwu0209/dsh-Unlimited-OCR-Skill
---

# Set up DSH Unlimited-OCR Skill

Install the native DeepSeek Harness bundle. Do not present it as an OpenClaw
code plugin; this setup skill guides installation into DSH.

## Install and launch

1. Check Node.js 22.19+, Python 3.9+, `npx`, and `uv`. Explain any missing
   prerequisite before using its official installer. Do not use `sudo` or
   change unrelated settings without permission.
2. Run:

   ```bash
   npx @deepseek-ai/dsh plugin --profile web add "github:Aidenwu0209/dsh-Unlimited-OCR-Skill#main"
   npx @deepseek-ai/dsh web
   ```

3. Wait for the real local Web URL, open it, and confirm that **Settings →
   Unlimited-OCR** is visible.
4. Confirm that the official model repository, cloud API, authentication, and
   local-deployment links are visible and clickable.

## Configure safely

- Ask the user to choose Baidu Cloud or a local/OpenAI-compatible service.
- Store API keys through DSH Credentials; never echo, log, or place them in
  ordinary settings or source files.
- For local mode, allow loopback HTTP or remote HTTPS only.
- Do not claim success unless the plugin install succeeded, the Web URL
  responded, and the Settings panel was actually visible.

Report prerequisite versions, commands, the Web URL, provider status, and any
values still required from the user.
