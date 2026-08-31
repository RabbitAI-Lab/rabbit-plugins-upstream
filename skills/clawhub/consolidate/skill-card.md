## Description:

Consolidate and respond to external PR and issue feedback by gathering AI reviews, classifying findings, posting an AI Review Summary and Formal Review, and registering deferred items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering reviewers use this skill to consolidate PR or issue feedback from CodeRabbit, GitHub Copilot, internal review, and human comments into a structured review outcome. It helps classify findings, prepare review summaries, post formal review artifacts, and track deferred work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish GitHub reviews, edit PR metadata, write tracking files, and in limited cases push branch updates without consistently requiring fresh user approval.

Mitigation: Use --interactive when possible, verify the active GitHub account and token before running, and review drafted artifacts before posting or editing PR content.

Risk: The skill can create durable review records on shared or public repositories.

Mitigation: Run it only where the agent is authorized to act, confirm the target repository and PR number, and use the included validation workflow before treating the consolidation as complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/consolidate)
- [README](README.md)
- [Skill workflow](SKILL.md)
- [Posting and verification workflow](post.md)
- [Consolidation validator](scripts/verify_consolidate.py)
- [Superpowers plugin](https://github.com/obra/superpowers)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown review comments, structured tables, status text, next-action prompts, and inline shell or GitHub CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update GitHub review artifacts, PR metadata, tracking records, and local draft files depending on workflow path and user approval mode.]

## Skill Version(s):

0.6.1 (source: frontmatter, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
