## Description:

Helps developers scan code for vulnerabilities and secrets, review third-party skills, and assess shell command risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafter](https://clawhub.ai/user/rafter)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to scan repositories for vulnerabilities and secrets, review untrusted extensions, and evaluate shell commands before running them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote scans may share code or metadata with Rafter's service.

Mitigation: Review what will be scanned before enabling remote scans with RAFTER_API_KEY; use the local secrets scan when remote sharing is not appropriate.

Risk: Opt-in agent initialization can add persistent security hooks or audit logging.

Mitigation: Review the selected integrations and configuration before enabling them; avoid broad initialization unless needed.

## Reference(s):

- [Rafter](https://rafter.so)
- [Rafter Security on ClawHub](https://clawhub.ai/rafter/skills/rafter-security)

## Skill Output:

**Output Type(s):** [Security guidance, Markdown reports, Shell commands, JSON scan results]

**Output Format:** [Markdown guidance and audit reports; optional JSON secret-scan results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Secret-scan JSON redacts matched values.]

## Skill Version(s):

0.10.6 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
