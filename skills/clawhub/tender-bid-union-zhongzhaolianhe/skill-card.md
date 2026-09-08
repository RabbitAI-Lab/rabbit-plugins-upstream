## Description:

Helps agents query and analyze tender and bid data for market sizing, trend analysis, purchaser and supplier rankings, company intelligence, project timelines, competitor analysis, and historical price research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business analysts use this skill to search tender notices, evaluate buyers and suppliers, analyze bid markets, and retrieve company or project details through the Zhiliaobiaoxun service. It is suited for procurement research, sales opportunity discovery, competitive analysis, and tender-market reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or use a vendor account and store a ZLBX API key locally.

Mitigation: Prefer manually configuring your own key, restrict permissions on ~/.zlbx/config.json, and avoid sharing the key in chat or logs.

Risk: Automatic registration uses a persistent device fingerprint for trial-account deduplication.

Mitigation: Run automatic registration only after explicit consent, or skip it by configuring ZLBX_API_KEY before using the skill.

Risk: Auto-login and recharge links can act as bearer-style account access links.

Mitigation: Keep generated links private, do not paste them into shared chats, and regenerate only when needed.

Risk: Tender and company queries may return business contact data.

Mitigation: Treat contact data as sensitive, follow lawful-use obligations, and do not attempt to reconstruct masked contact details or export contacts in bulk.

Risk: The skill includes vendor account, recharge, and referral flows.

Mitigation: Review costs and service terms before using paid features or following promotional links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/tender-bid-union-zhongzhaolianhe)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [API account reference](references/api-account.md)
- [API company reference](references/api-company.md)
- [API market reference](references/api-market.md)
- [API search reference](references/api-search.md)
- [Automatic registration reference](references/auto-register.md)
- [Zhiliaobiaoxun API service](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun account portal](https://ai.zhiliaobiaoxun.com/?ch=s51)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with tables, concise summaries, links, JSON request examples, and optional shell commands for configuration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tender records, market aggregates, company facts, project contacts, account status summaries, and user-facing setup or retry guidance.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
