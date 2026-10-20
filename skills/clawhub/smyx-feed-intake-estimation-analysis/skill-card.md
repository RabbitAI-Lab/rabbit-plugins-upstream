## Description:

Estimates livestock feed intake from feeder images or videos and reports consumption trends and anomaly alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock managers and agricultural analysts use feeder images or videos to estimate consumption, monitor trends, and review anomalies and historical reports. Results are visual estimates, not feeding or formulation advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Feeder images, videos, or URLs are sent to configured lifeemergence.com services.

Mitigation: Submit only media or URLs approved for external processing.

Risk: The skill silently creates or reuses an identity, stores tokens in the workspace data directory, and can query account-linked report history.

Mitigation: Use a separate workspace or account when media and reports should not be linked to other analyses; protect local token storage.

## Reference(s):

- [Feed intake estimation API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or JSON analysis report; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes feed-intake estimates, trends, anomaly alerts, and report links; can save the result to a file.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
