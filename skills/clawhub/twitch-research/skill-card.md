## Description:

Pulls structured Twitch channel, clip, VOD, VOD chat replay, schedule, team, top-game, stream, and search data through the Crawlora API as JSON without Twitch API OAuth setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, analysts, and content teams use this skill to look up public Twitch channel status, clips, VODs, chat replay, schedules, teams, categories, live streams, and search results as structured JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twitch query parameters and the Crawlora API key are sent to Crawlora when the helper runs.

Mitigation: Use the skill only when sending those requests to Crawlora is acceptable, keep the key in CRAWLORA_API_KEY, and do not hardcode or commit the key.

Risk: Use of public Twitch data may still be subject to Crawlora and Twitch terms.

Mitigation: Review the relevant service terms for the intended use case before deployment.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/twitch-research)
- [Publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and is limited to documented GET routes for public Twitch data.]

## Skill Version(s):

1.0.15 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
