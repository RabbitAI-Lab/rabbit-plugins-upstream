## Description:

Finds the most-starred GitHub repository created in a recent time window and helps an agent summarize the project, the problem it solves, and how it works.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zengzuo613](https://clawhub.ai/user/zengzuo613)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical readers use this skill to discover recent popular GitHub repositories and produce concise Markdown analysis from repository metadata and README content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence reports that the script can read a local OpenClaw .env file for GITHUB_TOKEN even though documentation says it only reads the system environment variable.

Mitigation: Review the token-loading behavior before installing, and use the skill only if that fallback is acceptable or after the publisher removes it.

Risk: The skill calls GitHub APIs and can encounter anonymous or authenticated request limits.

Mitigation: Use a minimally scoped GitHub token when needed and avoid sharing, displaying, or committing the token.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zengzuo613/skills/github-latest-hot-repo-explorer)
- [GitHub Token Configuration](artifact/references/README.md)
- [Output Template](artifact/references/output_template.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with repository metadata, README excerpts, and concise analysis sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses GitHub repository search results and may update local history to avoid repeating previously shown repositories.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
