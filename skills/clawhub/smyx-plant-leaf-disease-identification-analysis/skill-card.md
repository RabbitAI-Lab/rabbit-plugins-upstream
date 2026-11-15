## Description:

Identifies likely plant leaf diseases from images or video and returns a confidence-rated report with general care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External growers, gardeners, and plant-care teams use leaf images or video to identify likely diseases and receive confidence-rated results with general care guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags persistent account data and automatic identity registration beyond the stated plant-analysis purpose.

Mitigation: Review the account setup and identity-handling behavior before installation, and avoid installing if that handling is not acceptable.

Risk: The security assessment says handling of media sent for remote analysis is unclear.

Mitigation: Review data-transfer behavior first and submit only images or videos you are comfortable processing remotely.

Risk: The security assessment notes that its coverage is incomplete because a local reference could not be resolved.

Mitigation: Treat the assessment as incomplete and inspect the skill's account setup and media transfer behavior before use.

## Reference(s):

- [Plant disease identification API documentation](references/api_doc.md)
- [Analysis API error codes](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-plant-leaf-disease-identification-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured Markdown report with disease identification, confidence, general care guidance, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are diagnostic guidance; the skill states that it does not provide specific chemical treatment plans.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
