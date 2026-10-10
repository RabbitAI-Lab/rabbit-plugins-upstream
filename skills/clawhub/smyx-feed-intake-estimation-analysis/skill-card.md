## Description:

Estimates daily livestock feed intake from feeder images or videos and reports intake trends and anomaly alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock operators and farm managers use feeder footage to estimate individual or group feed intake, monitor trends, and review anomalies or past reports. Results are visual estimates, not feeding or ration advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media or media URLs are sent to a remote analysis service.

Mitigation: Send only approved feeder footage and URLs; review remote data handling before use.

Risk: The skill automatically creates or reuses a cloud identity and stores returned tokens locally.

Mitigation: Avoid installation until identity override and token storage are tightened; use only an isolated workspace with trusted users if evaluating it.

Risk: Cloud report history access and import-path behavior require review.

Mitigation: Restrict access to trusted users and review history permissions and import-path behavior before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-feed-intake-estimation-analysis)
- [ClawHub publisher profile](https://clawhub.ai/user/18072937735)
- [Feed intake API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown report-history table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Daily intake estimates, trends, anomaly alerts, and links to cloud reports.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; bundled SKILL.md lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
