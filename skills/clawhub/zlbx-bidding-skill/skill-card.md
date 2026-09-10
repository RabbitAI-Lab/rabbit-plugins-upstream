## Description:

Helps agents query and analyze Zhiliaobiaoxun bidding, procurement, supplier, competitor, market, and account data through the provider's APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users, business development teams, procurement teams, and bidding teams use this skill to search tender and award notices, analyze companies and competitors, find expiring or proposed opportunities, and summarize market trends from Zhiliaobiaoxun data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider APIs receive bidding, company, competitor, and market-analysis queries.

Mitigation: Install only when those queries can be shared with the provider, and avoid sending sensitive internal procurement strategy unless approved.

Risk: The opt-in auto-registration flow sends a stable hashed MAC-derived device identifier.

Mitigation: Prefer configuring ZLBX_API_KEY manually; if auto-registration is used, obtain user consent before collection and send only the documented minimal fields.

Risk: Auto-registration may save an API key under ~/.zlbx/config.json.

Mitigation: Restrict permissions on the local config file and never display or ask the user to paste the API key in chat.

Risk: Contact-related endpoints may return masked or full phone numbers depending on account status.

Mitigation: Show contact data only as returned, do not attempt to unmask phone numbers, and do not bulk export contacts.

Risk: Follow-up recommendations may point to affiliated Zhiliaobiaoxun services.

Mitigation: Treat those links as provider-operated commercial services and keep recommendations brief and clearly optional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/zlbx-bidding-skill)
- [Bidding search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration flow](references/auto-register.md)
- [Zhiliaobiaoxun API base URL](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun API key and account portal](https://ai.zhiliaobiaoxun.com/?ch=s20)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with JSON REST request bodies, result tables, concise analysis, and occasional shell command or configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or an opt-in provider registration flow before protected API calls.]

## Skill Version(s):

1.4.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
