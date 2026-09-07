## Description:

Use when a user wants an AI agent to call Heyi's Xiaohongshu, Douyin, Kuaishou, or Bilibili HTTP APIs with a Bearer API Key, including endpoint discovery, point billing, balance checks, pagination, batching, error handling, retries, or usage reconciliation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heyi-byte](https://clawhub.ai/user/heyi-byte)

### License/Terms of Use:

MIT

## Use Case:

External developers and agent users use this skill to discover and call Heyi's paid social-media data APIs for Xiaohongshu, Douyin, Kuaishou, and Bilibili. It helps agents prepare authorized HTTP requests, explain expected point costs, interpret API responses, and reconcile usage against service-side point records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized calls may consume paid Heyi API points.

Mitigation: Check endpoint pricing and balance first, describe the expected request count and maximum point cost, and require explicit user confirmation before billable calls.

Risk: Search terms, IDs, and request bodies approved by the user are sent to Heyi-controlled servers.

Mitigation: Disclose the external service boundary and send only user-approved request data needed for the selected endpoint.

Risk: API keys could be exposed if pasted into chat, URLs, logs, screenshots, or generated code.

Mitigation: Use a credential store or HEYI_API_KEY, keep the key out of request URLs and response text, and avoid logging Authorization headers.

Risk: The installer can copy the skill into multiple detected local agent directories.

Mitigation: Use dry-run or explicit agent selection when users want to inspect or limit install targets before writing files.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/heyi-byte/skills/heyi-paid-api)
- [Heyi API homepage](https://api.01011.top)
- [API key guide](https://my.feishu.cn/wiki/SzpMwQQ1Piw3rck0NAPc7la1npe)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with HTTP request examples, JSON response summaries, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include raw or summarized API JSON data, billing estimates, and call-record references after user-authorized requests.]

## Skill Version(s):

1.2.0 (source: SKILL.md frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
