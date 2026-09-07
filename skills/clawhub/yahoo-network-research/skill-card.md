## Description:

Researches Yahoo editorial content and sports data through the Crawlora API, returning normalized JSON for story feeds, full articles, comments, shopping deals, scoreboards, standings, schedules, teams, and players.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to retrieve public Yahoo editorial feeds, article content, comments, shopping deals, and Yahoo Sports data through the Crawlora API for research and reporting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included helper can make authenticated Crawlora requests beyond the Yahoo endpoints described by the skill.

Mitigation: Constrain use of the helper to documented /yahoo-* paths and review requested paths before running commands with a real API key.

Risk: The helper allows CRAWLORA_API_BASE to override the official Crawlora API base.

Mitigation: Use the default https://api.crawlora.net/api/v1 base unless an approved environment explicitly requires another base.

Risk: The skill requires an API key for Crawlora requests.

Mitigation: Store the key only in CRAWLORA_API_KEY and avoid placing it in prompts, command arguments, URLs, logs, or committed files.

## Reference(s):

- [Yahoo Network Research Endpoint Reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; helper calls return raw JSON for the requested Yahoo endpoint.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
