## Description:

Provides structured decision support that learns a user's decision style, risk profile, and framework preferences while helping with multi-option tradeoffs, risk/benefit analysis, time-sensitive decisions, and retrospectives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[0xneosoul](https://clawhub.ai/user/0xneosoul)

### License/Terms of Use:

MIT-0

## Use Case:

External ClawHub users and developers use this skill to structure decisions, compare tradeoffs, surface assumptions, track decision outcomes, and improve future decision support from locally stored preferences and retrospectives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persistently stores decision habits, risk profile, framework preferences, and decision records in ~/decision-making/, which may contain sensitive personal or business context.

Mitigation: Install only when local persistent decision memory is desired, periodically inspect or delete ~/decision-making/, and avoid storing credentials, medical details, exact financial data, third-party sensitive information, or location patterns.

Risk: The setup flow can propose edits to global agent steering files such as SOUL.md, AGENTS.md, and HEARTBEAT.md, which may affect future agent behavior beyond one conversation.

Mitigation: Review each proposed steering change before applying it and consider skipping global steering integration when the decision-support behavior should stay project-scoped.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/0xneosoul/skills/neosoul-decision-agent)
- [Publisher profile](https://clawhub.ai/user/0xneosoul)
- [Skill homepage](https://clawic.com/skills/decision-making)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured decision analyses, confidence tags, local file templates, and occasional shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local persistent state under ~/decision-making/ for decision preferences, framework choices, decision records, retrospectives, and heartbeat markers.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
