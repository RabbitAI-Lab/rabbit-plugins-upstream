# 🚀 Antigravity CLI Skill for OpenClaw

[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://clawhub.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Google Antigravity](https://img.shields.io/badge/Google-Antigravity-green)](https://antigravity.google)

> **Autonomous coding agent from Google** — code generation, refactoring, debugging, and multi-step programming tasks

## About

This skill integrates Google's [Antigravity CLI](https://antigravity.google) (`agy`) with OpenClaw, providing autonomous coding capabilities as an alternative to Claude Code or other coding agents.

**Key Features:**
- 🤖 **Autonomous code editing** — multi-file changes with context awareness
- 🧠 **Multi-step reasoning** — complex refactoring and debugging
- 💰 **FREE** — uses Google AI Studio account limits (no subscription)
- 🔧 **Flexible output** — text, JSON, or streaming JSON
- 📁 **Project context** — understands your codebase structure

## Installation

### Prerequisites

- Node.js 20+ (for OpenClaw)
- Internet connection
- Google account (for authentication)

### Install Antigravity CLI

```bash
# Linux / macOS
curl -fsSL https://antigravity.google/cli/install.sh | bash

# Windows (PowerShell)
irm https://antigravity.google/cli/install.ps1 | iex

# Verify
agy --version
```

### Install Skill

```bash
# From ClawHub (when published)
openclaw skills install antigravity-cli

# From GitHub
openclaw skills install git:akdira/openclaw-skill-antigravity-cli

# Manual installation
git clone https://github.com/akdira/openclaw-skill-antigravity-cli.git ~/.openclaw/workspace/skills/antigravity-cli
```

## Authentication

First-time setup requires interactive OAuth login:

```bash
# Run interactive mode
agy

# Follow prompts:
# 1. Select "Google OAuth"
# 2. Open URL in browser
# 3. Sign in with Google account
# 4. Copy authorization code
# 5. Paste back into terminal
```

After authentication, headless mode works without interaction.

## Usage

### Basic Usage

```bash
# Single prompt
agy -p "Explain what this function does"

# Code generation
agy -p "Create a Python Flask API with CRUD endpoints"

# Code review
agy -p "Review src/ for security vulnerabilities" --effort high

# Refactoring
agy -p "Refactor authentication to use JWT" --mode accept-edits
```

### Advanced Usage

```bash
# With file context
agy -p "Review all Python files" --add-dir /path/to/project

# Model selection
agy -p "Complex task" --model gemini-2.5-pro

# JSON output
agy -p "List all functions" --output-format json

# Structured output
agy -p "Parse version v2.14.3" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"major":{"type":"integer"},"minor":{"type":"integer"},"patch":{"type":"integer"}}}'
```

### In OpenClaw Sub-Agents

```javascript
// Delegate coding task to Antigravity CLI
sessions_spawn({
  task: `You are a coding agent. Use Antigravity CLI:
  
  Task: Implement user authentication
  Files: src/auth.js, src/models/user.js
  
  Run: agy -p "implement JWT authentication" --add-dir ./src`
})
```

## Examples

See the [`examples/`](./examples/) directory for detailed use cases:

- [`code-generation.md`](./examples/code-generation.md) — Generate complete applications
- [`code-review.md`](./examples/code-review.md) — Security and performance audits
- [`refactoring.md`](./examples/refactoring.md) — Multi-file refactoring
- [`debugging.md`](./examples/debugging.md) — Bug investigation and fixes
- [`test-generation.md`](./examples/test-generation.md) — Unit test creation

## Configuration

Edit `~/.gemini/antigravity-cli/settings.json`:

```json
{
  "theme": "dark",
  "model": "gemini-2.5-pro",
  "effort": "medium"
}
```

## Billing & Limits

**FREE** — no subscription cost.

- Uses Google AI Studio account quota
- Rate limits: RPM, TPM, RPD (check at https://aistudio.google.com/)
- Free tier = rate limited, not paid
- If billing enabled on project, you'll be charged per token

## Troubleshooting

### Common Issues

**"authentication required"**
```bash
# Run interactive mode to authenticate
agy
```

**"command not found: agy"**
```bash
# Add to PATH
export PATH="$HOME/.local/bin:$PATH"
```

**"rate limit exceeded"**
- Wait for quota reset
- Check limits at https://aistudio.google.com/

See [SKILL.md](./SKILL.md) for complete troubleshooting guide.

## Comparison: Antigravity CLI vs Claude Code

| Feature | Antigravity CLI | Claude Code |
|---------|-----------------|-------------|
| **Provider** | Google | Anthropic |
| **Cost** | FREE (rate limited) | Subscription (flat-rate) |
| **Models** | Gemini 2.5 Pro/Flash | Claude 3.5 Sonnet/Opus |
| **Headless mode** | ✅ `agy -p` | ✅ `claude --print` |
| **Interactive mode** | ✅ TUI | ✅ TUI |
| **File context** | ✅ `--add-dir` | ✅ Auto-detect |
| **JSON output** | ✅ Multiple formats | ✅ JSON |
| **Best for** | Google ecosystem, free usage | Default choice, complex tasks |

**Recommendation:** Use Claude Code as default, Antigravity CLI as backup or for Google-specific tasks.

## Resources

- **Official Docs:** https://antigravity.google/docs/
- **GitHub Repo:** https://github.com/google-antigravity/antigravity-cli
- **Google AI Studio:** https://aistudio.google.com/
- **OpenClaw Docs:** https://docs.openclaw.ai

## License

This skill is licensed under MIT License. Antigravity CLI itself is © Google.

## Contributing

Contributions welcome! Please open an issue or PR on [GitHub](https://github.com/akdira/openclaw-skill-antigravity-cli).

## Support

- **Issues:** https://github.com/akdira/openclaw-skill-antigravity-cli/issues
- **Discussions:** https://github.com/akdira/openclaw-skill-antigravity-cli/discussions

---

Made with ❤️ by [PT Akdira Labs International](https://akdira.id)
