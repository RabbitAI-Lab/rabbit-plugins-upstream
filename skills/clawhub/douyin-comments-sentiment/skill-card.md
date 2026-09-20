## Description:

抖音评论分析 helps agents retrieve public Douyin search, hot list, creator post, and comment data, then summarize sentiment, audience intent, public-opinion risk, and operations recommendations for creators, brands, and ecommerce teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External creators, operations teams, brand analysts, ecommerce teams, and developers use this skill to fetch public Douyin content, comments, hot topics, and creator posts for trend research, competitor monitoring, comment insight, and report preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin queries, links, and request context are sent to the third-party guaikei.com API.

Mitigation: Use the skill only when third-party API processing is acceptable for the data being queried, and avoid submitting private or sensitive links.

Risk: Successful search, post, and comment results are saved locally in the skill's logs directory without opt-in or retention controls.

Mitigation: Run the skill in a controlled workspace, treat saved logs as sensitive business and social-data artifacts, and delete or rotate logs when they are no longer needed.

Risk: Public Douyin results can include user nicknames, comments, engagement metrics, and competitive business signals.

Mitigation: Limit redistribution of exported data, redact or de-identify personal fields before sharing, and confirm authorization before public or commercial reuse.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/why20261/skills/douyin-comments-sentiment)
- [Server-resolved source repository](https://github.com/why20261/douyin-comments-sentiment)
- [GuaiKei Douyin data API](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Hot list response schema](assets/hot_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON data, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Node.js shell commands; CLI tools return structured JSON on stdout.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; successful search, post, and comment datasets are saved to local logs.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
