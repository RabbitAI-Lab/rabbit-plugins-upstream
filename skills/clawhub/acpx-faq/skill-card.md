## Description:

Run coding agents (codex, claude, agy/Antigravity) through the acpx ACP CLI - the headless lane outside a herdr pane (no HERDR_ENV). Use before launching or prompting a subagent, and when a command fails, a session is not found, or a prompt is lost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to run and troubleshoot headless coding-agent sessions through acpx, including command syntax, session lifecycle, agent-specific setup, MCP configuration, failure detection, and teardown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Headless coding-agent runs can act in the user's local account and project directory without further approval.

Mitigation: Run untrusted or sensitive work in a disposable worktree, container, VM, or restricted OS account, and avoid exposing home directories, credentials, browser profiles, and service sockets.

Risk: Persistent sessions can leave resident adapter and agent processes after a run.

Mitigation: Prefer one-shot exec runs when possible and close named sessions after use.

Risk: Successful-looking exits may still hide truncated runs, content-filter stops, or MCP load failures.

Mitigation: Read the full stream, require a result file for important work, and check logs for MCP load failures before trusting completion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/acpx-faq)
- [Skill homepage](https://github.com/tenequm/skills/tree/main/skills/acpx-faq)
- [acpx project](https://github.com/openclaw/acpx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with shell and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.5.1 (source: frontmatter, release evidence, changelog released 2026-09-11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
