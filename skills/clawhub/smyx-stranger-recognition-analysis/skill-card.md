## Description:

Helps security operators compare faces in images or videos with a known-person database and review stranger-recognition reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security operators and developers use this skill to review potential strangers in access-control or surveillance images and videos, enroll known people, and retrieve past reports. Its results are intended to inform human security decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Biometric surveillance images and identity information are sent to cloud services.

Mitigation: Require a privacy and consent review before use; limit deployment to approved surveillance contexts.

Risk: Automatic identity creation and reused tokens may expose one operator's reports or enrollments to another.

Mitigation: Isolate each operator's workspace, disallow caller-supplied identities and shared fallback identities, and verify server-side ownership for listing, export, enrollment, and analysis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-stranger-recognition-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured recognition reports, report lists, and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a file and link to cloud-hosted reports.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
