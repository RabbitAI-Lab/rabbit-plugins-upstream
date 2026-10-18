## Description:

Analyzes post-feeding aquarium videos to report fish-feeding activity scores, leftover feed, and appetite alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers and aquaculture operators use this skill to assess feeding behavior from camera footage and review historical feeding reports. It provides activity scores, alerts, and suggested follow-up observations rather than disease diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium footage and identity-linked report history are sent to lifeemergence.com services.

Mitigation: Confirm the service and its data-retention practices are acceptable before sharing footage or querying reports.

Risk: The skill may create or reuse a local user record, read workspace identity files or environment variables, and store authentication tokens in local SQLite.

Mitigation: Review identity access and local credential storage before installation; run only in an environment where these behaviors are authorized.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-fish-feeding-activity-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown history table with report links; optional saved JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scores range from 0 to 100; results are not disease diagnoses.]

## Skill Version(s):

1.0.17 (source: server release; bundled SKILL.md lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
