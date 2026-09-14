## Description:

Queries and analyzes Jiangsu-focused tender, award, procurement, company, competitor, contact, account, and market data through the Zhiliaobiaoxun APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, sales, market intelligence, and bid teams use this skill to search tender and award notices, inspect company and contact data, track project timelines, and summarize procurement market trends. Jiangsu Province is the default search scope, while user-specified regions or industries can override or combine with that scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic registration can create a vendor account using a hashed MAC address plus basic system metadata and persist a reusable API key locally.

Mitigation: Prefer a manually supplied ZLBX_API_KEY. If automatic registration is used, require explicit user consent first and expect the key to be stored under ~/.zlbx/config.json.

Risk: Company contacts and procurement records may include sensitive business or contact data.

Mitigation: Use the data only for the user's stated procurement or market-analysis task, avoid bulk export or outreach misuse, and preserve any server-side masking rather than trying to enrich masked contacts.

Risk: API keys can be exposed if echoed into conversation or request examples.

Mitigation: Read keys from ZLBX_API_KEY or local agent configuration, do not ask users to paste keys into chat, and never display the key in responses.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bailianai/skills/tender-jiangsu)
- [Zhiliaobiaoxun Homepage](https://ai.zhiliaobiaoxun.com/?ch=s151)
- [API Overview](artifact/SKILL.md)
- [Tender Search API Details](artifact/references/api-search.md)
- [Company Analysis API Details](artifact/references/api-company.md)
- [Market Analysis API Details](artifact/references/api-market.md)
- [Account Query API Details](artifact/references/api-account.md)
- [Automatic Registration Flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON request examples, shell snippets, and tabular summaries when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved automatic registration; may store an API key in ~/.zlbx/config.json after consent.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
