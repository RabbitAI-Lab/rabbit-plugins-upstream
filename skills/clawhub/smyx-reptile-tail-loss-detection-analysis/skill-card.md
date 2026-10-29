## Description:

This skill analyzes gecko and lizard tail images against historical or body-length references to identify possible tail shortening, wounds, scabs, and tail-loss events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers can use the skill to review tail images or videos, receive structured visual findings, and look up prior tail-loss reports. The results are visual monitoring output and should not be treated as a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that selecting the no-analysis option may still permit footage uploads.

Mitigation: Wait for the no-analysis option to be fixed. For testing, use nonsensitive footage in a separate workspace.

Risk: Cloud account enrollment and token storage lack clearly explained user control, and cloud upload, pricing, and retention terms are unclear.

Mitigation: Wait until account enrollment, token storage, upload behavior, pricing, and retention are clearly explained before using the service with production footage or credentials.

Risk: Installation does not establish that daily camera monitoring is configured or running.

Mitigation: Do not assume automatic daily monitoring; confirm the monitoring setup separately.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill introduction demo](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-reptile-tail-loss-detection-analysis)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Guidance]

**Output Format:** [Structured visual analysis reports and historical report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event timestamps, measurements, findings, recommendations, and report links.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
