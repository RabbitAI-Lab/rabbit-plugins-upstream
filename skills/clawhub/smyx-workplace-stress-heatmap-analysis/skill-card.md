## Description:

Analyzes workplace camera footage to produce zone-level group stress heatmaps, trends, and management suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Workplace managers and organizational health teams use office camera footage to review aggregated stress patterns by workstation zone, compare trends, and access historical reports. The results are group-level indicators, not individual diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workplace camera footage and stress-related inferences are sent to LifeEmergence cloud services.

Mitigation: Use only with authorization to transmit footage; confirm employee notice and consent and the service's retention and deletion terms before deployment.

Risk: Claims of anonymity may not reflect what backend processing actually retains or exposes.

Mitigation: Verify that processing prevents employee identification and restrict access to heatmaps and historical reports.

Risk: The skill may silently create or reuse an account identity and store tokens in a local workspace database.

Mitigation: Review local credential storage and access controls before installation and limit workspace access.

## Reference(s):

- [Workplace group stress heatmap API reference](references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-workplace-stress-heatmap-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON with report and heatmap links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Zone-level stress indicators, trends, management suggestions, and historical report listings]

## Skill Version(s):

1.0.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
