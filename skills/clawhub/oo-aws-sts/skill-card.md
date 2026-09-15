## Description:

AWS STS (aws.amazon.com). Use this skill for AWS STS requests that inspect schemas and run OOMOL connector actions instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect the live AWS STS connector schema, run supported STS actions through an OOMOL-connected account, and recover from authentication, connection, scope, billing, or CLI setup issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential-issuing actions are under-labeled as safe reads.

Mitigation: Require explicit user approval before issuing or returning AWS STS credentials, and confirm the intended payload and effect.

Risk: First-time setup includes unverified remote installer commands.

Mitigation: Use a pinned, verified oo CLI package or manually review the download before running installer commands.

Risk: Connector output may contain temporary AWS credentials.

Mitigation: Treat returned credentials as secrets and avoid logging, sharing, or persisting connector output unless explicitly required.

## Reference(s):

- [ClawHub AWS STS Skill](https://clawhub.ai/oomol/skills/oo-aws-sts)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [AWS STS Homepage](https://aws.amazon.com/iam/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include temporary AWS credentials and should be treated as secrets.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
