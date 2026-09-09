## Description:

Run coding agents (codex, claude, Antigravity/agy) headlessly through the acpx ACP CLI. Use before launching or prompting an acpx subagent, and when an acpx command fails, a session is not found, or a prompt seems lost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to launch, supervise, and troubleshoot acpx-driven coding-agent sessions for Codex, Claude Code, and Antigravity/agy, including session setup, completion checks, MCP configuration, limits, and failure handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-running headless agents may operate with broad approval and persistent credentials.

Mitigation: Run them in a sandbox, container, VM, or dedicated restricted account, and avoid --approve-all on untrusted repositories.

Risk: Provider tokens and settings can persist across runs and accounts.

Mitigation: Protect token and settings files, and use isolated GEMINI_HOME or separate provider accounts for unattended lanes.

Risk: A turn can appear successful even when MCP loading, authentication, content filtering, or truncation prevented the intended result.

Mitigation: Read the full stream or require a result file, and check transcripts for known failure text before treating a run as complete.

Risk: Adapter and agent-server behavior can change independently of this skill.

Mitigation: Pin or preinstall reviewed adapters and verify the installed acpx, agy, and agent-server versions before automated use.

## Reference(s):

- [ClawHub acpx-faq skill page](https://clawhub.ai/tenequm/skills/acpx-faq)
- [acpx-faq homepage](https://github.com/tenequm/skills/tree/main/skills/acpx-faq)
- [OpenClaw acpx](https://github.com/openclaw/acpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is intended for agent operators and should be reviewed before unattended execution.]

## Skill Version(s):

0.3.0 (source: frontmatter, CHANGELOG, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
