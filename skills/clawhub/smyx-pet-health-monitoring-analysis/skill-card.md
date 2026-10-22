## Description:

Analyzes pet monitoring videos for feeding, drinking, elimination, behavior, vomiting, and mobility concerns, then provides health reports and access to report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caregivers use this skill to review monitoring footage for possible changes in pet health and retrieve past reports; findings are not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media and report history are processed by a cloud service.

Mitigation: Use non-sensitive media and confirm that cloud processing is acceptable before sharing footage.

Risk: The skill automatically creates or reuses an identity and stores service tokens in the local workspace.

Mitigation: Review or clear workspace data files when persistent account linkage is unwanted.

Risk: Remote video URLs may expose private resources to the service.

Mitigation: Avoid arbitrary private URLs; use only media you are authorized to share.

Risk: Health assessments could be mistaken for veterinary diagnoses.

Mitigation: Treat reports as screening guidance and consult a veterinarian about concerning symptoms.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-health-monitoring-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Structured JSON or text health reports; Markdown report-history table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include health indicators, alerts, suggestions, and report links; results can be saved to a file.]

## Skill Version(s):

1.0.17 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
