## Description:

Helps agents query and analyze construction and municipal tendering data, including bid notices, awards, project timelines, company profiles, competitors, market rankings, price trends, account balance, and remaining quota.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and summarize construction and municipal procurement opportunities, bid outcomes, company tender histories, competitor signals, and market statistics from the ZLBX tender-data APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-run login flow can read hardware-derived device characteristics and send a MAC hash to the vendor for trial de-duplication.

Mitigation: Use an already provisioned ZLBX_API_KEY from trusted secret management when possible; if auto-registration is needed, require explicit user consent before collecting device characteristics.

Risk: The skill can persist an API key in ~/.zlbx/config.json.

Mitigation: Treat the stored key as a secret, restrict filesystem access to the config file, and prefer managed environment secrets for shared or production environments.

Risk: Recharge or auto-login links may be printed and usable by anyone before expiration.

Mitigation: Share these links only in trusted contexts, avoid logging them, and rotate or invalidate access if a link is exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bailianai/skills/tender-construction)
- [ZLBX service homepage](https://ai.zhiliaobiaoxun.com/?ch=s155)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown responses with API request guidance, JSON examples, tabular summaries, and optional shell commands for first-run registration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a local ~/.zlbx/config.json API key; first-run auto-registration requires user consent before collecting device characteristics.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
