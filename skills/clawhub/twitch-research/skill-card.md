## Description:

Pulls structured Twitch data - channel profile and live status, clips, VODs, VOD chat replay, broadcast schedule, team rosters, top games, and search - via the Crawlora API as clean JSON, with no scraping or Twitch API OAuth setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to research public Twitch channels, games, teams, schedules, clips, VODs, and VOD chat replay through Crawlora API calls without setting up Twitch OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send a Crawlora API key to arbitrary API paths and to an environment-selected API host outside the stated Twitch scope.

Mitigation: Keep CRAWLORA_API_BASE unset or set only to a trusted host, and use a Twitch-only wrapper or endpoint allowlist when strict scope control is required.

Risk: The skill depends on a Crawlora API key for outbound requests.

Mitigation: Use a key with acceptable limits, rotate it when needed, and never hardcode, commit, or pass it through query parameters.

## Reference(s):

- [twitch-research endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/twitch-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API responses are public Twitch data returned as JSON.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
