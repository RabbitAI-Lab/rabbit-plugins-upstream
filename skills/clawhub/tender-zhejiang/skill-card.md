## Description:

This skill helps agents query and analyze Zhejiang-focused tender, award, company, market, and account data through Zhiliaobiaoxun APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement analysts, sales teams, and agents use this skill to search Zhejiang tender opportunities, review award histories, inspect company tender records, and summarize market trends. The Zhejiang region is a default search focus and can be overridden by the user's requested scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement and company queries are sent to Zhiliaobiaoxun APIs.

Mitigation: Install and use the skill only when this external API use is acceptable for the intended tender, company, and market queries.

Risk: First-use onboarding can create a remote account, send limited device features, and save an API key in ~/.zlbx/config.json.

Mitigation: Configure ZLBX_API_KEY before use to avoid device-based auto-registration, and review or remove ~/.zlbx/config.json when the saved key is no longer wanted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bailianai/skills/tender-zhejiang)
- [Zhiliaobiaoxun homepage](https://ai.zhiliaobiaoxun.com/?ch=s152)
- [Search API reference](artifact/references/api-search.md)
- [Company API reference](artifact/references/api-company.md)
- [Market API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Auto-registration flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON request examples and REST/API call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read ZLBX_API_KEY or ~/.zlbx/config.json; first-use auto-registration requires user consent and may save an API key locally.]

## Skill Version(s):

1.0.1 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
