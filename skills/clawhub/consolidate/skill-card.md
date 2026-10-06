## Description:

Consolidates external feedback on pull requests and issues into classified findings, review summaries, and follow-up decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and PR reviewers use this skill to collect CodeRabbit, Copilot, and other review feedback, classify findings, publish a review summary, and track deferred follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated GitHub access can change PR discussions or publish formal reviews.

Mitigation: Require explicit approval before posting reviews or pushing changes, and install a pinned release.

Risk: Local execution against untrusted PR worktrees can expose secrets or run untrusted code.

Mitigation: Review untrusted fork PRs in an isolated, secret-free environment and approve plugin installs and local tests or builds before running them.

## Reference(s):

- [Consolidate on ClawHub](https://clawhub.ai/drumrobot/skills/consolidate)
- [Superpowers review plugin](https://github.com/obra/superpowers)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown review summaries, findings tables, and review comments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can post GitHub PR comments and formal reviews and record deferred findings.]

## Skill Version(s):

0.7.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
