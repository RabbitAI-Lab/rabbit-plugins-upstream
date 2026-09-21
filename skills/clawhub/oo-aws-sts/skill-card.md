## Description:

AWS STS helps agents operate AWS Security Token Service through an OOMOL-connected account using the oo CLI and live connector schemas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect AWS STS connector schemas and request temporary AWS credentials through AssumeRole or OOMOL OIDC federation when an OOMOL AWS STS connection is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can return temporary AWS credentials to an agent through AWS STS actions.

Mitigation: Use it only where temporary credential exposure to the agent is acceptable, keep connected AWS permissions narrowly scoped, and confirm write-tagged payloads with the user before execution.

Risk: First-time setup examples include remote installer commands that execute downloaded scripts.

Mitigation: Prefer a verified package or reviewed installer path for the oo CLI before running AWS STS actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aws-sts)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [AWS STS homepage](https://aws.amazon.com/iam/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions executed with --json return a JSON object containing data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
