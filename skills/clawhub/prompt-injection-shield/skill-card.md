## Description:

Scans untrusted content for English and Chinese prompt-injection patterns before it enters an AI context, returning a risk score, matched rules, and handling guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0 (ClawHub listing); MIT for .py code only, with documentation and theory all rights reserved (artifact)

## Use Case:

Developers and agent operators scan retrieved pages, emails, tool outputs, and uploaded text for possible prompt injection before passing that content to an AI agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pattern-based risk scores can miss or misclassify prompt injections.

Mitigation: Treat scores as advisory and have a person review important content before acting on it.

Risk: Installing or running a third-party skill exposes the agent to publisher-supplied instructions and code.

Mitigation: Review the skill files before installation and use it only when a Chinese-first scanning workflow is needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-injection-shield)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON scan results, with Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk score (0–100), matched rules, and pass/quarantine/drop recommendation]

## Skill Version(s):

1.0.2 (source: ClawHub release; artifact declares 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
