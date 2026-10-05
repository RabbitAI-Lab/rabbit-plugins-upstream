## Description:

Compare public fixtures, live scores, match statistics, standings, and head-to-head records using Crawlora Flashscore and LiveScore tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

People researching public sports matches use this skill to check scores and fixtures, prepare sourced previews or recaps, and reconcile observations from Flashscore and LiveScore.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sports lookup queries and a Crawlora API key are sent to Crawlora.

Mitigation: Confirm this data sharing is acceptable and keep the key scoped to Crawlora.

Risk: Repeated lookups can consume API credits.

Mitigation: Bound requests to the needed matches and monitor credit usage.

Risk: The bundled fallback executes a shell helper.

Mitigation: Use the fallback only where shell execution is acceptable.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown with attributed match observations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes match status, observation times, source references, unresolved discrepancies, and limitations.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
