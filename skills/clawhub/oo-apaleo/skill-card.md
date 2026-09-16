## Description:

apaleo (apaleo.com). Use this skill for ANY apaleo request: reading, creating, updating, and deleting data through the OOMOL apaleo connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage apaleo properties, units, unit groups, and unit attributes from an agent through the OOMOL-connected `oo` CLI. It supports read workflows plus controlled write and destructive workflows that require schema inspection and user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes internet-downloaded installer scripts.

Mitigation: Review the setup path before installation and prefer verified oo CLI installation instructions or package sources with integrity checks.

Risk: Write actions can change apaleo property, unit, unit group, and unit attribute state.

Mitigation: Inspect the live action schema, confirm the exact payload and expected effect with the user, and run only after approval.

Risk: Destructive actions can delete or reset apaleo data.

Mitigation: Confirm the exact target and payload, obtain explicit approval, and restrict execution to intended test or production resources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-apaleo)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [apaleo homepage](https://apaleo.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the `oo` CLI and may return connector JSON containing `data` and `meta.executionId`.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
