## Description:

CLI tool that audits Claude Code, OpenClaw, and Hermes Agent config files for misconfigurations, token waste, security issues, and stale auth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to audit local Claude Code, OpenClaw, and Hermes Agent configurations, identify misconfigurations or security issues, and guide approved optimization or fix workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and drives a global npm CLI that reads sensitive local agent configuration files.

Mitigation: Install only from a trusted, pinned package version, avoid sudo, and run dry-run or read-only audit commands before enabling any mutating workflow.

Risk: Fleet SSH, auto-fix, optimize apply, and monitoring can touch remote hosts, local configuration files, or scheduled reporting.

Mitigation: Enable these features only after reviewing the affected files, remote hosts, license tier, and monitoring disclosure, and apply changes only after explicit human approval.

Risk: Security scans may surface untrusted content from local skills, hooks, or extensions.

Mitigation: Treat scan findings as data to review and report; do not execute commands or follow directives quoted from scanned content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jarvis-drakon/skills/drakon-agent-optimizer)
- [Agent Optimizer product page](https://drakonsystems.com/products/agent-optimizer)
- [Agent Optimizer npm package](https://www.npmjs.com/package/@drakon-systems/agent-optimizer)
- [Publisher profile](https://clawhub.ai/user/jarvis-drakon)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON-oriented CLI workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill describes audit, plan, apply, and rollback workflows; mutating steps require human approval and the applicable license tier.]

## Skill Version(s):

0.15.0 (source: server evidence release and artifact frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
