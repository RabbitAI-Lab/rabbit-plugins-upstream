## Description:

Retrieves public Douyin data for keyword search, creator posts, video comments, and trending topics through command-line tools that return JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect public Douyin search results, creator posts, comments, and hot-list data for content research, competitive analysis, public opinion analysis, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin queries, URLs, and requested public result data are sent to Guaikei's API.

Mitigation: Use the skill only for intended public-data tasks and confirm ambiguous requests before invoking it.

Risk: Automatic JSON logs may retain sensitive research queries or result data locally.

Mitigation: Avoid shared machines or synced folders for sensitive searches and periodically delete logs that are no longer needed.

Risk: The required GUAIKEI_API_TOKEN and token-error behavior need review before installation.

Mitigation: Store GUAIKEI_API_TOKEN as a secret, do not print or persist it, and review authentication-error output before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-data-feed)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [Guaikei service site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [shell commands, JSON, configuration, guidance]

**Output Format:** [JSON results on stdout, diagnostic logs on stderr, and optional saved JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >=16.14 and GUAIKEI_API_TOKEN; supports search, creator-post, comment, and hot-list commands.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
