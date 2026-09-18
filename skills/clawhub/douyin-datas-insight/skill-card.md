## Description:

Douyin Data Insight is a read-only command skill for collecting public Douyin search results, creator posts, video or image-text comments, and real-time hot-list data as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, operators, marketers, analysts, and developers use this skill to research short-video topics, monitor competitor accounts, review public comments, and track Douyin trends from structured public-data outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided Douyin keywords, links, IDs, request parameters, and the GUAIKEI_API_TOKEN are sent to www.guaikei.com.

Mitigation: Use the skill only when that third-party data transfer is approved, avoid sensitive inputs, and keep the API token secret.

Risk: Search, post, and comment results are saved locally under the skill logs directory by default.

Mitigation: Treat logs as sensitive analysis artifacts, review local retention and permissions, and remove logs that are no longer needed.

Risk: Untrusted strings containing terminal control characters may be unsafe until logging sanitization is improved.

Mitigation: Avoid passing untrusted terminal-control input and review generated output or logs before sharing them.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/why20261/douyin-datas-insight)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-datas-insight)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search input schema](assets/search_cli_req.schema.json)
- [Search output schema](assets/search_cli_resp.schema.json)
- [Post input schema](assets/post_cli_req.schema.json)
- [Post output schema](assets/post_cli_resp.schema.json)
- [Comment input schema](assets/comment_cli_req.schema.json)
- [Comment output schema](assets/comment_cli_resp.schema.json)
- [Hot-list output schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results are emitted as JSON envelopes; search, post, and comment results may also be saved locally under the skill logs directory.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
