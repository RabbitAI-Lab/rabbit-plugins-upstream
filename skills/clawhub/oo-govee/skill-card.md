## Description:

The Govee skill lets an agent operate Govee devices through the OOMOL oo CLI, including listing devices and scenes, reading device state, and controlling documented capabilities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to manage Govee devices through an OOMOL-connected account. It supports device and scene discovery, device state checks, and confirmed changes to documented device capabilities such as power, brightness, color, mode, and temperature.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change Govee device state through control_capability even though parts of the description emphasize search and read use.

Mitigation: Require explicit user confirmation of the exact payload and expected effect before any control_capability call.

Risk: The setup guidance includes remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Prefer a verified package, pinned release, checksum, or vendor-documented safer installation path before installing the oo CLI.

## Reference(s):

- [ClawHub Govee skill page](https://clawhub.ai/oomol/skills/oo-govee)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Govee homepage](https://www.govee.com)
- [OOMOL Govee connection setup](https://console.oomol.com/app-connections?provider=govee)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
