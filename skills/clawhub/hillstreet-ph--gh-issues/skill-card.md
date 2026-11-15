## Description:

Fetch GitHub issues, select candidates, spawn background fix agents, open PRs, and optionally process PR review comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to find GitHub issues, delegate selected fixes to background workers, open pull requests, and optionally process review comments on workflow-created pull requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: With --yes or --cron, issue and review work can run without confirmation and may spawn workers that create pull requests.

Mitigation: Use --dry-run to inspect candidates, and enable --yes or --cron only when unattended work is intended.

## Reference(s):

- [gh-issues on ClawHub](https://clawhub.ai/hillstreet-ph/skills/gh-issues)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Text]

**Output Format:** [Code changes, GitHub pull requests, and text status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May launch up to eight background workers; watch and cron modes support ongoing or unattended operation.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
