# Overview and Workflows

Surface choice and shared harness: `references/config-platform.md`. Step detail: `references/best-practices.md`.

| Need | Prefer |
| --- | --- |
| Fast local terminal iteration | CLI |
| SSH, headless, tmux, multiplexers | CLI |
| Scriptable one-shot prompts | CLI |
| Visual project management | Antigravity 2.0 |
| Rich desktop artifact review | Antigravity 2.0 |
| Continue a complex terminal session visually | Export to Antigravity 2.0 |

## Workflow

Complex change:

1. Ask the agent to explore and name constraints.
2. Ask for a plan, or use `/plan`.
3. Review artifacts before approving multi-file edits.
4. Give a local check: `npm test`, `pytest`, `go test ./...`, or the project build.
5. Let the agent iterate on that output.

Small change: use a direct prompt or `agy -p`, keep the scope narrow, and ask for the summary plus the check result.

## Session and automation

`Esc` stops a wrong turn. `/rewind` returns to an earlier message. `/fork` tries an experiment. `/resume` returns to the stable thread. Background subagents cover broad search and parallel cleanup.

Print mode needs the output contract in the prompt. Launch from the repo.

```bash
agy -p "Review this git diff and produce a conventional commit message. Output only the commit title and body."
agy -p "Implement the requested refactor, then run npm test and summarize the result."
```
