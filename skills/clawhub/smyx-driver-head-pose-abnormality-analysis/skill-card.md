## Description:

Analyzes driver-facing video for head-down and side-view events and returns distracted-driving alerts and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Fleet operators and developers use this skill to assess driver-facing videos for prolonged head-down or side-view behavior and review distraction reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver video is uploaded to an external service and may contain sensitive biometric information.

Mitigation: Obtain informed driver or employee consent and confirm the backend domain, retention policy, and fleet-data requirements before use.

Risk: The skill silently creates or reuses identities and stores tokens locally.

Mitigation: Review the publisher and token storage model before installation; restrict access to local credentials.

Risk: Broad history requests can retrieve identity-linked cloud reports.

Mitigation: Limit report access to authorized users and verify consent for identity-linked history retrieval.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-driver-head-pose-abnormality-analysis)
- [Head-pose analysis API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis results, distracted-driving alerts, report links, and Markdown history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a file and retrieve identity-linked cloud report history.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release; bundled SKILL.md says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
