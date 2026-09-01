## Description:

Helps users migrate a local AI assistant between computers by packaging assistant memory and configuration into a zip archive, then guiding a user-confirmed restore on the new machine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hechunxian](https://clawhub.ai/user/hechunxian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, or end users use this skill when moving a local assistant setup to a new computer. It guides local packing, path confirmation, restore, and post-restore checks for assistant memory and configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive assistant memory and configuration that may include secrets, private notes, tokens, or account details.

Mitigation: Review the archive contents and keep the zip private; prefer encrypted storage or transfer when moving it between machines.

Risk: The migration depends on external pack.py and deploy.py scripts that are not included in the release artifact for review.

Mitigation: Run the skill only when the local scripts are trusted, and review those scripts before using them with real assistant memory.

Risk: A restore can overwrite existing assistant files on the destination machine.

Mitigation: Confirm the destination path before deployment, use MIGRATE_DEST for isolated test restores, and keep destination backups before applying changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hechunxian/skills/migration-pack-deploy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and file path checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs local archive creation and restore steps; state-changing operations require user-confirmed paths.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
