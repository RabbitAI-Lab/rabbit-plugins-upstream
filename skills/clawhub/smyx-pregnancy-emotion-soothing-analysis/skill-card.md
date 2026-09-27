## Description:

Analyzes pregnancy-related camera footage and optional audio for signs of emotional distress and returns soothing suggestions and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pregnant people and their caregivers can use this skill to review home or prenatal waiting-room recordings for possible emotional distress, receive non-diagnostic soothing guidance, and retrieve prior reports. It may suggest notifying a caregiver or contacting a clinician or support line when distress persists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive pregnancy-related audio and video are sent to a remote analysis service.

Mitigation: Obtain informed consent from the monitored person and bystanders, and confirm retention and deletion controls before use.

Risk: The skill silently creates or reuses an account, stores a local identity token, and can retrieve cloud report history.

Mitigation: Require clear identity and access controls, explain account creation to users, and protect or remove local tokens and stored reports.

Risk: Caregiver notifications can disclose a person's inferred emotional state without their choice of recipient.

Mitigation: Disable notifications unless the monitored person opts in and selects recipients.

Risk: Emotion inference from recordings may be mistaken for a medical diagnosis.

Mitigation: Treat results as non-diagnostic guidance; seek qualified clinical support when appropriate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pregnancy-emotion-soothing-analysis)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured report in text or JSON; Markdown links for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save a report to a file and retrieve cloud-hosted report history.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
