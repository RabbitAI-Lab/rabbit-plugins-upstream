## Description:

Tanium lets an agent inspect schemas and run GraphQL documents against a connected Tanium Gateway endpoint through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Security operations and endpoint management practitioners use this skill to query Tanium through an OOMOL-connected account, with schema inspection before running connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use broad GraphQL access against a connected Tanium account.

Mitigation: Review GraphQL mutations, administrative operations, target scope, and expected effects with the user before execution.

Risk: The skill includes remote installer commands that pipe downloaded scripts to a shell.

Mitigation: Avoid running pipe-to-shell installers unless the installer has been independently verified through a trusted channel.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-tanium)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Tanium Homepage](https://www.tanium.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and execution metadata when actions are run.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
