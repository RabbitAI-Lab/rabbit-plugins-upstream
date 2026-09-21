## Description:

LIFX (lifx.com). Use this skill for LIFX requests that read, create, or update data through the OOMOL-connected LIFX connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents supporting users with connected LIFX accounts use this skill to list lights and scenes, validate colors, activate scenes, and control light state through the oo CLI. It is intended for LIFX account operations where write actions are confirmed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may run remote installer scripts directly in the shell.

Mitigation: Review OOMOL's installer source or use a safer documented package or release path before running setup.

Risk: LIFX write actions can change the state of connected lights.

Mitigation: Confirm the exact target, payload, and user-visible effect before running write actions.

## Reference(s):

- [ClawHub LIFX skill page](https://clawhub.ai/oomol/skills/oo-lifx)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [LIFX homepage](https://www.lifx.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce read or write oo CLI actions; write actions should include the intended payload and effect for confirmation before execution.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
