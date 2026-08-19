## Description:

Analyzes uploaded trading journals to identify behavioral patterns, performance leaks, psychological triggers, and retrospective improvement drills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heroinyan-stack](https://clawhub.ai/user/heroinyan-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and trading coaches use this skill to review historical trade logs, spot recurring behavioral and execution issues, and generate a retrospective improvement plan. It is intended for journal analysis and education, not future trade recommendations or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded trade logs may contain sensitive financial records or account identifiers.

Mitigation: Redact account identifiers and unnecessary personal or financial details before use.

Risk: Sizing, setup-selection, instrument-focus, or expected-return language may be mistaken for trading advice.

Mitigation: Treat all recommendations as retrospective educational coaching and require human judgment before any trading decision.

Risk: Small trade samples can make behavioral pattern recognition unreliable.

Mitigation: Use the skill's sample-size warnings and prefer larger journal periods before acting on detected patterns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heroinyan-stack/skills/trade-journal-coach)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report with tables, calculated metrics, warnings, and action-plan sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided trade logs and should include an educational-use disclaimer.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
