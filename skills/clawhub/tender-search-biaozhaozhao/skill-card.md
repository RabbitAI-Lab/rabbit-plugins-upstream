## Description:

招投标快捷检索引擎-标找找 helps agents quickly search tender and bid-award notices by keyword and return concise lists with project names, amounts, and links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search Chinese tender, bid-award, company, account, and market intelligence APIs, then summarize relevant opportunities, companies, competitors, prices, contacts, and account status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback registration path fingerprints the device and saves an API key locally.

Mitigation: Prefer a user-supplied ZLBX_API_KEY; when auto-registration is needed, require explicit user consent before collecting platform, CPU architecture, and MAC hash.

Risk: The skill can retrieve business contacts and broader company or market intelligence.

Mitigation: Review outputs before sharing, preserve masked contact data as returned, and avoid bulk contact export or attempts to enrich masked phone numbers.

Risk: The skill may append referral or promotional links.

Mitigation: Keep responses focused on the requested data and include promotional links only when they are necessary for account setup, quota recovery, or a directly relevant next step.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/tender-search-biaozhaozhao)
- [Biaozhaozhao API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Biaozhaozhao account and registration portal](https://ai.zhiliaobiaoxun.com/?ch=s25)
- [Tender search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown prose, tables, JSON request examples, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read or store an API key through ZLBX_API_KEY or ~/.zlbx/config.json when the user consents to the documented setup flow.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
