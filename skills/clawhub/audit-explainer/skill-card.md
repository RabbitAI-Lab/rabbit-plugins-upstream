## Description:

Explains OpenClaw security audit findings in plain English, prioritizes them by severity, and points to OpenClaw's remediation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ismyagentsafe](https://clawhub.ai/user/ismyagentsafe)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use the skill to understand their own security audit results, identify which findings to address first, and find OpenClaw's suggested fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit output can contain sensitive details about a user's setup, and sharing it externally may expose that information.

Mitigation: Do not save or upload audit output through the skill. Before manually sharing it with any optional external service, review it and remove secrets or other sensitive details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ismyagentsafe/skills/audit-explainer)
- [Skill homepage and support repository](https://github.com/ismyagentsafe/audit-explainer)
- [OpenClaw security audit checks](https://docs.openclaw.ai/gateway/security/audit-checks)
- [OpenClaw security audit documentation](https://docs.openclaw.ai/cli/security)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Plain-English Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prioritizes findings by severity and summarizes up to five findings in an initial response.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
