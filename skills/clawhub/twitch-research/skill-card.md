## Description:

Pulls structured Twitch data - channel profile and live status, clips, VODs, VOD chat replay, broadcast schedule, team rosters, top games, and search - via the Crawlora API as clean JSON, with no scraping or Twitch API OAuth setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to look up public Twitch channel, category, team, clip, VOD, schedule, and VOD chat replay data through Crawlora. It is useful when an agent needs normalized Twitch research output without setting up Twitch API OAuth or scraping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twitch lookup requests and the Crawlora API key are sent to Crawlora.

Mitigation: Install only when that data sharing is acceptable, keep CRAWLORA_API_KEY out of code and commits, and use the provided helper.

Risk: Modifying the helper to call unrelated routes could expand the skill beyond its reviewed Twitch research behavior.

Mitigation: Keep requests limited to the documented Twitch route catalog.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/twitch-research)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and returns public Twitch lookup results through scoped Crawlora routes.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
