## Description:

Detects whether anyone has fallen within a target area and supports video stream analysis for real-time safety monitoring of elderly people living alone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and home safety operators use this skill to review video for possible falls and retrieve previous analysis reports. Treat its alerts as prompts for human confirmation; the skill documentation says they do not replace on-site confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security guidance flags remote handling of potentially sensitive video.

Mitigation: Review the service's privacy and data-handling terms and obtain appropriate consent before sending video for analysis.

Risk: The security guidance flags that the export-only option may still perform analysis.

Mitigation: Do not rely on that option to avoid analysis; confirm its behavior before use with sensitive footage.

Risk: The security guidance flags identity or credential management beyond the skill's stated fall-detection purpose.

Mitigation: Review identity and credential handling before installation and limit access to what the deployment requires.

Risk: The security assessment says the scan was partial because a local reference could not be resolved, so its findings are incomplete.

Mitigation: Review the skill and complete an appropriate security scan before installation.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured fall-detection analysis results, with report links and Markdown history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes alert and report details; detection results are for safety reference and require human confirmation.]

## Skill Version(s):

1.0.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
