## Description:

Subvisory enables agents to read, create, update, and delete Subvisory data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to manage Subvisory categories, payment methods, and subscriptions from an OOMOL-connected account. It supports reads, writes, updates, deletes, live schema inspection, and guided recovery for authentication, connection, CLI, and billing errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute downloaded shell or PowerShell code.

Mitigation: Review the setup path before installing and run installer commands only after independently trusting the OOMOL installer source.

Risk: Write and destructive actions can change or remove Subvisory data.

Mitigation: Confirm the exact payload and expected effect with the user before writes, and require explicit approval before destructive actions.

## Reference(s):

- [Subvisory Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-subvisory)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Subvisory Homepage](https://www.subvisory.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are expected to inspect live action schemas before submitting requests; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
