## Description:

Builds sourced Flashscore match reports using covered player statistics, lineups, absences, momentum, sport-specific scoring, and editorial coverage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Sports analysts and other users seeking detailed event analysis use this skill to assemble source-linked match reports from available Flashscore statistics and editorial coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Match search terms, IDs, and query parameters are sent to Crawlora using an API key.

Mitigation: Use only if comfortable sharing these queries with Crawlora; protect the API key and avoid including sensitive information in searches.

Risk: Missing data or predicted lineups may be mistaken for confirmed match facts.

Mitigation: Report unavailable coverage explicitly and distinguish predictions and editorial claims from observed statistics.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/flashscore-match-analysis)
- [Flashscore endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Sourced match report in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes event identity and status, selected observations, source links and timestamps, and coverage limitations.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
