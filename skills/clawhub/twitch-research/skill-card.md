## Description:

Pulls structured Twitch data -- channel profile and live status, clips, VODs, VOD chat replay, broadcast schedule, team rosters, top games, and search -- via the Crawlora API as clean JSON, with no scraping or Twitch API OAuth setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to look up public Twitch channel, category, team, clip, VOD, schedule, and chat replay data through Crawlora and return concise Twitch research results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call arbitrary Crawlora paths, methods, JSON bodies, and an overridden API base.

Mitigation: Restrict use to the documented /twitch GET endpoints unless a reviewer explicitly approves broader Crawlora API access.

Risk: Twitch channel names, searches, VOD IDs, helper arguments, and the Crawlora API key are sent to Crawlora during use.

Mitigation: Use a scoped operational environment, keep CRAWLORA_API_KEY out of prompts and files, and avoid passing secrets or unrelated private data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/twitch-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY and returns public Twitch data from Crawlora endpoints.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
