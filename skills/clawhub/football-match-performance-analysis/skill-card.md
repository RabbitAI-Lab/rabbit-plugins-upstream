## Description:

Produces a source-grounded football match brief from SofaScore event statistics, incidents, lineups, and match context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Fans, analysts, and writers use this skill to prepare a concise post-match report that distinguishes recorded match statistics and incidents from interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Match searches and event IDs, along with the Crawlora API key, are sent to a third-party API.

Mitigation: Use only when sharing those queries with Crawlora is acceptable; keep the API key confidential.

Risk: Aggregate match statistics and incomplete event data can support misleading causal or tactical conclusions.

Mitigation: Verify match identity and status, label periods and missing values, and separate observations from interpretations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/football-match-performance-analysis)
- [SofaScore endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown match brief with a statistics table and incident timeline]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies the match and status, preserves source labels and periods, and flags missing or ambiguous data.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
