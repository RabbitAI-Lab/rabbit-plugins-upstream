## Description:

GitHub Flow guides agents through GitHub issue, pull request, review, merge, dependency, publishing, and sanitization workflows using gh CLI procedures and guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to turn plans and implementation work into GitHub issues, pull requests, review comments, dependency records, and merges while preserving verification, account, and publication hygiene.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use existing GitHub credentials for broad write and auth-sensitive actions.

Mitigation: Install it only for GitHub workflow automation use cases, limit the active GitHub account and token scopes, and confirm the target repository and PR or issue before every write.

Risk: Some workflows can mutate GitHub state or post issue, PR, review, dependency, or merge actions without a clear per-action confirmation.

Mitigation: Require explicit user confirmation for state-changing operations, inspect generated bodies before posting, and prefer draft PRs unless the user requests ready-for-review publication.

Risk: Account switching and token injection can cause actions to run under the wrong GitHub identity if not verified.

Mitigation: Verify the active GitHub account before and after account-sensitive commands, use command-scoped token wrappers where appropriate, and restore the original account immediately after switched-account operations.

Risk: Local policy files and drafts can influence public GitHub content and may include private paths or personal data.

Mitigation: Run the documented sanitization checks before creating or editing public-facing issues, PRs, comments, review text, or merge messages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/github-flow)
- [Skill overview](SKILL.md)
- [Changelog](CHANGELOG.md)
- [Auth Scope](auth-scope.md)
- [Identity Auth](identity-auth.md)
- [PR Creation](pr.md)
- [Merge](merge.md)
- [Issue Dependencies and Sub-issues](dependencies.md)
- [Sanitize](sanitize.md)
- [Review](review.md)
- [Review Apply](review-apply.md)
- [Publish](publish.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown instructions with inline shell commands and JSON/API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces issue and PR bodies, review text, GitHub CLI/API command sequences, and local wrapper script usage.]

## Skill Version(s):

0.9.0 (source: ClawHub release metadata and CHANGELOG, released 2026-08-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
