## Description:

Compare public fixtures, live scores, match statistics, standings, and head-to-head records using Crawlora Flashscore and LiveScore tools for sourced score checks, previews, recaps, and provider reconciliation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Sports fans, analysts, and other users can check public match scores and fixtures, prepare sourced previews or recaps, and compare Flashscore and LiveScore observations across sports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sports lookup parameters and the required API key are sent to Crawlora.

Mitigation: Use a Crawlora key only if comfortable with that disclosure; avoid private or sensitive non-sports data.

Risk: Broad or repeated score requests may exceed the intended credit budget.

Mitigation: Limit requests and polling to the matches, competitions, intervals, and budget requested.

Risk: Asynchronous provider snapshots can disagree or be mistaken for final results.

Mitigation: Keep source, match status, and observation time for each result; state unresolved discrepancies rather than selecting a winner.

## Reference(s):

- [Crawlora skill release](https://clawhub.ai/crawlora-org/skills/multi-sport-match-research)
- [Flashscore and LiveScore endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown with sourced match observations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes match identity, status and observation time, scores or preview evidence, source attribution, and unresolved discrepancies.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
