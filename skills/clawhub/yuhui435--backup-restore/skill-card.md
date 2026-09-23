## Description:

Provides a Python script and usage guidance for creating, listing, verifying, and managing local OpenClaw backup ZIP files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuhui435](https://clawhub.ai/user/yuhui435)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to back up local OpenClaw configuration and workspace data, inspect available backup archives, and verify ZIP integrity before relying on a backup workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restore behavior may report success without restoring data.

Mitigation: Do not rely on this skill for disaster recovery or migration until restore behavior is implemented and tested with non-critical backups.

Risk: Backup coverage and source-path selection may be incomplete or environment-specific.

Mitigation: Confirm the configured OpenClaw paths and expected files before use, and test backup completeness before depending on the archives.

Risk: Backup ZIP files may contain sensitive configuration and workspace data.

Mitigation: Store generated ZIP files in protected storage and apply encryption or access controls outside the skill.

Risk: Command-line parsing may not match the documented restore and verify examples.

Mitigation: Validate command syntax in a disposable environment before using the skill on important backups.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled script may create local ZIP backup files when executed.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
