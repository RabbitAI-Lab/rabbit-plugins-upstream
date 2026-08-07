## Description:

Consolidate and respond to external PR and issue feedback by gathering AI reviews, classifying findings, posting review summaries or formal reviews, and registering deferred follow-up items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and code reviewers use this skill to consolidate PR feedback from tools such as CodeRabbit, GitHub Copilot, and internal review flows into actionable findings, review comments, formal review decisions, and deferred tracking records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can post or modify GitHub PR review artifacts, including issue comments and formal reviews.

Mitigation: Invoke it explicitly for PR review work and use --interactive when draft review bodies should be approved before posting.

Risk: Deferred findings may be written into local trackers or opened as GitHub issues.

Mitigation: Review the proposed tracking medium and issue-creation options before approving follow-up actions.

Risk: Bundled hook scripts can block or steer review-comment workflows once registered.

Mitigation: Review the hook scripts before enabling them in an agent environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/consolidate)
- [README](README.md)
- [Consolidate workflow](SKILL.md)
- [PR review entrypoint](pr.md)
- [Post AI Review Summary and Formal Review](post.md)
- [Superpowers plugin](https://github.com/obra/superpowers)
- [receiving-code-review](https://skills.sh/obra/superpowers/receiving-code-review)
- [requesting-code-review](https://skills.sh/obra/superpowers/requesting-code-review)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown review summaries, formal review bodies, status text, follow-up options, and shell commands for GitHub PR review workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May draft or post GitHub PR comments, formal reviews, and deferred tracking records depending on workflow state and user-selected options.]

## Skill Version(s):

0.5.1 (source: frontmatter, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
