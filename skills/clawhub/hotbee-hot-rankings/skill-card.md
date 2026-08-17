## Description:

Helps an agent retrieve HotBee all-web hot rankings and platform hot-search data for Xiaohongshu, Douyin, Baidu, Weibo, and Bilibili without inventing unsupported endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shanye1402-hash](https://clawhub.ai/user/shanye1402-hash)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to choose confirmed HotBee hot-ranking endpoints from Chinese platform requests, run dry-run checks, and summarize live ranking results after API-key and quota approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live HotBee requests may spend API quota.

Mitigation: Start with the dry-run flow and require explicit approval before making paid live calls.

Risk: The HotBee API key could be exposed if echoed, logged, or persisted.

Mitigation: Read HOTBEE_API_KEY only from the local environment and do not print or store it.

Risk: Unsupported platform requests could lead to incorrect or fabricated endpoint use.

Mitigation: Use only confirmed endpoints and ask for the official OpenAPI contract when a requested platform is not confirmed.

## Reference(s):

- [Hot Rankings API](references/api.md)
- [HotBee Skills](https://www.hotbee.cn/skills)
- [HotBee API Base](https://www.smsz.xyz/prod-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run command suggestions and returned HotBee ranking fields when live API calls are approved.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
