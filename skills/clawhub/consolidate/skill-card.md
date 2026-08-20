## Description:

Consolidate and respond to external PR and issue feedback by gathering AI reviews, classifying findings, posting an AI Review Summary and Formal Review, and registering deferred items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and maintainers use this skill to consolidate AI bot and internal review feedback on GitHub pull requests, decide formal review posture, publish review summaries, and preserve deferred follow-up work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make durable GitHub and local-workspace changes, including posting reviews or comments and updating tracking files.

Mitigation: Install it only for workflows where active PR-review operation is intended, and use interactive mode when draft review bodies should be approved before posting.

Risk: Formal reviews, review comments, or inline annotations can create persistent PR records and may be difficult to clean up after duplicate or wrong-medium posts.

Mitigation: Follow the built-in draft, duplicate-review, requested-reviewer, existing-review, and post-publish verification gates before each GitHub write.

Risk: The workflow can create follow-up issues or perform code changes in allowed fix paths.

Mitigation: Require explicit user instruction for fixes, honor branch ownership checks, and register deferred items in the selected tracking medium rather than silently applying changes.

## Reference(s):

- [Consolidate on ClawHub](https://clawhub.ai/drumrobot/skills/consolidate)
- [superpowers plugin](https://github.com/obra/superpowers)
- [requesting-code-review skill](https://skills.sh/obra/superpowers/requesting-code-review)
- [receiving-code-review skill](https://skills.sh/obra/superpowers/receiving-code-review)
- [CodeRabbit CLI](https://www.coderabbit.ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown review bodies, shell commands, JSON payloads, local tracking entries, and concise chat status updates.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May post GitHub PR reviews or comments, update local tracking files, create follow-up issues, and make code changes only when the workflow branch and user-instruction gates allow it.]

## Skill Version(s):

0.5.4 (source: frontmatter, release metadata, changelog released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
