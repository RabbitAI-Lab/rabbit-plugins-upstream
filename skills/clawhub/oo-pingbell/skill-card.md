## Description:

PingBell helps agents operate PingBell through an OOMOL-connected account by inspecting connector schemas, listing available sources, and ringing selected sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate PingBell from an agent: list connected account sources, inspect live connector schemas, and ring a selected source after confirming the state-changing effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Review installation before use, prefer safer official installation methods where possible, and do not allow an agent to run the installer automatically.

Risk: The ring_source action changes visible PingBell account state by updating counters, screens, and subscribed devices.

Mitigation: Require explicit user confirmation of the selected source and expected effect before running ring_source.

## Reference(s):

- [PingBell homepage](https://pingbell.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pingbell)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before payload construction; state-changing ring_source calls require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
