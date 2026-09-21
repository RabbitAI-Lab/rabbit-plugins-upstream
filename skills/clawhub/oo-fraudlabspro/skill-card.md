## Description:

Use this skill for FraudLabs Pro requests that read, create, or update data through the OOMOL oo CLI rather than calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to screen FraudLabs Pro order transactions for fraud risk, retrieve screening results, and send approve or reject feedback through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute a remote installer script for the oo CLI.

Mitigation: Install the oo CLI only from verified vendor documentation or inspected downloads before using the skill.

Risk: FraudLabs Pro actions may transmit order data or change transaction records.

Mitigation: Require explicit user confirmation before screening orders or sending approve or reject feedback.

## Reference(s):

- [FraudLabs Pro homepage](https://www.fraudlabspro.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fraudlabspro)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing FraudLabs Pro action payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
