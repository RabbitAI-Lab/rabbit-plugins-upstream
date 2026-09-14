## Description:

Helps an agent operate SF Express through an OOMOL-connected sf_express account for reading, creating, updating, and deleting shipment and business data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to inspect SF Express connector schemas and run SF Express actions through an OOMOL-connected account. It supports shipment ordering, tracking, freight, station, print, notification, and account-related workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change live shipment and business data through broad command access and incomplete confirmation boundaries.

Mitigation: Require explicit user approval for actions that create, cancel, update, append, report, upload, register, send, charge, or delete data, and confirm the exact payload and expected effect before execution.

Risk: Installing the oo CLI by piping a remote installer directly to a shell can expose the user to installer supply-chain risk.

Mitigation: Review the oo CLI installer before running it and use trusted installation paths where available.

Risk: Connected SF Express credentials may authorize broad account operations.

Mitigation: Use the least-privileged SF Express account available and avoid initiating sign-in or connection flows unless a command fails with an authentication or connection error.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-sf-express)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [SF Express Open Platform](https://open.sf-express.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an OOMOL sign-in, an SF Express connection, and live schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
