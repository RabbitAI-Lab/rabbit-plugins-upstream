## Description:

Security checks for external content - downloads, fetched documents, attachments, and newly imported resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-hussein](https://clawhub.ai/user/z-hussein)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agent operators use this skill to handle downloads, fetched documents, attachments, imported resources, and full-system security checks with a conservative evidence-before-trust posture.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security guidance can be misapplied outside the requested scope or used to run broad host checks without consent.

Mitigation: Require an explicit bounded scope and user confirmation before host-wide enumeration or full-system checks.

Risk: External content may contain instructions, hidden directives, or malicious payloads that try to influence the agent.

Mitigation: Treat external content as data, isolate it before processing, verify source and integrity, and decline to execute untrusted content.

Risk: Security reports can accidentally expose credentials, raw payloads, or sensitive configuration details.

Mitigation: Summarize findings without raw secrets or exploit payloads and keep verification logs concise.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/z-hussein/skills/security-shield)
- [Attack Patterns Reference](references/attack.patterns.md)
- [Security Audit Checklist](references/audit-checklist.md)
- [Cryptography & Security Examples](references/crypto-examples.md)
- [Modern Security Tools Reference](references/modern-tools.md)
- [Security Best Practices Reference](references/security-best-practices.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with checklists and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Security summaries should avoid raw secrets, raw payloads, and unnecessary sensitive configuration details.]

## Skill Version(s):

2.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
