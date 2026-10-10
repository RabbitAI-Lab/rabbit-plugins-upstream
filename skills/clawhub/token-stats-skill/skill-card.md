## Description:

Records and analyzes token usage from eight local coding agents and optionally synced Trae CN accounts, with source diagnostics, daily and date-range reports, and user-approved offline scheduling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[baijian](https://clawhub.ai/user/baijian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users inspect private token-usage history, diagnose source coverage, and compare daily or date-range usage. Optional Trae CN account synchronization and periodic local recording require separate approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The pinned CLI is an opaque binary that can read sensitive local agent usage stores.

Mitigation: Install only if the publisher is trusted, verify the pinned executable before use, and restrict collection to requested sources and dates.

Risk: Reports and snapshots may expose private paths and activity patterns.

Mitigation: Keep data in dedicated private directories; avoid sharing full reports or logs and enable per-run snapshots only when needed.

Risk: Trae CN synchronization accesses existing account credentials and contacts a remote service.

Mitigation: Obtain separate consent for account selection and synchronization; do not put credential checks or network sync in offline scheduled jobs.

Risk: Installing a periodic recorder persists a task, and retention can delete snapshots.

Mitigation: Preview the schedule, paths, and retention settings and obtain explicit authorization before installing, replacing, or enabling deletion.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/baijian/skills/token-stats-skill)
- [Token Recording](references/token-recording.md)
- [Trae CN](references/trae-cn.md)
- [Recorder Security](references/recorder-security.md)
- [token-stats v0.0.4 binary release](https://github.com/baijian/token-stats/releases/tag/v0.0.4)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with token-usage summaries and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated daily reports and snapshots may contain sensitive paths, model names, and usage history; missing or stale coverage is not zero usage.]

## Skill Version(s):

0.0.4 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
