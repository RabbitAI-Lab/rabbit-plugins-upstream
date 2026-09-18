## Description:

Queries public Douyin video, author, comment, and hot-list data through Guaikei-backed Node.js command tools for social listening, competitor tracking, and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to collect public Douyin search results, trending topics, creator posts, and video comments, then feed the structured data into short-video research, competitive analysis, public-opinion monitoring, and marketing reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin queries, Douyin links, and the configured Guaikei API token to a third-party service.

Mitigation: Install only when that data flow is acceptable, keep the token private, and rotate the token if exposure is suspected.

Risk: The skill may save collected Douyin results and logs locally, which can include public usernames, comments, links, and research context.

Mitigation: Treat generated logs as sensitive research records, keep the skill directory private, and delete logs when they are no longer needed.

Risk: The security evidence marks the release as suspicious because token handling and saved result files require user review before installation.

Mitigation: Review the security summary and guidance before deployment and confirm that the intended use complies with applicable platform and data-use requirements.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/why20261/douyin-crawler-guaikei)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-crawler-guaikei)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance, analysis]

**Output Format:** [Structured JSON from Node.js CLI tools, with concise Markdown summaries when the agent explains results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; command output is JSON on stdout, logs are written to stderr, and result files may be saved locally.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
