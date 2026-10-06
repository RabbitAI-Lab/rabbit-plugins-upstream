## Description:

Analyzes video and optional audio for signs of emotional distress during pregnancy and provides structured reports and soothing responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Expectant parents and care teams use this skill to review camera footage and optional audio from homes or prenatal waiting rooms for signs of emotional distress, receive a structured report, and initiate soothing actions or approved contact notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive pregnancy audio and video could be processed without informed consent, particularly in shared spaces.

Mitigation: Obtain explicit consent from every monitored person; provide visible clinic notice and an opt-out before use.

Risk: External API uploads and local identity token or database persistence may expose sensitive data.

Mitigation: Review the external data transfer and local retention practices before installing; limit access to recordings and stored credentials.

Risk: Automatic messages to a husband or emergency contact can reveal private emotional information or create danger in an unsafe relationship.

Mitigation: Notify only contacts approved by the monitored person and do not deploy for covert monitoring or in unsafe relationship contexts.

Risk: Emotion inferences from footage may be mistaken for a clinical assessment.

Mitigation: Treat results as supportive signals, not a medical diagnosis; refer persistent concerns to qualified prenatal care or mental health services.

## Reference(s):

- [Pregnancy emotion soothing API documentation](references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-pregnancy-emotion-soothing-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown history table with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be saved to a file.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
