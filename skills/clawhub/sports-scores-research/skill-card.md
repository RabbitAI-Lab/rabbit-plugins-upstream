## Description:

Retrieves live sports scores, standings, statistics, betting odds, routes, and sports news through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Fans, analysts, and developers use this skill to research games, teams, players, betting odds, and endurance-sport routes using public sports data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sports queries, identifiers, and the API key are sent to Crawlora's external service.

Mitigation: Share only necessary identifiers and use an environment-provided API key rather than placing it in prompts or files.

Risk: The endpoint catalog includes Cricinfo and Sportskeeda editorial and news routes beyond the short sports-data description.

Mitigation: Review endpoint selection and distinguish editorial reports from official scores or roster announcements.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/sports-scores-research)
- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora documentation](https://crawlora.net/docs)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Markdown responses or JSON returned by API requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live data reflects source update cadence; a Crawlora API key is required.]

## Skill Version(s):

1.0.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
