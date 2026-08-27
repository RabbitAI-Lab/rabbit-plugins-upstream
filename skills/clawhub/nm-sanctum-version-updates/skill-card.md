## Description:

Bumps versions, updates changelogs, and coordinates version changes across files for releases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release maintainers use this skill to plan and apply version bumps, changelog updates, and release-related documentation checks across project files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger words can invoke the workflow when a user only meant to ask about a version, release, or changelog generally.

Mitigation: Confirm that the user intends a release or version bump before applying file changes.

Risk: Version update guidance can affect multiple configuration and documentation files, so an incorrect target version or file set can create misleading release changes.

Mitigation: Confirm the target version, review the dry run where available, and inspect the git diff before accepting changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-version-updates)
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with shell command examples and file-change summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose multi-file version, changelog, and documentation updates for reviewer approval.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
