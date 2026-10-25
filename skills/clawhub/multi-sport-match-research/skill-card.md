## Description:

Compare public fixtures, live scores, match statistics, standings, and head-to-head records using Crawlora Flashscore and LiveScore tools for sourced multi-sport match previews, recaps, and scoreboard reconciliation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Sports researchers, fans, and analysts use this skill to check public multi-sport fixtures and scores, assemble sourced match previews or recaps, and explain discrepancies between Flashscore and LiveScore.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and the Crawlora API key are sent to Crawlora; requests may consume credits.

Mitigation: Keep the API key private, exclude unrelated personal information from queries, and limit requests to the sports data and credit budget needed.

Risk: Live score snapshots may be incomplete or disagree across providers.

Mitigation: Preserve source links and observation times, identify unresolved conflicts, and do not treat missing results as a confirmed score or cancellation.

## Reference(s):

- [Flashscore and LiveScore endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/multi-sport-match-research)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Sourced Markdown match report or score summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes event identity, match status and observation time, source URLs, unresolved provider discrepancies, and coverage limits.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
