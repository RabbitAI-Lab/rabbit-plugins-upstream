## Description:

Consolidate helps agents gather external PR and issue feedback, classify review findings, coordinate decisions, and post review summaries and formal review outcomes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and maintainers use this skill to consolidate CodeRabbit, GitHub Copilot, internal review, and human PR feedback into clear findings, decisions, summaries, formal reviews, and deferred follow-up records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can post or patch PR reviews and comments, edit promotion PR descriptions, and register deferred work.

Mitigation: Use interactive mode for review-before-post and approve drafts before publishing durable GitHub or tracking changes.

Risk: The skill operates through the user's GitHub credentials when managing PR review workflow.

Mitigation: Use least-privilege GitHub authentication and install it only where active PR review management is intended.

## Reference(s):

- [Consolidate Skill on ClawHub](https://clawhub.ai/drumrobot/skills/consolidate)
- [README](README.md)
- [Skill Definition](SKILL.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples, review summaries, formal review text, and deferred-work records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or propose durable GitHub review comments, PR comments, status text, and local tracking files depending on user approval and mode.]

## Skill Version(s):

0.5.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
