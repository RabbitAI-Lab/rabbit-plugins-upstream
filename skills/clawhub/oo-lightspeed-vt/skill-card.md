## Description:

LightSpeed VT lets an agent search and read LightSpeed VT courses, locations, and users through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve LightSpeed VT course, location, and user records from a connected OOMOL account without handling raw credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LightSpeed VT user-listing results may contain sensitive account data.

Mitigation: Review retrieved user data before sharing it and restrict use to authorized LightSpeed VT and OOMOL accounts.

Risk: CLI installation or login steps can affect the local environment and account access.

Mitigation: Review oo CLI install and login commands before allowing them, and use setup steps only when an auth or connection error requires them.

Risk: Broad invocation wording may cause the skill to be used for LightSpeed VT tasks beyond its read-only connector actions.

Mitigation: Use the documented actions for course, location, and user retrieval, and confirm exact payloads before any future write or destructive action is added.

## Reference(s):

- [LightSpeed VT homepage](https://lightspeedvt.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and a meta.executionId value.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
