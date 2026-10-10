## Description:

Analyzes pet camera or feeder footage for feeding, drinking, excretion, activity, vomiting, and limping indicators and produces health monitoring reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and their agents use camera or feeder footage to review pet behavior, identify possible health anomalies, and retrieve past monitoring reports. Results are informational and do not replace veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet footage, file URLs, and report history are sent to a cloud service.

Mitigation: Use only with informed consent; review the service's data handling and deletion options before uploading sensitive footage.

Risk: The integration can silently create or reuse a service identity and store authentication tokens locally.

Mitigation: Treat it as an account-linked integration; review local workspace data and remote reports, and plan how to revoke access and delete both.

Risk: Behavior-based health assessments may be mistaken for a veterinary diagnosis.

Mitigation: Treat findings as informational and consult a veterinarian when concerning symptoms appear.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-health-monitoring-analysis)
- [Pet health analysis API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Text or Markdown health reports and history tables, with optional JSON results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include behavior summaries, possible anomalies, suggestions, and links to cloud-hosted reports.]

## Skill Version(s):

1.0.16 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
