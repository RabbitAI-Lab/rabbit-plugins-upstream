## Description:

AppDrag lets an agent read, create, and update AppDrag data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect AppDrag connector schemas and run AppDrag Cloud Backend API functions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change AppDrag state when the agent runs connector actions.

Mitigation: Confirm the exact payload and expected effect with the user before executing write actions.

Risk: The optional oo CLI installation path includes remote installer scripts.

Mitigation: Prefer a verified package-manager or installer path, or review the installer before running it.

## Reference(s):

- [AppDrag homepage](https://appdrag.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [AppDrag skill on ClawHub](https://clawhub.ai/oomol/skills/oo-appdrag)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
