## Description:

Identifies likely plant leaf diseases from images or videos and returns visible lesion findings, confidence scores, and general care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as growers, greenhouse staff, and home gardeners use the skill to review plant leaf images or videos, identify likely disease patterns, and view confidence-scored findings with general management guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may silently create an account and save login tokens in workspace storage.

Mitigation: Use an isolated workspace and avoid sensitive credentials until account creation is explicit and token handling is clear.

Risk: Submitted media is sent to LifeEmergence services, and export-only mode may still upload media.

Mitigation: Use non-sensitive images and confirm upload behavior before submitting media, especially when selecting export-only mode.

Risk: The security guidance calls for restricting credential destinations to approved HTTPS services.

Mitigation: Use only approved HTTPS destinations for credentials.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-plant-leaf-disease-identification-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured disease analysis report (JSON by default); Markdown for report lists and summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include likely disease labels, confidence scores, general management guidance, and report links; does not provide specific chemical treatment plans.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
