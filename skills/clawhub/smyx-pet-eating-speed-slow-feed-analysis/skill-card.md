## Description:

Analyzes pet-feeding videos to estimate feeding duration and speed, compare results with reference thresholds, and provide non-diagnostic slow-feeding intervention guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and developers use this skill to review feeding videos, track feeding duration and estimated speed, and get threshold-based prompts for possible slow-feeding interventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video processing may upload clips to Life Emergence even when a no-analysis option is selected.

Mitigation: Have the publisher fix the ignored option before using private footage; use only clips approved for external processing and review the service privacy terms.

Risk: The skill may create service accounts automatically and retain login tokens locally.

Mitigation: Protect the workspace database and stored tokens, and avoid sensitive footage until the account and credential behavior is reviewed.

## Reference(s):

- [API interface notes](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-eating-speed-slow-feed-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis with feeding timestamps, estimated speed, threshold assessment, intervention guidance, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Non-diagnostic; intervention signals are recommendations for an external device.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
