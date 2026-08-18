## Description:

Uses a Node.js CLI to search public Douyin content, fetch creator posts and comments, and retrieve real-time trending topics for research and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and content teams use this skill to collect public Douyin search results, creator posts, comments, and trending topics for content research, competitor analysis, reputation monitoring, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends search queries, Douyin URLs, and the GUAIKEI token to the provider.

Mitigation: Install only when this provider data flow is acceptable for the intended use, and avoid submitting sensitive or private information as query text or URLs.

Risk: Generated logs may retain fetched Douyin results on local or synced machines.

Mitigation: Review generated logs after use and delete or protect them according to the team's data retention requirements.

Risk: The security review reports that token-error paths may print provider contact or marketing text despite the skill's neutral-error claim.

Mitigation: Review authentication failure output before production use and avoid exposing runtime errors directly to end users.

Risk: The skill can trigger broadly for Douyin-related research intents.

Mitigation: Confirm user intent before running commands that fetch public platform data, especially for large result limits.

## Reference(s):

- [Skill documentation](readme.md)
- [Command options](references/options.md)
- [Changelog](references/changelog.md)
- [JSON Schemas](assets/*.schema.json)
- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-search-and-analyze)
- [Publisher profile](https://clawhub.ai/user/engheng-art)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI stdout is intended to be pure JSON; logs and banner output are separated from stdout and saved locally.]

## Skill Version(s):

1.0.0 (source: server release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
