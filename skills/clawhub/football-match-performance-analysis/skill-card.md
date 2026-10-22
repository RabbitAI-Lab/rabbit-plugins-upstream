## Description:

Produces a source-grounded football match brief from SofaScore event statistics, incidents, lineups, and match context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Football fans, analysts, and writers use this skill to prepare a post-match statistical brief for one verified match, separating recorded facts from interpretations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Match queries and event IDs are sent to Crawlora/SofaScore.

Mitigation: Use the skill only if sharing those match details with the service is acceptable.

Risk: The user-provided API key could be exposed in logs or shared transcripts.

Mitigation: Keep CRAWLORA_API_KEY out of logs and shared transcripts.

Risk: Broad or repeated match collection may consume API credits.

Mitigation: Limit collection to one match by default and confirm before expanding the scope.

## Reference(s):

- [SofaScore endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/football-match-performance-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown report with a match summary, statistics table, and incident timeline]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates observations from interpretation and identifies missing or ambiguous data.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
