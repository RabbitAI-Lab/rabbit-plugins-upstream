## Description:

Consolidates external PR and issue feedback into classified findings, review summaries, and next-step guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and reviewers use this skill to gather PR feedback, assess findings, publish review summaries, and track deferred follow-up work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish GitHub reviews and comments on behalf of the user.

Mitigation: Enable interactive review of drafts and confirm the account, target PR, and message before posting.

Risk: Reviewing untrusted PR code can expose agents to unsafe content while creating local worktrees.

Mitigation: Use a sandbox for untrusted fork PRs and inspect the checkout before granting agent execution.

Risk: Plugin and hook installation can introduce persistent local changes.

Mitigation: Review requested plugins and hooks before installing or enabling them.

## Reference(s):

- [Consolidate on ClawHub](https://clawhub.ai/drumrobot/skills/consolidate)
- [Superpowers code-review plugin](https://github.com/obra/superpowers)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Files]

**Output Format:** [Markdown review summaries, findings, and follow-up plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May publish GitHub comments or formal reviews and record deferred findings locally.]

## Skill Version(s):

0.8.1 (source: frontmatter, CHANGELOG, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
