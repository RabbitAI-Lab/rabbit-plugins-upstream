## Description:

Amara enables agents to read, create, update, and delete Amara data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Amara videos, subtitle languages, subtitle data, notes, users, teams, activity, and workflow actions from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that could execute unverified code in a shell.

Mitigation: Review the setup path before installation, prefer a trusted versioned source with integrity verification, and do not let an agent run remote installer scripts automatically.

Risk: Write and destructive Amara actions can change or remove account data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any write or destructive action.

## Reference(s):

- [Amara Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-amara)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Amara homepage](https://amara.org)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON data and execution metadata from the connector.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
