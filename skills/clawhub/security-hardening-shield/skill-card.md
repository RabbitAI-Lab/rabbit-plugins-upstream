## Description:

Security Hardening Shield helps agents assess application security posture, map trust, data, and network boundaries, check OWASP Top 10 risks, audit secrets and dependencies, and produce remediation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and security reviewers use this skill to guide pre-release security hardening for applications, including input validation, authentication and authorization review, secret handling, dependency auditing, and remediation planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may cause an agent to read a target repository, run local security and dependency tools, and write audit reports.

Mitigation: Use it only in repositories where that access is acceptable, review proposed commands before execution, and inspect generated reports before relying on them.

Risk: The artifact includes optional callback_url behavior that could send results to an external endpoint.

Mitigation: Avoid callback_url unless the endpoint is trusted and the data being sent is understood.

Risk: Security tooling commands may include package installs, secret scans, or application startup commands.

Mitigation: Run commands in a controlled environment and confirm command scope before package installation, scanning, or application startup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/security-hardening-shield)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with inline code and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce security-audit.md, vulnerabilities.md, remediation.md, and dependency-audit.md style reports.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata; artifact frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
