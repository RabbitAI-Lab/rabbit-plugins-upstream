## Description:

Analyzes greenhouse plant images or videos alongside environmental sensor readings and returns structured assessments and climate-control recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Greenhouse operators use this skill to assess plant stress from images or videos and sensor readings, then review prioritized suggestions for irrigation, shading, ventilation, or heating.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Footage may be uploaded even when export-only mode is selected, and remote analysis behavior has not been verified.

Mitigation: Use only footage approved for external processing, confirm provider retention and deletion terms, and verify export-only behavior before handling sensitive footage.

Risk: Account enrollment and stored credential handling lack clear user control.

Mitigation: Protect credentials, confirm provider charging terms, and avoid real credentials until account handling is clarified.

Risk: Climate-control recommendations may be inappropriate for local greenhouse conditions.

Mitigation: Review recommendations and require local controller safeguards before taking action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-greenhouse-climate-plant-feedback-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API interface reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis reports in JSON or text, with Markdown report lists when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes prioritized climate-control suggestions and report links; treat suggestions as decision support subject to local controller safeguards.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
