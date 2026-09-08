## Description:

Trace removed or relocated config files across source, releases, migration code, and local state without mistaking relocation for deletion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when configuration, workspace, or instruction files disappear after an upgrade and they need to determine whether content was deleted, relocated, merged, or left unsupported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to inspect private repositories, local backups, or configuration files while troubleshooting migrations.

Mitigation: Review proposed commands before execution and avoid exposing sensitive repository content, backups, or local configuration data in shared outputs.

Risk: A missing legacy file can be mistaken for data loss when content was relocated, merged, or intentionally retained elsewhere.

Mitigation: Verify destination content, backups, hashes, timestamps, and active instruction references before concluding that data was deleted.

Risk: Release notes or large API responses may omit migration ordering, rollback behavior, or edge cases.

Mitigation: Use release metadata, changed-file lists, migration source, docs, and templates together, and label unchecked invariants as unknown.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/trace-configuration-file-migrations)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or concise text reports with file paths, timelines, commands, and verification status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Unknown invariants should be labeled unknown rather than treated as successful migration evidence.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
