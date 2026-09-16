## Description:

Use this skill for OptimoRoute requests at optimoroute.com, including reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate OptimoRoute through an OOMOL-connected account, including reading orders, creating or updating orders, and deleting orders when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote installer scripts without verification.

Mitigation: Review setup steps before installing and prefer a trusted, verifiable installation method for the oo CLI.

Risk: Write and delete actions can change or remove OptimoRoute order data.

Mitigation: Confirm the exact payload, target account impact, and explicit user approval before running write or destructive actions.

## Reference(s):

- [OptimoRoute homepage](https://optimoroute.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Relies on live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: skill metadata and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
