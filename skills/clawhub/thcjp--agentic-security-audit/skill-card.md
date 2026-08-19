## Description:

Audits codebases, infrastructure descriptions, and agentic AI systems for security risks and produces security findings and remediation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security reviewers, and automation teams use this skill to review a specified repository, infrastructure description, or agent system for security issues, compliance concerns, and prioritized improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read files, run commands, and write outputs while performing security audits.

Mitigation: Provide a narrow target path and audit scope, and review proposed command execution or file writes before granting broad access.

Risk: Security findings may be incomplete or may prioritize issues incorrectly.

Mitigation: Treat generated audit results as review material and validate high-impact findings before deployment or remediation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agentic-security-audit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured JSON-style audit summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include grades, scores, findings, remediation suggestions, and reviewable command or file-write proposals.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
