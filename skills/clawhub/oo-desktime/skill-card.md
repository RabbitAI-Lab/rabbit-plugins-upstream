## Description:

DeskTime enables an agent to read, create, and update DeskTime data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate DeskTime through an OOMOL-connected account, including reading company, employee, and project data and creating projects after confirming state-changing payloads with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that could be unsafe if run without verification.

Mitigation: Review the setup path before installation and prefer an official, verifiable package or a manually inspected installer.

Risk: DeskTime write actions can change workspace data.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged as write or destructive.

## Reference(s):

- [DeskTime homepage](https://desktime.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-desktime)
- [Publisher Profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include oo CLI commands, connector schema inspection steps, JSON request payloads, and confirmation prompts for write actions.]

## Skill Version(s):

1.0.3 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
