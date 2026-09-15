## Description:

Operate Govee devices through an OOMOL-connected account by listing devices, reading states and scenes, and controlling documented capabilities with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect and manage Govee devices connected through OOMOL, including device inventory, current state, scenes, and supported capability controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change the state of connected Govee devices through control_capability.

Mitigation: Require explicit user confirmation before any control_capability call, including the exact device, capability, value, and expected physical effect.

Risk: The provided first-time setup includes remote installer commands for the OOMOL CLI.

Mitigation: Avoid running remote installer commands as written unless the installation source has been independently trusted and verified.

Risk: Security evidence reports under-disclosed device-control authority and flags the release as suspicious.

Mitigation: Review the skill before installation and use it only when the user is comfortable with an agent operating their connected Govee account through OOMOL.

## Reference(s):

- [ClawHub Govee Skill](https://clawhub.ai/oomol/skills/oo-govee)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Govee Homepage](https://www.govee.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May operate connected Govee devices through OOMOL; device-control actions should include explicit user confirmation of the device, capability, value, and physical effect.]

## Skill Version(s):

1.0.2 (source: frontmatter, evidence release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
