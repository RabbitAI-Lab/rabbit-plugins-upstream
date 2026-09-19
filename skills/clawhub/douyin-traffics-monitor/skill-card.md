## Description:

Retrieves public Douyin keyword search results, creator posts, video or image comments, and hot-list entries as structured JSON for content research, competitor monitoring, public-sentiment analysis, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, creators, marketers, operators, and analysts use this skill to inspect public Douyin traffic signals, including popular keyword results, creator output, comments, and real-time hot topics. It supports internal content planning, competitive analysis, marketing research, and trend monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided Douyin keywords or links are sent to the third-party guaikei.com API.

Mitigation: Use only approved monitoring targets, avoid sensitive keywords or links, and confirm that data sharing with the API provider is permitted for the intended workflow.

Risk: Successful search, creator-post, and comment results may be retained in the skill's local logs directory.

Mitigation: Review local log contents after use, protect log storage, and delete retained results according to the user's data-retention requirements.

Risk: The skill works with public Douyin data that may still include personal or sensitive user-generated content.

Mitigation: Limit redistribution of retrieved data and confirm use complies with Douyin terms, privacy rules, and applicable organizational policies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-traffics-monitor)
- [Server-resolved source repository](https://github.com/why20261/douyin-traffics-monitor)
- [Guaikei API access and support](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)
- [Hot list response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Structured JSON results with concise Markdown or text guidance from the agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; commands send Douyin keywords or links to guaikei.com and may save successful search, post, and comment results under a local logs directory.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter and package.json report 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
