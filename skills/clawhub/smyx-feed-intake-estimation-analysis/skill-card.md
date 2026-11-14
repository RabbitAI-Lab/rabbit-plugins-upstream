## Description:

Estimates daily feed intake per livestock individual from continuous feeder videos by tracking the change of feed remaining in the trough, and outputs intake trend with anomaly alerts. | 通过食槽视频估算每日采食量变化，异常时预警。

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock managers and farm operators can use feeder-area images or videos to estimate daily feed intake, review consumption trends, and spot potential anomalies. Results are visual estimates; the skill does not provide feeding adjustments or feed formulation advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the skill suspicious and says its account and credential handling, remote requests, and video processing require review; the advertised analysis behavior is not demonstrated in the visible implementation.

Mitigation: Review those behaviors and confirm the service and analysis results are suitable for your use before installing or relying on the skill.

Risk: Security scan coverage is partial because a local reference was missing, so the scan does not settle what that reference contains.

Mitigation: Review the complete release contents, including any missing references, before deployment.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill introduction](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-feed-intake-estimation-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Structured feed intake estimates and trends with anomaly alerts; JSON or Markdown report text, with a report link when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual estimates based on feeder images or videos; may include daily intake, historical trends, anomaly levels, and report links.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
