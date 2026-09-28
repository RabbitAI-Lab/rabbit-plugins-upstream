## Description:

Helps agents preserve project progress across sessions by reading and updating project-root workflow files and producing a handoff summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project teams use this skill to keep shared progress, tasks, decisions, and daily logs in a project-root .workflow directory so an agent can resume work across sessions or hand off to another agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project handoff files may expose secrets or unnecessary sensitive project details.

Mitigation: Keep credentials, secrets, and unnecessary sensitive details out of .workflow files.

Risk: Installation to an unintended agent or user-wide skill directory may broaden where the workflow runs.

Mitigation: Use a pinned install command with an explicit --agent or --dir target; avoid -g unless installation for all supported agents is intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-workflow)
- [Project homepage (listed in skill metadata)](https://github.com/YottaMeta/yotta-workflow)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown project-status files and a text handoff anchor]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keeps progress, tasks, decisions, roadmap, and daily logs under the project's .workflow directory.]

## Skill Version(s):

0.4.2 (source: ClawHub release metadata, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
