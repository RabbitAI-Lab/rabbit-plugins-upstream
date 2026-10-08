## Description:

Retrieves sports scores, standings, rosters, player and team statistics, public sports media, and betting odds through the Crawlora API, with optional public Strava route and club lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Sports researchers, developers, and other users can look up public game scores, statistics, rosters, sports news, and odds, or research public routes and clubs when relevant to a request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives the API key and sports research queries.

Mitigation: Use the skill only when comfortable sharing these with Crawlora; avoid confidential research targets and keep the key out of source files and URLs.

Risk: Public Strava routes or clubs may reveal location-sensitive patterns.

Mitigation: Limit lookups to the user's relevant request and do not infer a person's home, routine, or sensitive location history.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/sports-scores-research)
- [Crawlora API documentation](https://crawlora.net/docs)
- [Bundled endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands]

**Output Format:** [Plain text or Markdown summaries; optional JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live information depends on upstream update cadence; API requests require a Crawlora key.]

## Skill Version(s):

1.0.21 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
