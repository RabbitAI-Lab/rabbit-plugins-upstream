## Description:

Analyzes medication-area video for pill pick-up, movement to the mouth, and swallowing, then reports observed steps and possible incomplete medication events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and elder-care teams use the skill to review medication-area footage for observed pick-up, to-mouth, and swallow actions and to check current or historical adherence reports. Results are an aid to follow-up, not a substitute for medical guidance or direct confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive medication-area images or videos and report history are sent to a cloud service.

Mitigation: Use only with clear consent from the monitored person or authorized caregiver; check the provider's retention, access, deletion, and export safeguards.

Risk: Local workspace records and the smyx-api-key file can retain identities and authentication tokens.

Mitigation: Restrict access to local records and credentials, and manage their retention as sensitive data.

Risk: Visual detection can leave swallowing unobserved or report an incomplete medication event.

Mitigation: Have a caregiver confirm concerning results directly; do not use the output to change medication guidance.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/18072937735/skills/smyx-elderly-medication-compliance-analysis)
- [Medication compliance API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown report list; JSON output available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include adherence status, observed steps, and report links.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
