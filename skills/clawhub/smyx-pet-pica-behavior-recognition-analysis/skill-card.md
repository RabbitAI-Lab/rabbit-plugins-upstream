## Description:

Analyzes indoor pet videos for sustained contact between a pet’s mouth and hazardous non-food items, then returns a warning and structured report without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and smart-home operators use the skill to review indoor camera videos for possible chewing or contact with hazardous non-food objects and receive warning signals and follow-up suggestions. It does not provide medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment says video may be sent for remote analysis unexpectedly.

Mitigation: Before submitting footage, confirm that the service is trusted and that people shown in the video have appropriate consent; avoid sending sensitive footage.

Risk: The security assessment reports credential and privacy concerns, including account, profile, and history features.

Mitigation: Review the service’s credential handling and account and history behavior before connecting it to personal data.

Risk: The security scan was partial because a referenced item was missing, leaving some behavior unverified.

Mitigation: Verify the complete release contents and the missing referenced item before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-pica-behavior-recognition-analysis)
- [API documentation](references/api_doc.md)
- [Skill usage demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis report with warning results, suggestions, and a report link; JSON or Markdown detail is available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-video analysis; the documented warning threshold is contact lasting at least 2 seconds. No disease diagnosis.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
