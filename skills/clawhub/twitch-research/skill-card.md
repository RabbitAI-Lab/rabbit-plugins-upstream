## Description:

Pulls structured Twitch data -- channel profile and live status, clips, VODs, VOD chat replay, broadcast schedule, team rosters, top games, and search -- via the Crawlora API as clean JSON, with no scraping or Twitch API OAuth setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to retrieve public Twitch channel, stream, clip, VOD, chat replay, schedule, team, search, and category data through Crawlora API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twitch query inputs and the Crawlora API key are sent to Crawlora.

Mitigation: Use only public Twitch identifiers, avoid sending private workspace content as API parameters or request bodies, and protect CRAWLORA_API_KEY like any other API credential.

Risk: CRAWLORA_API_BASE can redirect requests to an alternate endpoint.

Mitigation: Keep CRAWLORA_API_BASE unset unless the alternate endpoint is intentionally trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/twitch-research)
- [Crawlora](https://crawlora.net)
- [Endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public Twitch identifiers and requires a Crawlora API key in CRAWLORA_API_KEY.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
