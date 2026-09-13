## Description:

乙方投标助手，面向投标方（乙方）的全网招中标数据分析助手。当用户涉及以下场景时必须使用此SKILL：查询招标/中标公告、分析竞争对手中标情况、寻找潜在合作与供应商、评估某类项目的中标价格区间、乙方视角的投标决策支持。作为投标方的日常查标工具，必须以清晰的表格或图表输出结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and bidding teams use this skill to search tender and award notices, analyze competitors, identify potential suppliers or partners, estimate award price ranges, and support bid decisions from a supplier perspective.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts Zhiliaobiaoxun services and uses an API key for bid-data access.

Mitigation: Provide your own ZLBX_API_KEY when possible and avoid sharing the API key in chat or generated reports.

Risk: Automatic trial registration can send a stable MAC-derived device hash for trial deduplication.

Mitigation: Use automatic registration only after explicit consent, or configure an API key manually to skip the registration flow.

Risk: The skill may save an API key in a local plaintext config file.

Mitigation: Review and restrict permissions on ~/.zlbx/config.json, and rotate the key if the file may have been exposed.

Risk: Normal answers may include vendor referral or promotional links.

Mitigation: Review generated answers before sharing them externally, especially when neutral reporting is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/bidding-yifangbao)
- [API search reference](references/api-search.md)
- [API company reference](references/api-company.md)
- [API market reference](references/api-market.md)
- [API account reference](references/api-account.md)
- [Auto-register reference](references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun account and registration](https://ai.zhiliaobiaoxun.com/?ch=s24)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with tables, concise summaries, API request guidance, and occasional configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a local ~/.zlbx/config.json API key; some contact fields may be masked depending on account status.]

## Skill Version(s):

2.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
