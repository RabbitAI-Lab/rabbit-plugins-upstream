## Description:

Screens poultry and pig barn images or videos for abnormal behavior and returns risk-ranked analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators and animal-health teams use this skill to screen poultry and pig barn footage for concerning behaviors, review risk levels, and retrieve past reports. Results support observation and veterinary follow-up, not diagnosis or treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn images or videos are sent to Life Emergence cloud services for analysis.

Mitigation: Get permission before sending footage, and avoid including unnecessary sensitive content.

Risk: The skill may silently create or reuse an identity, register or log in remotely, and store authentication tokens locally.

Mitigation: Require informed approval before use, restrict access to local tokens, and request a documented way to disable or delete stored identity data.

Risk: Behavioral risk scores may be mistaken for a veterinary diagnosis.

Mitigation: Treat results as screening signals and seek veterinary assessment before diagnosis or treatment decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-sick-poultry-behavior-detect-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Text or JSON analysis report; Markdown table for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Behavior categories, risk level, affected animal locations, and report links when available.]

## Skill Version(s):

1.0.9 (source: server-resolved ClawHub release metadata; artifact frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
