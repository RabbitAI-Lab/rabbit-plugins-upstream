## Description:

Analyzes turtle enclosure camera images or videos for visual signs associated with abnormal open-mouth breathing, mucus, nasal discharge, posture changes, and related respiratory risk warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and turtle-care operators use this skill to submit clear turtle enclosure media for structured visual screening of respiratory warning signs and to retrieve cloud-stored report history. It is a visual risk-warning aid, not a veterinary diagnosis or treatment plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Turtle tank media and report history may be sent to the publisher's backend.

Mitigation: Submit only videos or URLs intended for cloud analysis, and avoid broad history-query prompts unless account-linked records should be retrieved.

Risk: The skill automatically links users to cloud accounts and persists session tokens locally with limited user control.

Mitigation: Review how to delete or revoke local SQLite tokens and any cloud account data created by the skill before installation or after use.

Risk: Respiratory risk warnings could be mistaken for veterinary diagnosis or treatment guidance.

Mitigation: Treat outputs as visual screening only, avoid drug or dosage recommendations, and confirm concerning results with a professional reptile veterinarian.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-turtle-pneumonia-symptom-detection-analysis)
- [Skill usage demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [JSON or Markdown text with structured report fields and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include symptom indicators, alert level, non-prescriptive recommended actions, disclaimers, and cloud report export links.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
