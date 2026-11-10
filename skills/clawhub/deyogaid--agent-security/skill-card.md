## Description:

Security hardening for AI agents. Audit your workspace for leaked secrets, check file permissions, validate API key storage, scan for prompt injection risks, and monitor for unauthorized access patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deyogaid](https://clawhub.ai/user/deyogaid)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use the shell checks to find credential-like strings, review credential file permissions and age, identify sensitive files tracked by Git, and inspect network reachability. They can adapt the checklist for recurring agent workspace reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The network check contacts an external host whose role is unexplained, which could expose when the check is run.

Mitigation: Remove the external host or independently verify its purpose before running the network check.

Risk: The secret scan can print matching lines that may contain credential values in chat or logs.

Mitigation: Change the check to report file and line locations without values, and redact any findings before sharing.

## Reference(s):

- [ClawHub agent-security release](https://clawhub.ai/deyogaid/skills/agent-security)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
