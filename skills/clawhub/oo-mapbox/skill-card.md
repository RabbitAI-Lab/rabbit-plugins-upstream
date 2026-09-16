## Description:

Mapbox (mapbox.com) skill for reading, creating, and updating Mapbox data through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Mapbox connector schemas, run geocoding, directions, and matrix actions, and handle Mapbox setup issues through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute changing code on the user's machine.

Mitigation: Prefer a safer oo CLI installation path when available, verify the installer source and integrity before running it, and avoid repeating setup commands unless an auth or connection failure requires them.

Risk: Mapbox requests are routed through OOMOL using the connected account, and write actions can change Mapbox state.

Mitigation: Confirm write action payloads and expected effects with the user before execution, and fetch the live connector schema before constructing each request.

## Reference(s):

- [ClawHub Mapbox Skill](https://clawhub.ai/oomol/skills/oo-mapbox)
- [Mapbox Homepage](https://www.mapbox.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and requires confirmation before write or destructive actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
