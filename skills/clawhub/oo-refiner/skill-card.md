## Description:

Refiner (refiner.io). Use this skill for ANY Refiner request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Refiner contacts, forms, segments, responses, reporting, and product events through an OOMOL-connected Refiner account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update contacts, track events, tag responses, and modify segment membership in Refiner.

Mitigation: Confirm the exact payload and expected effect with the user before write actions, and require explicit approval before destructive actions.

Risk: The optional oo CLI installer uses pipe-to-shell commands.

Mitigation: Review or verify the installer before running it, or use the platform install guide instead of executing the command blindly.

Risk: Refiner access is mediated through OOMOL-connected credentials.

Mitigation: Install and use the skill only when the user accepts OOMOL as the intermediary for the connected Refiner account.

## Reference(s):

- [Refiner homepage](https://refiner.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; command responses are JSON from the oo CLI.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
