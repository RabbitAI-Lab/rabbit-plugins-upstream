## Description:

Use when a user wants an AI agent to call Heyi's Xiaohongshu, Douyin, Kuaishou, or Bilibili HTTP APIs with a Bearer API Key, including endpoint discovery, point billing, balance checks, pagination, batching, error handling, retries, or usage reconciliation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heyi-byte](https://clawhub.ai/user/heyi-byte)

### License/Terms of Use:

MIT

## Use Case:

External developers and API consumers use this skill to let an agent discover and call Heyi's paid social-media data APIs, confirm billable requests, handle pagination and retries, and reconcile point usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger paid external API calls through Heyi endpoints.

Mitigation: Keep HEYI_API_KEY in a credential store or environment variable, summarize endpoint, parameters, request count, and maximum point cost, and require explicit confirmation before billable calls.

Risk: Broad social-media data requests may be routed to Heyi's paid external APIs unintentionally.

Mitigation: Verify that the user's request is meant to use Heyi before making calls, and use endpoint discovery before selecting an API.

Risk: The artifact includes maintainer publishing automation that can use marketplace or npm credentials.

Mitigation: Do not run bin/publish-all.sh unless acting as the maintainer and prepared to use publishing credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heyi-byte/skills/heyihub-skill)
- [Source repository](https://github.com/heyi-byte/heyihub-skill)
- [Source SKILL.md](https://github.com/heyi-byte/heyihub-skill/blob/main/SKILL.md)
- [Skill docs path](https://github.com/heyi-byte/heyihub-skill/tree/main/docs/skills/heyi-paid-api)
- [Heyi API homepage](https://api.01011.top)
- [Heyi API console](https://bot.01011.top)
- [API Key guide](https://my.feishu.cn/wiki/SzpMwQQ1Piw3rck0NAPc7la1npe)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Text]

**Output Format:** [Markdown guidance with shell commands, code snippets, and JSON API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires HEYI_API_KEY and explicit user confirmation before billable API calls.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
