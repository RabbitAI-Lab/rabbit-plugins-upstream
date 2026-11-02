## Description:

Analyzes infant sleep monitoring images or videos to classify sleep states, summarize sleep duration and awakenings, and produce reports and routine analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents use the skill to review an infant's sleep patterns and read daily sleep reports. Treat the analysis as parenting reference, not medical advice; consult a pediatrician about sleep concerns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An export-only request can still upload baby videos, while remote account creation and credential storage lack clear user control.

Mitigation: Before using nursery footage, confirm upload, retention, deletion, and account-creation practices; request fixes for export-only behavior, Windows HTTP logging, and credential protection.

Risk: Sleep-state analysis may be mistaken for medical guidance.

Mitigation: Use reports for parenting reference only and consult a pediatrician about abnormal sleep.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [Skill Demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured sleep analysis reports in JSON or readable text, with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize sleep states, sleep duration, awakenings, and routine patterns]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
