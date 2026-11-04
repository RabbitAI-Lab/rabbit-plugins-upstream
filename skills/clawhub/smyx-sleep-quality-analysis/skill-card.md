## Description:

Identifies sleep stages including falling asleep, light sleep, deep sleep, and REM; monitors body movement, nighttime awakenings, and sleep apnea, suitable for sleep monitoring scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

People using sleep-monitoring videos can request analysis of sleep stages, movement, awakenings, and breathing patterns, with structured findings and report links. The skill also supports looking up prior reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says private sleep recordings may be uploaded despite a no-analysis option, and cloud accounts may be created silently.

Mitigation: Avoid private recordings until the no-analysis option is fixed and cloud uploads, account enrollment, and token storage are clearly controlled. Confirm the provider's retention, deletion, and charging practices, and use a dedicated account and workspace.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sleep-quality-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured JSON analysis reports and Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include sleep-stage estimates, movement and awakening observations, breathing-related findings, suggestions, and report links.]

## Skill Version(s):

1.0.19 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
