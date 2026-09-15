## Description:

Operate SafetyCulture through an OOMOL-connected account to inspect action schemas, read inspections and actions, search inspections, and create SafetyCulture actions with explicit confirmation for writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to interact with SafetyCulture through the OOMOL `oo` CLI, including retrieving inspections, listing or searching actions, and preparing write requests with user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that can execute code on the user's machine.

Mitigation: Prefer an official reviewed install path, verify the installer where possible, and do not run installer commands blindly.

Risk: The `create_action` operation changes SafetyCulture data.

Mitigation: Confirm the exact payload and expected effect with the user before allowing write operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-safetyculture)
- [SafetyCulture Homepage](https://safetyculture.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing SafetyCulture action payloads.]

## Skill Version(s):

1.0.2 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
