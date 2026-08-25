## Description:

Fetches public Douyin search results, creator posts, comments, and trending-list data through Guaikei-backed Node.js CLI commands for content research, competitor analysis, sentiment review, and topic tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect public Douyin data for short-video topic research, competitor monitoring, comment analysis, public-opinion review, and trending-topic tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ambiguous short-video research prompts may trigger Douyin collection even when the user did not explicitly name Douyin.

Mitigation: Confirm the user wants Douyin data collection before running commands for ambiguous short-video, competitor, or public-opinion research tasks.

Risk: Fetched public profile and comment datasets may be saved locally under the skill's logs directory.

Mitigation: Protect generated logs as research data and periodically delete them when they are no longer needed.

Risk: Queries, target URLs, limits, and the GUAIKEI_API_TOKEN are sent to the Guaikei provider.

Mitigation: Use the skill only when this provider data flow is acceptable, keep the token in an environment variable, and rotate it if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/douyin-quick-fetch-public-guaikei)
- [Guaikei service site](https://www.guaikei.com)
- [Complete CLI options](references/options.md)
- [Changelog](references/changelog.md)
- [Search CLI request schema](assets/search_cli_req.schema.json)
- [Search CLI response schema](assets/search_cli_resp.schema.json)
- [Post CLI request schema](assets/post_cli_req.schema.json)
- [Post CLI response schema](assets/post_cli_resp.schema.json)
- [Comment CLI request schema](assets/comment_cli_req.schema.json)
- [Comment CLI response schema](assets/comment_cli_resp.schema.json)
- [Hot list response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [shell commands, JSON, files, configuration, guidance]

**Output Format:** [JSON on stdout plus timestamped JSON log files, with stderr logs and Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >= 16.14 and GUAIKEI_API_TOKEN; single fetch commands support limits up to 10000 records.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
