## Description:

Provides agent guidance for managing Freshstatus services and service groups through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read, create, update, and delete Freshstatus services and service groups through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change Freshstatus service or group state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: Destructive actions can delete Freshstatus services or groups.

Mitigation: Confirm the target resource and obtain explicit user approval before running destructive actions.

Risk: Freshstatus access depends on trusting OOMOL to broker credentials through the connected account.

Mitigation: Only complete oo CLI login or Freshstatus connection steps when the user intends to manage Freshstatus through OOMOL.

## Reference(s):

- [Freshstatus homepage](https://www.freshworks.com/statuspage)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Freshstatus skill page](https://clawhub.ai/oomol/skills/oo-freshstatus)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
