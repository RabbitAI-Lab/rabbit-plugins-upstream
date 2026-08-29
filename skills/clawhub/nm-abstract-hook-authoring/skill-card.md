## Description:

Guide creating Claude Code hooks with security-first design for validation and enforcement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent engineers use this skill to design, test, and document Claude Code and Claude Agent SDK hooks for validation, logging, context injection, automation, and security enforcement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hook examples can enable high-impact validation, logging, HTTP, scheduling, or auto-approval behavior without enough privacy, consent, or safety guardrails.

Mitigation: Review carefully before installation or use, treat HTTP hooks as data egress, avoid logging raw tool inputs or outputs, keep auto-approval limited to narrow low-risk allowlists, and avoid putting secrets in scheduled prompts or persistent state.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-abstract-hook-authoring)
- [Clawdis Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)
- [Claude Code Hooks Documentation](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Claude Agent SDK Documentation](https://docs.anthropic.com/en/docs/claude-agent-sdk)
- [Claude Code Settings Configuration](https://docs.anthropic.com/en/docs/claude-code/settings)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON, Python, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; examples require user review before use.]

## Skill Version(s):

1.9.19 (source: server evidence release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
