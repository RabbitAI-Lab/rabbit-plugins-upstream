## Description:

Omnisend helps agents read, create, update, and delete Omnisend contacts, tags, and segments through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Omnisend contacts, tags, and segments from an agent workflow while relying on an existing OOMOL account connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes a remote installer that could execute code before users inspect it.

Mitigation: Review and verify the installer before use; prefer a pinned, verified installer or package-manager installation and avoid elevated shells.

Risk: Write and destructive Omnisend actions can change contact tags or contact records.

Mitigation: Inspect the live action schema and confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [Omnisend Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-omnisend)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Omnisend Homepage](https://www.omnisend.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions can return JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
