## Description:

Detects abnormal body temperature rise or drop in livestock and poultry from thermal or visible-light imagery, and outputs fever/hypothermia early warnings based on visual thermal features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock farm operators and animal health teams use this skill to screen livestock and poultry images or short videos for unusual surface temperature patterns, review estimated temperatures and anomaly levels, and retrieve analysis reports. Results support screening and do not provide a disease diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Analysis may send imagery and identity data to remote services.

Mitigation: Before use, confirm where imagery and identity data are sent and whether that handling is appropriate for the data being analyzed.

Risk: Account and credential handling is not clearly declared.

Mitigation: Review how accounts and API tokens are handled and stored before installation.

Risk: The export-only option may still run analysis.

Mitigation: Confirm the option's behavior before relying on it to avoid analysis or network activity.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-fever-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis reports and Markdown report lists with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include estimated temperature ranges, anomaly levels, individual locations, abnormal-animal lists, group summaries, and report links; screening results only.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
