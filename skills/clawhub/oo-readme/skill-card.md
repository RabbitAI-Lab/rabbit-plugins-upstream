## Description:

ReadMe (readme.com). Use this skill for ANY ReadMe request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation teams use this skill to manage ReadMe projects through an OOMOL-connected account, including docs, categories, changelogs, custom pages, project versions, API specifications, search, metadata, and Owlbot questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Use a verified installer or official package source before running setup commands.

Risk: The skill can create, update, or delete ReadMe content and project configuration.

Mitigation: Confirm the exact payload, target, and effect with the user before write or destructive actions.

Risk: The skill depends on OOMOL-connected ReadMe account access.

Mitigation: Install only when the connector model and associated ReadMe account permissions are acceptable.

## Reference(s):

- [ClawHub ReadMe Skill Page](https://clawhub.ai/oomol/skills/oo-readme)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ReadMe Homepage](https://readme.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue oo CLI connector commands that return JSON responses from ReadMe actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
