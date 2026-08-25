## Description:

This skill helps agents search Douyin keywords, fetch creator post lists and video comments, and retrieve hot rankings as structured JSON for content research and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and content teams use this skill to collect public Douyin search results, creator posts, comments, and hot rankings for content research, competitor analysis, sentiment review, and trend monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin keywords, profile or video URLs, requested limits, and GUAIKEI_API_TOKEN to www.guaikei.com.

Mitigation: Install only when that data sharing is acceptable, keep the token in an environment variable, and rotate it if exposure is suspected.

Risk: Saved logs and comment exports can contain user identifiers or sensitive research data.

Mitigation: Treat generated logs as sensitive, restrict access to them, and delete exports when they are no longer needed.

Risk: Returned media URLs or public Douyin data could be reused outside the permissions of the platform or rightsholders.

Mitigation: Use collected data only for permitted analysis and do not download, redistribute, or republish media unless rights and platform permission are confirmed.

Risk: The server security verdict is suspicious because token handling and scraped Douyin data require user review before installation.

Mitigation: Review the security guidance and intended data flows before deployment, especially in commercial or customer-data environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-bulk-videos-fetch)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Repository metadata link](https://github.com/um-why/douyin-search-openclaw)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [Request and response schemas](artifact/assets/)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI output is pure JSON on stdout, logs and prompts go to stderr, and task logs may be saved under logs/.]

## Skill Version(s):

1.0.0 (source: server release evidence, artifact metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
