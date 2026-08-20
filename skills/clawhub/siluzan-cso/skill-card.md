## Description:

Siluzan CSO helps agents operate the Siluzan content operations platform for content workflows, persona management, RAG-backed brand knowledge, social-media publishing, account operations, planning, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to guide agents through Siluzan CSO workflows for content drafting, persona management, RAG-backed brand answers, media account publishing, task handling, planning, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer scripts and CLI setup may make broad, persistent local changes.

Mitigation: Review the installer scripts first, prefer installing Node and the CLI manually, avoid persistent npm registry changes, and register the skill only in the intended assistant.

Risk: The skill can guide upload, publish, delete, account-group, planning, and persona-save actions.

Mitigation: Confirm each write action with the user before it runs and verify the result afterward with the relevant read-only command.

Risk: Generated content may include incorrect or unsupported claims, and the security guidance flags adversarial persuasion framing in some workflow rules.

Mitigation: Review generated content carefully, ground brand or product claims in RAG evidence, and run the skill's content validation workflow where applicable.

## Reference(s):

- [Siluzan CSO ClawHub release page](https://clawhub.ai/sigedev01-bit/skills/siluzan-cso)
- [Setup](references/setup.md)
- [Publishing workflow](references/publish.md)
- [RAG workflow](references/rag.md)
- [Content writer workflow](three-lib-content-workflow/content-writer.workflow.md)
- [Planning workflow](references/planning.md)
- [Persona workflow](references/persona.md)
- [Reporting workflow](references/report.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local files such as cover images, validation reports, and publish configuration when the agent follows the skill workflows.]

## Skill Version(s):

1.1.41 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
