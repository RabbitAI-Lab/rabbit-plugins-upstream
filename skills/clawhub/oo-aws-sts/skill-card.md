## Description:

Operate AWS STS through an OOMOL-connected account using the oo CLI and server-side credential injection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect AWS STS connector schemas and request temporary credentials through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can request temporary AWS STS credentials while describing those credential-issuing actions as safe reads.

Mitigation: Require explicit user confirmation before running assume_role or get_federated_credentials, and use only trusted roles with least-privilege, short-lived sessions.

Risk: The setup guidance includes remote installer commands.

Mitigation: Verify the installer source and integrity independently before executing installation commands.

Risk: Returned STS credentials are sensitive secrets.

Mitigation: Avoid logging, sharing, or storing returned credentials, and handle them according to secret-management policy.

## Reference(s):

- [AWS STS homepage](https://aws.amazon.com/iam/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aws-sts)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and an executionId under meta.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
