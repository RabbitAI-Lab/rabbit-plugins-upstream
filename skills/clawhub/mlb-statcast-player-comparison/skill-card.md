## Description:

Compares MLB players using Crawlora Statcast leaderboards and player statistics while accounting for season, role, qualification, metric units, and sample size.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, developers, and baseball researchers use this skill to compare observed player performance, pitch arsenals, or role-specific shortlists with qualification and sample context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends MLB queries to an external service using a Crawlora API key.

Mitigation: Store the key securely, avoid logging it, and send only MLB-related identifiers and query parameters rather than unrelated confidential data.

Risk: Different board qualifications and small samples can make player comparisons misleading.

Mitigation: State the board, role, season, thresholds, event counts, units, and any missing-player or sample limitations alongside comparisons.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/mlb-statcast-player-comparison)
- [Crawlora MLB endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown tables and explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports identity and scope, metric definitions, qualification, sample counts, source context, and uncertainties.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
