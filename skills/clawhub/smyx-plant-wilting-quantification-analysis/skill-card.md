## Description:

Analyzes full-plant images to estimate wilting severity and, when soil-moisture data is available, distinguish underwatering from overwatering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as home gardeners and greenhouse growers can submit a plant image or video to estimate wilting severity and possible causes, then receive a report with general irrigation or drainage direction. They can also request previously generated reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious because of reported account and credential handling, broad or undisclosed external processing, and other behavior that may not match its stated purpose. The scan is incomplete because a referenced local path was missing; the verdict is suspicious, not malicious.

Mitigation: Before installing or sending images, clarify the publisher's identity, how credentials and identity data are handled, and where media is processed; limit use to the data and access you need.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-plant-wilting-quantification-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)
- [Analysis API errors and response reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Structured analysis report; JSON detail is supported and report lists are formatted as Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes an estimated wilting score (0–100%), likely cause, and general intervention direction; it does not provide a specific watering amount. Without soil-moisture data, cause identification is an estimate.]

## Skill Version(s):

1.0.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
