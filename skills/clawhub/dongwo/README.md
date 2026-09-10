# Dongwo（懂我）

A zero-service, Markdown-based preference memory shared by coding agents.

Dongwo uses lifecycle hooks plus a small Python standard-library engine to:

- capture user prompts into separate per-agent inboxes;
- redact common secrets before storage;
- distinguish explicit preferences, stable observations, and unresolved items;
- rebuild an auditable Markdown memory;
- inject a short context snapshot into Codex and Claude Code.

## Install

```bash
clawhub install @cutd/dongwo
cd skills/dongwo
python3 scripts/setup.py --root /path/to/project
```

The setup helper installs the engine under `.dongwo/` and prints configuration
snippets. It deliberately does not overwrite existing Codex or Claude Code
configuration.

## Privacy

The published package contains only code and documentation. It does **not**
contain the author's profile, prompt inbox, generated context, or personal
memory.

Keep these local and private:

- `myprofile.md`
- `.dongwo/memory/`
- legacy `03_Projects/15_懂我/memory/`

## Requirements

- Python 3.10+
- macOS or Linux (`fcntl` file locking)
- a client that supports lifecycle command hooks for automatic capture/injection

## License

Skills published on ClawHub use the registry's default MIT-0 license.
