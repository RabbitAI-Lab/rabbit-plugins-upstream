## Description:

Helps developers manage GitHub issues, pull requests, reviews, and merges with structured checks and guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to turn plans into GitHub issues and pull requests, coordinate reviews and dependencies, and check readiness before merging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitHub write and merge access may change repositories or publish content unintentionally.

Mitigation: Limit token scopes and require user confirmation before issue or pull request creation and merges.

Risk: Credential and account mapping could select the wrong identity or expose excessive authority.

Mitigation: Review credential handling and verify account mapping files before use.

Risk: The Test Plan parser is not reliable as a merge gate.

Mitigation: Fix and verify the parser before relying on its merge decision.

## Reference(s):

- [github-flow on ClawHub](https://clawhub.ai/drumrobot/skills/github-flow)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with GitHub CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Issue and pull request drafts, review comments, and workflow checklists]

## Skill Version(s):

0.11.4 (source: ClawHub release and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
