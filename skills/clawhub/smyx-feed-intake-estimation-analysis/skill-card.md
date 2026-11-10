## Description:

Estimates daily feed intake per livestock individual from continuous feeder videos by tracking the change of feed remaining in the trough, and outputs intake trend with anomaly alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock producers and feed-management teams can use feeder-trough images or videos to estimate individual or group intake over time and review trend changes or anomaly alerts. The estimates are visual guidance and do not provide ration or feed-formula recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious for account and credential handling beyond its stated livestock-analysis purpose.

Mitigation: Before use, review whether video upload, account creation, identity and token storage, and broad report lookup are necessary and acceptable for your deployment.

Risk: ClawScan reports unexpected remote and local side effects, and its scan was partial because a referenced local path was missing.

Mitigation: Inspect the missing referenced path and review the relevant upload and report lookup behavior before processing data.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-feed-intake-estimation-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured intake estimates and trend or anomaly results in JSON, with Markdown report listings and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual estimates; includes intake trends and anomaly alerts when available]

## Skill Version(s):

1.0.15 (source: target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
