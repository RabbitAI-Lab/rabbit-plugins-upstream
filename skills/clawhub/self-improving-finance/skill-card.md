## Description:

Captures reconciliation errors, forecast variances, control weaknesses, regulatory gaps, valuation errors, and cash flow anomalies to support continuous finance operations improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Finance teams and agent users use this skill to record anonymized finance issues, learnings, and feature requests as local markdown entries. It supports later review and promotion of recurring patterns into close checklists, reconciliation procedures, control matrices, tax calendars, forecast models, or audit response templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local finance logs may expose regulated, client-identifying, or otherwise sensitive financial data if populated with real account numbers, client names, exact figures, credentials, or raw transcripts.

Mitigation: Keep entries anonymized with placeholders and never record real account numbers, bank details, client names, credentials, exact figures, or raw transcripts.

Risk: Optional reminder hooks may be too broad for the intended finance workflow, and PostToolUse scanning may inspect sensitive command output.

Mitigation: Keep hooks project-scoped, start with the activator-only hook, use narrow finance matchers, and enable PostToolUse only when command-output scanning is acceptable.

Risk: Promoted procedures or generated skills could encode incorrect finance guidance if accepted without review.

Mitigation: Review generated skills and proposed promotions before accepting them, and apply changes only after explicit approval.

## Reference(s):

- [OpenClaw Integration](artifact/references/openclaw-integration.md)
- [Hook Setup Guide](artifact/references/hooks-setup.md)
- [Entry Examples](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown entries and reminder text with inline shell and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or appends local .learnings markdown files when the workflow is followed; optional hooks emit reminder text and do not need to log raw command output.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
