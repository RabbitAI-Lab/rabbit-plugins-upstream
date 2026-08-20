## Description:

This skill helps operators collect public Douyin search, creator post, comment, and hot-list data for content planning, competitor research, sentiment review, and trend monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External operators and content teams use this skill to query public Douyin data, inspect competitor accounts, review video comments, and track current hot topics. It supports agent workflows that turn natural-language requests into Node.js CLI calls and structured JSON results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger on broad short-video research prompts.

Mitigation: Use it only for explicit Douyin search, account, comment, or hot-list tasks and confirm ambiguous intent before running commands.

Risk: Douyin requests and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Install only when that data flow is acceptable, scope the token to intended use, and rotate or revoke it if exposure is suspected.

Risk: Collected competitor, author, and comment data may be saved in local logs.

Mitigation: Protect the logs directory, avoid committing logs, and periodically delete retained data that is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-discovery)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Douyin search skill website](https://www.guaikei.com)
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

**Output Type(s):** [shell commands, configuration, JSON, guidance]

**Output Format:** [JSON from CLI stdout with logs on stderr; agent guidance may be Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >= 16.14 and GUAIKEI_API_TOKEN; each request can return up to 10,000 public Douyin records and may save local JSON logs.]

## Skill Version(s):

1.0.0 (source: package.json, release evidence, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
