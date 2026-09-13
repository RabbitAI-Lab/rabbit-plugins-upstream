## Description:

Pulls structured Twitch channel, clip, VOD, chat replay, schedule, team, top-game, stream, and search data through the Crawlora API as clean JSON without Twitch OAuth setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to research public Twitch channels, categories, teams, VODs, clips, schedules, live streams, and chat replay through Crawlora API calls without setting up Twitch OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twitch lookup parameters and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when sharing public Twitch lookup parameters with Crawlora is acceptable, keep CRAWLORA_API_KEY in the environment, and avoid unrelated sensitive data in queries or request bodies.

Risk: Requests can expose unrelated sensitive data if users place it in query parameters or request bodies.

Mitigation: Limit requests to public Twitch data as documented and do not include sensitive unrelated data in queries or request bodies.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/twitch-research)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; helper use is bounded to documented Twitch routes.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
