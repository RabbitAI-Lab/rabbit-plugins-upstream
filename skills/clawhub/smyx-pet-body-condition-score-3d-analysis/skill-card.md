## Description:

Analyzes pet videos through a cloud service to estimate a 3D body condition score (BCS, 1–9) and provide a structured body-shape report without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and developers of pet health tools use multi-angle videos or video URLs to assess body condition, review weight-management observations, and retrieve prior reports. Results are estimates, not veterinary diagnoses or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos or video URLs are sent to configured Life Emergence services.

Mitigation: Share only videos you are authorized to send and review the service's data practices before use.

Risk: The skill may silently create or reuse an identity, store login tokens locally, and retrieve cloud report history.

Mitigation: Use an isolated workspace; remove smyx-common-claw.db and smyx-api-key.txt when cross-run identity reuse is unwanted.

Risk: Visual BCS estimates can differ from a hands-on assessment.

Mitigation: Treat results as weight-management observations and consult a veterinarian for clinical assessment.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-body-condition-score-3d-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured body-condition report or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [BCS score, body-shape observations, report links, and optional saved output]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
