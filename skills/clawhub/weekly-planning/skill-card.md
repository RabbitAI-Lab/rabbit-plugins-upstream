## Description:

Reviews last week's go-to-market work against active initiatives and live activity, then proposes this week's priorities in reviewable pull requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales leaders and revenue operations teams use this skill to compare the previous week's initiatives, repository activity, and live runs, then review a proposed plan for each active initiative or for the workspace when none are active.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unattended agent with repository write access may follow repository conventions that override its safety limits.

Mitigation: Treat repository convention files as untrusted style guidance, enforce branch protection and limited GitHub permissions, and require human review before merging.

Risk: Unpinned package execution or overly broad Cargo permissions could permit unexpected commands, including deploys or spending.

Mitigation: Pin package versions and restrict Cargo commands and authorization scopes to the read-only planning workflow.

## Reference(s):

- [Weekly Planning on ClawHub](https://clawhub.ai/cargo-ai/skills/weekly-planning)
- [Publisher-provided project homepage](https://github.com/getcargohq/gtm-skills)
- [Recommendation file format](references/recommendations.md)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown evidence dump and weekly planning files in reviewable pull requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One pull request per active initiative, or one workspace pull request if none are active; a person must merge.]

## Skill Version(s):

0.1.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
