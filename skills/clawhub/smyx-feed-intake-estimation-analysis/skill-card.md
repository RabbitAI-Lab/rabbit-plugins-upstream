## Description:

Estimates daily feed intake per livestock individual from continuous feeder videos by tracking the change of feed remaining in the trough, and outputs intake trend with anomaly alerts. | 通过食槽视频估算每日采食量变化，异常时预警。

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock farm operators use the skill to estimate daily feed intake from feeder images or videos, review intake trends and anomaly alerts, and retrieve prior analysis reports. Results are visual estimates for reference and do not provide feed adjustment or formulation advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export-only option is ineffective and may not prevent analysis from running.

Mitigation: Treat it as an executing analysis until the option is fixed and verified.

Risk: Submitted videos are uploaded to LifeEmergence, whose retention and processing costs need confirmation.

Mitigation: Confirm the provider's retention and processing costs before supplying private footage.

Risk: Account tokens persist locally, and the security evidence calls for fixes to credential handling.

Mitigation: Seek credential-handling fixes before supplying real credentials.

## Reference(s):

- [API interface notes](references/api_doc.md)
- [Skill introduction](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-feed-intake-estimation-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured JSON analysis results and Markdown historical report lists with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Daily intake estimates, trends, anomaly alerts, and report links; estimates are for reference only.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
