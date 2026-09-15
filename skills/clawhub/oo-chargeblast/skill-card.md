## Description:

Chargeblast (chargeblast.com). Use this skill for Chargeblast requests that read, create, or update account data through the OOMOL-connected connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support or operations teams use this skill to inspect Chargeblast alerts, orders, merchants, deflection logs, and paginated lists, and to create credit requests or update alerts after confirming write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance includes remote installer commands that should be reviewed before execution.

Mitigation: Prefer a verified, versioned, or package-manager installation path for the oo CLI before using the skill.

Risk: Some connector actions change Chargeblast account state.

Mitigation: Confirm the target account, payload, and expected effect with the user before running write actions.

## Reference(s):

- [Chargeblast homepage](https://www.chargeblast.com)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Chargeblast ClawHub release](https://clawhub.ai/oomol/skills/oo-chargeblast)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce connector command guidance and summarize JSON responses from Chargeblast actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
