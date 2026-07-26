## Description: <br>
Updates installed agent skills safely with version checks, diff previews, backups, explicit approval, data migration, and rollback support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to update installed skills with previewed behavior changes, backups, local-edit handling, migrations, and rollback paths before changes are applied. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent through changes to installed skill behavior, backups, logs, and configuration. <br>
Mitigation: Require diff preview, explicit approval, backup creation, and a verification run before reporting an update as successful. <br>
Risk: Batch updates, migrations, or local edit collisions can affect multiple agent installs or user data conventions. <br>
Mitigation: Inventory all install locations, single out risky updates, preserve hand edits through merge review, and restore from the same backup timestamp if migration fails. <br>


## Reference(s): <br>
- [Skill Update on ClawHub](https://clawhub.ai/ivangdavila/skills/skill-update) <br>
- [Skill Update on Clawic](https://clawic.com/skills/skill-update) <br>
- [Preview Changes](preview.md) <br>
- [Rollback](rollback.md) <br>
- [Handling Migrations](migrate.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe backup paths, update logs, diff summaries, migration plans, and rollback steps.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
