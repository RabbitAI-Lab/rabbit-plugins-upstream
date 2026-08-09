## Description:

Moves the WorkBuddy data directory from the Windows system drive to a fixed non-system drive using a directory junction so WorkBuddy data, runtimes, logs, sessions, skills, and caches stop consuming C: space.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guibe7391](https://clawhub.ai/user/guibe7391)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support engineers, and WorkBuddy users use this skill when WorkBuddy data or runtime files are filling the Windows system drive. It guides a migration to a non-system disk while preserving the original C: path through a directory junction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The migration permanently redirects all WorkBuddy data and can delete or overwrite the target WorkBuddy data folder when run in the wrong state.

Mitigation: Back up the current WorkBuddy data folder, verify the selected target path contains nothing needed, and confirm the source and target state before running or rerunning the migration.

Risk: Broad deletion behavior in cleanup and stale-target handling could erase data if paths are mistaken or reused after reinstall.

Mitigation: Use only verified exact WorkBuddy paths, avoid ad hoc rm -rf or repeated rmdir cleanup notes, and review the generated migration plan before approving deletion.

Risk: Interrupted migration or Windows environment quirks can leave WorkBuddy in a partially migrated state.

Mitigation: Close WorkBuddy first, keep a backup, review the target-drive migration log, and verify the junction, database, and copied data before removing old source data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guibe7391/skills/workbuddy-data-migration)
- [Lessons learned root-cause log](references/lessons.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with bundled Windows batch and Node.js scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Windows-only migration workflow that creates a directory junction and writes a migration log on the selected target drive.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
