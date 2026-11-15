## Description:

Track upcoming deadlines from a DEADLINES.md table and cross-check each one against its git repo (uncommitted changes, unpushed commits, or days since the last GitHub push) to flag work that is at risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aditya-datar](https://clawhub.ai/user/aditya-datar)

### License/Terms of Use:

MIT-0

## Use Case:

Students, project teams, and individual developers use the skill to review deadlines in DEADLINES.md and flag near-term work that may be at risk based on local repository state or GitHub push activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan inspected only 4 of 5 components, and static analysis of one file was incomplete.

Mitigation: Review the uninspected component and the skill files before installing.

Risk: The skill checks public repositories through the GitHub API, and the scan noted that tool scope was unclear.

Mitigation: Review scripts/radar.mjs and confirm its local and GitHub repository checks fit the workspaces you plan to use.

Risk: Commit age may not match the push activity that matters to a project's deadline workflow.

Mitigation: Verify reported push times against the repository's actual submission or progress tracking process.

## Reference(s):

- [Deadline Radar on ClawHub](https://clawhub.ai/aditya-datar/skills/deadline-radar)
- [GitHub commits API endpoint used for public repositories](https://api.github.com/repos/{owner}/{repo}/commits?per_page=1)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text deadline report or JSON containing matching deadlines and repository status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports a configurable look-ahead window and timezone; alert mode prints NO_REPLY when no deadlines are at risk.]

## Skill Version(s):

1.0.0 (source: release metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
