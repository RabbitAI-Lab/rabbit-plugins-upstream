## Description:

Guides GitHub issue, pull request, review, and merge workflows with checks for authentication, verification, and public content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to plan and publish GitHub issues and pull requests, manage reviews and dependencies, and coordinate guarded merges across accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad GitHub permissions and token handling could expose credentials or allow unintended account actions.

Mitigation: Review authentication and account-switching guidance, limit granted scopes, and confirm the active account before use.

Risk: Automated language rules or GitHub state changes may be inappropriate for some repositories.

Mitigation: Check repository policies and review proposed public content, pull requests, and merge actions before execution.

## Reference(s):

- [GitHub Flow on ClawHub](https://clawhub.ai/drumrobot/skills/github-flow)
- [Authentication scope guidance](./auth-scope.md)
- [Account identity and authentication guidance](./identity-auth.md)
- [Public content sanitization guidance](./sanitize.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with GitHub issue and pull request text and inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide changes to GitHub issues, pull requests, reviews, and merge status.]

## Skill Version(s):

0.11.3 (source: ClawHub release and CHANGELOG, released 2026-09-27)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
