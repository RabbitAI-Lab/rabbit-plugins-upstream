## Description:

Interact with GitHub via the gh CLI: issues, pull requests, CI runs, repository health, changelog generation, and issue triage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and repository maintainers use this skill to inspect GitHub issues, pull requests, CI runs, repository health, and recent changes through the GitHub CLI. It helps an agent propose read-only GitHub reporting commands and summarize repository maintenance signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run GitHub CLI read commands against repositories the user names and can use the user's existing gh login.

Mitigation: Review repository targets and GitHub authentication scope before execution, and run commands only against repositories intended for analysis.

Risk: Some bundled helper output is localized in Danish, which may make reports harder for some users to interpret.

Mitigation: Review generated reports and translate or localize output before relying on it for operational decisions.

## Reference(s):

- [ClawGit Pro on ClawHub](https://clawhub.ai/northcap-group/skills/clawgit-pro)
- [Northcap Group ClawHub publisher profile](https://clawhub.ai/user/northcap-group)
- [GitHub](https://github.com)
- [GitHub API endpoint used by the skill](https://api.github.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and plain text with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the GitHub CLI and GitHub network access; no API keys or paid calls are disclosed in the evidence.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
