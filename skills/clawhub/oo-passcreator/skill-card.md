## Description:

Passcreator helps agents read, create, and update Passcreator wallet pass data through OOMOL's oo CLI and a connected Passcreator account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Passcreator templates and passes, then create wallet passes from template-specific JSON data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that first-time setup instructions include remote installer commands.

Mitigation: Install the oo CLI through a trusted, verified method and do not allow the skill to run installer scripts automatically.

Risk: The skill can create Passcreator wallet passes, which changes account state.

Mitigation: Confirm the exact create_pass payload and expected effect with the user before sending it.

## Reference(s):

- [Passcreator ClawHub Skill](https://clawhub.ai/oomol/skills/oo-passcreator)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Passcreator Homepage](https://www.passcreator.com/)
- [Passcreator Icon](https://static.oomol.com/logo/third-party/passcreator.svg)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target the oo CLI passcreator connector and may return JSON data with execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
