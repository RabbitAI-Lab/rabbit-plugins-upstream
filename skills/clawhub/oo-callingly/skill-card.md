## Description:

Callingly support for reading, creating, updating, and deleting Callingly data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Callingly from an agent session, including listing and retrieving agents, teams, leads, and calls, and creating, updating, or deleting Callingly records after appropriate confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote script execution for installing the oo CLI.

Mitigation: Review the oo CLI installation path before use, install from a trusted official source, and prefer version pinning with signature or checksum verification.

Risk: The skill can create, update, or delete Callingly data.

Mitigation: Require explicit confirmation of the exact payload, target record, and expected effect before running write or destructive actions.

## Reference(s):

- [Callingly homepage](https://callingly.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-callingly)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building payloads and returns JSON responses from oo connector runs.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
