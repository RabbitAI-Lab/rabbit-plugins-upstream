## Description:

Fetches public Douyin data for keyword search, creator post collection, video comment analysis, and real-time trending queries for content research, competitive analysis, comment insight, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and content research teams use this skill to query public Douyin videos, creators, comments, and trending topics through Node.js CLI commands that return structured JSON for analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential handling is review-worthy because the API token is sent to the provider in URL query parameters and invalid-token paths can display promotional contact or website text.

Mitigation: Review before installation, use only a scoped GUAIKEI_API_TOKEN through the environment, avoid sharing command traces, and stop on authentication errors until token handling is confirmed.

Risk: Collected comments, account data, and automatically written JSON logs may contain personal data from public Douyin content.

Mitigation: Use only for clearly Douyin-related public-data tasks, avoid sensitive search terms, restrict exports to internal analysis, and redact or delete logs before sharing.

Risk: Some output schemas include playback or download-capable URL fields even though the skill scope excludes downloading or redistributing videos.

Mitigation: Use returned media URLs only for permitted analysis or verification, and do not automate downloads, redistribution, or uses that violate platform terms or applicable law.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-public-data-fetcher)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [Search request schema](artifact/assets/search_cli_req.schema.json)
- [Search response schema](artifact/assets/search_cli_resp.schema.json)
- [Post request schema](artifact/assets/post_cli_req.schema.json)
- [Post response schema](artifact/assets/post_cli_resp.schema.json)
- [Comment request schema](artifact/assets/comment_cli_req.schema.json)
- [Comment response schema](artifact/assets/comment_cli_resp.schema.json)
- [Hot list response schema](artifact/assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with Node.js CLI commands; command stdout is JSON and successful collection tasks may also write JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14 or later and GUAIKEI_API_TOKEN; individual collection commands support limits up to 10000 public Douyin records.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
