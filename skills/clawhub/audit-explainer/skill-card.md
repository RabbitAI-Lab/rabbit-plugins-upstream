## Description:

Explains the output of your own openclaw security audit --json in plain English.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ismyagentsafe](https://clawhub.ai/user/ismyagentsafe)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to understand the results of a local `openclaw security audit --json`, prioritize findings, and locate OpenClaw's remediation guidance. It explains the audit output but does not change settings or fix findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit output manually submitted to the optional website may contain secrets or sensitive setup details.

Mitigation: Remove secrets and sensitive setup details before pasting any audit output into the website.

## Reference(s):

- [OpenClaw security audit checks](https://docs.openclaw.ai/gateway/security/audit-checks)
- [OpenClaw CLI security](https://docs.openclaw.ai/cli/security)
- [Project homepage](https://github.com/ismyagentsafe/audit-explainer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Concise Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prioritizes critical, warn, then info findings; summarizes up to five findings initially; redacts secrets.]

## Skill Version(s):

1.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
