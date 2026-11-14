## Description:

Fetch GitHub issues, select candidates, spawn background fix agents, open PRs, and optionally process PR review comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to triage GitHub issues, select candidate fixes, launch background coding agents, and open pull requests with evidence. It can also monitor workflow-created PRs for actionable review comments and route follow-up work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can autonomously modify repositories, push branches, open pull requests, and process untrusted GitHub issue or review content.

Mitigation: Use dry-run first, avoid unattended --yes, --cron, and --watch modes on repositories with untrusted authors, and require manual review before pushes or PR updates.

Risk: Write-capable GitHub credentials can expand the impact of unintended actions.

Mitigation: Use a minimally scoped GitHub token and install only when repository write automation is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/gh-issues)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May spawn background agents that modify repositories, push branches, open pull requests, and process review comments when authorized.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
