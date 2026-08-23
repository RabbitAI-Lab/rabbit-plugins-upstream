## Description:

This skill helps agents query public Douyin data for keyword search, creator posts, video comments, and live trending topics for market research and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams use this skill to collect public Douyin search results, creator post metadata, video comments, and hot-list entries for marketing research, competitor monitoring, content planning, sentiment review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad research prompts may trigger the skill when the user did not intend to query Douyin public data.

Mitigation: Confirm that the task should use Douyin public data before running commands, especially for broad market or content research prompts.

Risk: Queries and parameters are sent to guaikei.com to retrieve public Douyin data.

Mitigation: Use the skill only for intended Douyin public-data requests and avoid submitting sensitive research terms or private account information.

Risk: The skill saves full JSON result logs that can contain research terms, target accounts, comments, and returned public-content metadata.

Mitigation: Protect the logs directory with appropriate access controls and periodically delete logs that are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-public-data-for-market-analysis)
- [Skill README](artifact/readme.md)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [Search response schema](artifact/assets/search_cli_resp.schema.json)
- [Post response schema](artifact/assets/post_cli_resp.schema.json)
- [Comment response schema](artifact/assets/comment_cli_resp.schema.json)
- [Hot-list response schema](artifact/assets/hot_cli_resp.schema.json)
- [Guaikei service page](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown guidance with shell commands; runtime command output is JSON and saved JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a GUAIKEI_API_TOKEN environment variable and writes timestamped query result logs under the skill logs directory.]

## Skill Version(s):

1.0.0 (source: evidence release, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
