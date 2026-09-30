## Description:

Explores recently created repositories from major technology organizations on GitHub, selecting unreported projects with more than 1,000 stars across an expanding time window.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zengzuo613](https://clawhub.ai/user/zengzuo613)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to discover and summarize popular new repositories from major technology organizations without repeating previously featured projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads a local GitHub token and uses it for GitHub API requests without clear user-facing disclosure.

Mitigation: Review the skill before installation, and use an intentionally limited GitHub token if comfortable with this credential access.

Risk: Repository history is stored locally within the skill directory.

Mitigation: Review the stored history and account for local persistence when deploying or sharing the skill.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zengzuo613/skills/github-big-teach-latest-repo-explorer)
- [Organization list](references/organizations.json)
- [Repository answer template](references/output_template.md)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown repository overview with selection statistics and project analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the applied time window and stars > 1000 filter; marks conclusions based only on limited metadata.]

## Skill Version(s):

1.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
