## Description:

Analyzes WorkBuddy conversation history across six dimensions and produces a monthly diagnostic report with prioritized actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guipi888](https://clawhub.ai/user/guipi888)

### License/Terms of Use:

MIT-0

## Use Case:

WorkBuddy users review monthly conversation patterns, unfinished tasks and priorities through a six-dimension diagnostic report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Monthly scans may access sensitive personal or business conversations.

Mitigation: Obtain consent, confirm the data scope before use, and avoid automatic runs unless monthly scanning is intended.

Risk: The documentation's title-only privacy claim does not match the helper's ability to export full message bodies.

Mitigation: Check whether the chosen workflow reads titles or full messages; limit transcript exports and review generated files before sharing.

Risk: Generated output includes unrelated promotional text and links.

Mitigation: Review reports and exports, and remove promotional content before distribution.

## Reference(s):

- [WorkBuddy 月度体检 on ClawHub](https://clawhub.ai/guipi888/skills/workbuddy-monthly-checkup)
- [WorkBuddy](https://www.workbuddy.cn)

## Skill Output:

**Output Type(s):** [Markdown, Text, JSON]

**Output Format:** [Monthly Markdown report; optional conversation exports in Markdown, JSON or plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Six-dimension scores and three prioritized actions; optional exports may contain full message bodies.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
