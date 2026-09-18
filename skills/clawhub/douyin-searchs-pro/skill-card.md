## Description:

抖音作品搜索 helps agents query public Douyin content by keyword, hot ranking, creator profile, or post/comment link and return structured results for content discovery and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and content operations teams use this skill to retrieve public Douyin search results, trending topics, creator works, and comment data for internal research, comparison, reporting, and downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords, URLs, IDs, and retrieved public content are sent to guaikei.com with the user's GUAIKEI_API_TOKEN.

Mitigation: Use only approved tokens and queries, treat GUAIKEI_API_TOKEN as a secret, and confirm that sending requested data to the third-party API is permitted.

Risk: Search, post, and comment results are saved as local JSON logs and may contain public nicknames, comments, links, and engagement data.

Mitigation: Review log retention before use, avoid sharing raw logs externally, and redact or delete retained results when they are no longer needed.

Risk: The skill is limited to public Douyin data and does not support private, hidden, login-state, or write actions.

Mitigation: Route only public read-only Douyin requests to this skill and stop or ask for clarification when a request implies private data access or platform actions.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/why20261/skills/douyin-searchs-pro)
- [Server-resolved GitHub provenance](https://github.com/why20261/douyin-searchs-pro)
- [GUAIKEI API token and support](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Hot ranking response schema](assets/hot_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command outputs are structured JSON; logs are written locally under the skill logs directory.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
