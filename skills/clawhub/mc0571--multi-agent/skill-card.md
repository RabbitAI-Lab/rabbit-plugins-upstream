## Description:

Guides authorized multi-agent delegation, task handoffs, independent PR review, and integration while leaving approval and final decisions with the primary agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mc0571](https://clawhub.ai/user/mc0571)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to coordinate explicitly authorized subagents on programming tasks, assign independent reviews, and integrate results. It also guides PR review submissions when the user has authorized public posting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A PR review could be published without the user's authorization.

Mitigation: Require explicit authorization before public submission and keep the review tied to the examined commit.

Risk: Delegation may be mistaken for permission to make unrelated code or GitHub changes.

Mitigation: Keep delegated work within user and repository permissions, with the primary agent responsible for scope and integration.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/mc0571/skills/multi-agent)
- [GitHub pull request review API](https://docs.github.com/en/rest/pulls/reviews#create-a-review-for-a-pull-request)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Text and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task assignments, review findings, and integration guidance as applicable.]

## Skill Version(s):

0.3.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
