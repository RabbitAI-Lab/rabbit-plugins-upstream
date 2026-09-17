## Description:

FraudLabs Pro helps agents screen order transactions for fraud risk, retrieve screening results, and submit approve or reject feedback through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate FraudLabs Pro from an agent workflow, including screening orders, checking transaction results, and submitting approve or reject feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running a remote installer directly in a shell.

Mitigation: Review the oo CLI installation path before installing and prefer a version-pinned package or verified installer.

Risk: FraudLabs Pro actions can create or modify screening and feedback records.

Mitigation: Require explicit confirmation of the payload and intended effect before executing screening or feedback actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-fraudlabspro)
- [FraudLabs Pro Homepage](https://www.fraudlabspro.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON when actions are executed with the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
