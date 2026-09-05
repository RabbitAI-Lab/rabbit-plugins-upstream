## Description:

Analyze reviews or public customer feedback across multiple sources and produce themes, sentiment signals, and product actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users, product teams, and developers use this skill to turn public customer reviews into themes, sentiment signals, source-bias notes, and prioritized product actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Dataify account token and may spend Dataify credits while collecting public review data.

Mitigation: Keep the token in an environment variable, never paste it into chat, and use dry-run or max-action limits when cost control is needed.

Risk: Review samples and sentiment counts may be incomplete or biased by source, market, period, or platform coverage.

Mitigation: Report sample size, source bias, date range, platform coverage, and evidence-linked examples instead of treating sentiment counts as ground truth.

Risk: A timed-out paid task could be submitted again and duplicate credit usage.

Mitigation: Preserve and resume the task ID when monitoring stops instead of submitting the same target again.

## Reference(s):

- [Dataify Review Intelligence skill page](https://clawhub.ai/dataify-server/skills/dataify-review-intelligence)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise analysis, evidence-linked examples, and optional shell commands for setup or execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports sample size, platform bias, rating or sentiment signals, concrete examples, and prioritized actions.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
