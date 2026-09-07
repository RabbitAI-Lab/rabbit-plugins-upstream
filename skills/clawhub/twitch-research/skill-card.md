## Description:

Pulls structured Twitch data, including channel profile and live status, clips, VODs, VOD chat replay, broadcast schedules, team rosters, top games, and search results, via the Crawlora API as clean JSON without scraping or Twitch API OAuth setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and external agents use this skill to resolve public Twitch channels, games, and teams, then retrieve live status, clips, VODs, chat replay, schedules, and discovery results as normalized JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the Crawlora API key to an overridden API base URL.

Mitigation: Run it only in a trusted shell, keep the default Crawlora API base unless the destination is fully trusted, and prefer a release that pins or validates the API host.

Risk: The skill retrieves public Twitch data through a third-party API service.

Mitigation: Use the documented read-only Twitch endpoints and review Twitch and Crawlora terms before using the output in production workflows.

## Reference(s):

- [Twitch Research Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/twitch-research)
- [ClawHub Publisher Profile](https://clawhub.ai/user/tonywangcn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled helper prints raw JSON responses from the Crawlora API for downstream inspection or jq processing.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
