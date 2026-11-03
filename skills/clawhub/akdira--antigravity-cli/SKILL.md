---
name: antigravity-cli
version: "1.0.0"
description: "Use this skill when you need a coding agent from Google for code generation, refactoring, review, debugging, or any programming task. Antigravity CLI (agy) is Google's official terminal-based AI coding assistant that provides autonomous code editing, multi-step reasoning, and file manipulation. Trigger when user mentions 'coding agent', 'code generation', 'refactor code', 'debug code', 'review code', or needs autonomous programming assistance."
homepage: "https://antigravity.google"
metadata:
  openclaw:
    emoji: "🚀"
    requires:
      bins: ["agy"]
    install:
      - id: "curl"
        kind: "curl"
        url: "https://antigravity.google/cli/install.sh"
        bins: ["agy"]
        label: "Install Antigravity CLI (curl)"
    dependencies:
      auth: "First interactive run triggers OAuth login flow. Credentials stored in ~/.gemini/antigravity-oauth-token"
      network: "Requires internet access to Google AI endpoints"
      model-availability: "Models available at runtime may vary; check `agy models` for current list"
---

# Antigravity CLI Skill

Use Google's Antigravity CLI (`agy`) as an autonomous coding agent for code generation, refactoring, debugging, and multi-step programming tasks.

## When to Use

- User asks to **generate, refactor, debug, or review code**
- User needs **autonomous code editing** across multiple files
- User wants a **Google-based coding agent** (alternative to Claude Code)
- User mentions **"coding agent"**, **"code generation"**, **"refactor"**, **"debug"**, **"review code"**
- Task requires **multi-step reasoning** about code structure
- **NOT for:** Simple file reads, grep searches, or basic edits (use direct tools instead)

## Prerequisites

| Requirement | Detail |
|-------------|--------|
| Binary | `agy` must be installed at `/root/.local/bin/agy` or in PATH |
| Authentication | OAuth login required (one-time interactive setup) |
| Network | Internet access to Google AI endpoints |
| Billing | **FREE** — uses Google AI Studio account limits (no subscription cost) |

## Installation

### Linux / macOS (Recommended)

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

This installs `agy` to `~/.local/bin/agy` and adds it to PATH.

### Windows (PowerShell)

```powershell
irm https://antigravity.google/cli/install.ps1 | iex
```

### Windows (CMD)

```cmd
curl -fsSL https://antigravity.google/cli/install.cmd -o install.cmd && install.cmd && del install.cmd
```

### Verify Installation

```bash
agy --version
# Expected output: 1.1.21 (or newer)
```

## Authentication

**First-time setup requires interactive OAuth login:**

```bash
# Run interactive mode (requires TTY)
agy

# Follow the prompts:
# 1. Select "Google OAuth"
# 2. Open the provided URL in your browser
# 3. Sign in with your Google account
# 4. Copy the authorization code
# 5. Paste it back into the terminal
```

**After authentication**, credentials are cached at `~/.gemini/antigravity-oauth-token` and headless mode works without interaction.

**Headless environments (SSH, CI/CD):** If you can't run interactive mode, you can use `GOOGLE_API_KEY` environment variable:

```bash
export GOOGLE_API_KEY="your-api-key-here"
agy -p "test prompt"
```

## Usage Patterns

### 1. Headless Mode (Non-Interactive)

**Best for:** Scripts, automation, sub-agent delegation

```bash
# Single prompt, text output (default)
agy -p "Explain what this function does"

# Capture output to variable
result=$(agy -p "Generate a Python function to calculate fibonacci")

# Redirect to file
agy -p "Write unit tests for main.py" > tests.md
```

### 2. Interactive Mode (TTY Required)

**Best for:** Development sessions, iterative coding

```bash
# Launch interactive TUI
cd /path/to/project
agy

# Then type prompts directly in the TUI
```

### 3. Model Selection

```bash
# Use specific model
agy -p "Refactor this code" --model gemini-2.5-pro

# List available models
agy models
```

**Available models (as of 2026):**
- `gemini-2.5-pro` — Most capable, best for complex tasks
- `gemini-2.5-flash` — Faster, good for simple tasks

### 4. File Context

```bash
# Add directory to workspace context
agy -p "Review all Python files" --add-dir /path/to/project

# Multiple directories
agy -p "Compare implementations" --add-dir ./frontend --add-dir ./backend
```

### 5. Effort Level

```bash
# Low effort — quick answers, less thorough
agy -p "Quick syntax check" --effort low

# Medium effort — balanced (default)
agy -p "Refactor this function" --effort medium

# High effort — deep analysis, comprehensive
agy -p "Full code review with security audit" --effort high
```

### 6. Output Formats

```bash
# Text (default) — human-readable
agy -p "Explain this code"

# JSON — structured output with metadata
agy -p "List all functions in this file" --output-format json

# Stream JSON — real-time events (for monitoring)
agy -p "Analyze this project" --output-format stream-json
```

**JSON output includes:**
```json
{
  "conversation_id": "uuid",
  "status": "SUCCESS",
  "response": "The agent's response text",
  "duration_seconds": 7.16,
  "num_turns": 1,
  "usage": {
    "input_tokens": 10415,
    "output_tokens": 657,
    "total_tokens": 11072
  }
}
```

### 7. Structured Output (JSON Schema)

```bash
agy -p "Parse version v2.14.3 into major, minor, patch" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"major":{"type":"integer"},"minor":{"type":"integer"},"patch":{"type":"integer"}},"required":["major","minor","patch"]}'
```

### 8. Permission Modes

```bash
# Auto-approve all tool actions (USE WITH CAUTION)
agy -p "Refactor entire project" --dangerously-skip-permissions

# Plan mode — only suggest, don't execute
agy -p "How would you fix this bug?" --mode plan

# Accept edits — auto-apply suggested changes
agy -p "Fix all linting errors" --mode accept-edits
```

## Examples

### Example 1: Code Generation

```bash
agy -p "Create a Python Flask API with endpoints for CRUD operations on a User model. Include proper error handling and validation."
```

### Example 2: Code Review

```bash
agy -p "Review the code in src/ directory. Check for:
1. Security vulnerabilities
2. Performance issues
3. Code style violations
4. Missing error handling
Provide specific file:line references for each issue." --effort high
```

### Example 3: Refactoring

```bash
cd /path/to/project
agy -p "Refactor the authentication module to use JWT tokens instead of session cookies. Update all related tests." --mode accept-edits
```

### Example 4: Debugging

```bash
agy -p "The function calculateTotal() in src/cart.js returns NaN when the cart is empty. Debug and fix this issue. Add proper null checks."
```

### Example 5: Test Generation

```bash
agy -p "Generate comprehensive unit tests for src/utils/validation.js. Cover edge cases, error conditions, and happy paths. Use Jest framework."
```

### Example 6: Documentation

```bash
agy -p "Generate JSDoc comments for all exported functions in src/api/*.js. Include @param, @returns, and @example tags."
```

### Example 7: Multi-File Changes

```bash
agy -p "Migrate the database layer from MongoDB to PostgreSQL. Update:
- All model files in src/models/
- All query functions in src/db/
- All tests in tests/
- Database config in src/config/
Keep the same API interface." --add-dir ./src --add-dir ./tests
```

## Troubleshooting

### Error: "authentication required"

**Cause:** Not authenticated or token expired

**Solution:**
```bash
# Run interactive mode to authenticate
agy

# Or set API key
export GOOGLE_API_KEY="your-key"
```

### Error: "bubbletea: error opening TTY"

**Cause:** Running interactive mode in non-TTY environment

**Solution:** Use headless mode instead:
```bash
agy -p "your prompt"
```

### Error: "command not found: agy"

**Cause:** Binary not in PATH

**Solution:**
```bash
# Add to PATH
export PATH="$HOME/.local/bin:$PATH"

# Or use full path
/root/.local/bin/agy -p "prompt"
```

### Error: "rate limit exceeded"

**Cause:** Hit Google AI Studio quota

**Solution:**
- Wait for quota reset (usually hourly/daily)
- Check limits at https://aistudio.google.com/
- Consider upgrading to paid tier if needed

### Headless mode hangs or times out

**Cause:** Complex task or permission prompt

**Solution:**
```bash
# Increase timeout
agy -p "complex task" --print-timeout 10m

# Or auto-approve permissions (use with caution)
agy -p "task" --dangerously-skip-permissions
```

## Billing & Limits

**Antigravity CLI is FREE** — no subscription cost.

**Limits:**
- Uses your Google AI Studio account quota
- Rate limits: RPM (requests per minute), TPM (tokens per minute), RPD (requests per day)
- Check your limits: https://aistudio.google.com/
- Free tier = rate limited, not paid

**Important:**
- If your Google Cloud project has billing enabled, you'll be charged per token
- For free usage, ensure billing is NOT enabled on the project
- Multiple API keys in same project share the same quota

## Integration with OpenClaw

### Using in Sub-Agents

When spawning sub-agents for coding tasks, you can delegate to Antigravity CLI:

```javascript
// In sub-agent task
sessions_spawn({
  task: `You are a coding agent. Use Antigravity CLI for implementation:
  
  Task: ${taskDescription}
  Files: ${relevantFiles}
  
  Run: agy -p "implement the task" --add-dir /path/to/project`
})
```

### Combining with Claude Code

Both Antigravity CLI and Claude Code can be used:

```bash
# Claude Code (default, subscription-based)
claude --permission-mode bypassPermissions --print "refactor code"

# Antigravity CLI (free, Google-based)
agy -p "refactor code"
```

**When to use which:**
- **Claude Code** — Default choice, flat-rate subscription
- **Antigravity CLI** — Alternative when Claude limit exhausted, or for Google ecosystem tasks

## Configuration

**Config file:** `~/.gemini/antigravity-cli/settings.json`

```json
{
  "theme": "dark",
  "model": "gemini-2.5-pro",
  "effort": "medium"
}
```

**View/edit config:**
```bash
# Interactive config editor
agy
# Then type: /config

# Or edit file directly
nano ~/.gemini/antigravity-cli/settings.json
```

## Resources

- **Official Docs:** https://antigravity.google/docs/
- **GitHub Repo:** https://github.com/google-antigravity/antigravity-cli
- **Google AI Studio:** https://aistudio.google.com/
- **Rate Limits:** https://ai.google.dev/gemini-api/docs/rate-limits

## License

This skill is provided under MIT License. Antigravity CLI itself is © Google.
