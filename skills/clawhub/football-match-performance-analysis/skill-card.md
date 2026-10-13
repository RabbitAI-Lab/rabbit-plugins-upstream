## Description:

Produces source-grounded football match briefs using SofaScore event statistics, incidents, lineups, and match context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Sports analysts, writers, and fans use this skill to prepare a concise, source-grounded report on a football match, distinguishing recorded events and statistics from interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Match lookup parameters are sent to Crawlora and access requires a Crawlora API key.

Mitigation: Provide the API key only when comfortable using Crawlora, and keep private or unrelated information out of match search queries.

Risk: Match statistics and incident timelines may be incomplete or mistaken for proof of causation.

Mitigation: Check event identity and status, distinguish observed data from interpretation, and state missing or ambiguous fields.

## Reference(s):

- [SofaScore endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/football-match-performance-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown report with a statistics table and incident timeline]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies the match, source-labeled statistics, relevant lineup facts, and missing or ambiguous evidence.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
