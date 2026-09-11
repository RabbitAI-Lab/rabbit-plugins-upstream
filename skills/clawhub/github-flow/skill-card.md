## Description:

GitHub Flow helps agents turn plans, code changes, reviews, and merge decisions into GitHub issues and pull requests using documented GitHub CLI workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill when working in GitHub repositories to create and update issues and pull requests, manage dependency and review workflows, prepare merges, sanitize public-facing content, and coordinate GitHub account authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide GitHub CLI workflows that require repository write access.

Mitigation: Install only for repositories where that authority is acceptable, and review proposed issue, pull request, review, merge, and publish actions before execution.

Risk: Broad or persistent GitHub authorization can affect more repositories or operations than intended.

Mitigation: Review requested GitHub scopes and prefer command-scoped tokens over global gh auth switching.

Risk: Alternate-account approval or review workflows can publish actions under an unintended GitHub identity.

Mitigation: Disable or remove alternate-account approval workflows unless they are required and the acting account mapping is verified.

Risk: Public issue, pull request, or review content can expose unwanted branding or sensitive information.

Mitigation: Remove unwanted PR branding and apply the skill's public-content sanitization guidance before publishing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/github-flow)
- [Skill Overview](artifact/SKILL.md)
- [Changelog](artifact/CHANGELOG.md)
- [Authentication and Scope Guide](artifact/auth-scope.md)
- [Pull Request Guide](artifact/pr.md)
- [Merge Guide](artifact/merge.md)
- [Public Content Sanitization Guide](artifact/sanitize.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, GitHub CLI commands, issue and pull request body structures, and helper script behavior.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for agent-mediated GitHub workflows and should be reviewed before actions that publish content or mutate repositories.]

## Skill Version(s):

0.10.2 (source: server release metadata and CHANGELOG, released 2026-09-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
