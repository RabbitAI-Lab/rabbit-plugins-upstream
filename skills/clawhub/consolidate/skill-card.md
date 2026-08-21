## Description:

Consolidate gathers external PR feedback, runs internal review fallback, classifies findings, and helps post an AI Review Summary, Formal Review, status line, and deferred-item tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and maintainers use this skill to review pull-request feedback from CodeRabbit, Copilot, and internal review, decide what to fix or defer, and publish consistent GitHub review summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can post or patch GitHub review comments and formal review decisions, which may affect repository review state or mergeability.

Mitigation: Use interactive mode for normal operation and review generated GitHub posts before publication.

Risk: The skill uses the caller's gh authentication and can request reviewers, edit promotion PR bodies, and write local tracking records.

Mitigation: Install it only for active GitHub PR review workflows and run it in workspaces where those repository actions and tracking writes are intended.

Risk: Incorrect consolidation can omit findings or create misleading PR review summaries.

Mitigation: Use the bundled verification workflow and keep Internal Code Review and AI Review Summary outputs paired and sequential.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/consolidate)
- [README](artifact/README.md)
- [Workflow index](artifact/SKILL.md)
- [PR workflow](artifact/pr.md)
- [Collect AI reviews](artifact/collect.md)
- [Analyze and classify](artifact/classify.md)
- [Post summary and formal review](artifact/post.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, GitHub comments or reviews, shell commands, and local tracking entries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use gh-authenticated API calls to read and post PR comments or reviews and write local deferred tracking records.]

## Skill Version(s):

0.6.0 (source: frontmatter, release evidence, CHANGELOG released 2026-08-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
