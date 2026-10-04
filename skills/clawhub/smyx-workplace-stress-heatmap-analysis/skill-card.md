## Description:

Analyzes workplace camera footage to produce zone-level stress estimates, heatmap reports, and historical report listings for organizational wellness monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Workplace managers and organizational wellness teams use office camera recordings or video URLs to review zone-level stress estimates, heatmaps, trends, and past reports rather than individual assessments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive workplace camera media or video URLs are sent to a third-party cloud service.

Mitigation: Obtain employee notice and consent before use, and approve the cloud data transfer before sending footage or URLs.

Risk: Automatically created account-linked identities and locally or remotely retained report history may undermine anonymity claims.

Mitigation: Ask the provider to document retention, access controls, and deletion for identities and reports before deployment.

Risk: Small-group results could permit employee re-identification despite zone-level aggregation.

Mitigation: Confirm that minimum group sizes and output controls prevent employee-level identification before relying on anonymity claims.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-workplace-stress-heatmap-analysis)
- [Workplace stress heatmap API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured JSON-like analysis text or Markdown report listings with links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Zone-level stress indicators, heatmap or report links, trends, and manager suggestions when available.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
