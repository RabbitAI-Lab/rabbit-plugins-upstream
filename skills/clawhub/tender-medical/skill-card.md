## Description:

面向医疗卫生招投标场景，帮助代理查询招标、中标、拟建与临期项目、企业工商和联系人信息，并生成市场、价格和竞争分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

External business users, procurement teams, sales teams, and developers use this skill to query Chinese tender data for medical and healthcare opportunities, supplier research, account checks, and market trend analysis. It helps an agent return concise result summaries, tables, API-backed analyses, and next-step guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate an account registration flow that uses device fingerprinting and stores an API credential in ~/.zlbx/config.json.

Mitigation: Prefer manually setting ZLBX_API_KEY when possible; if automatic registration is used, require user consent first and review any credential written to ~/.zlbx/config.json.

Risk: Auto-login recharge links can grant account access if shared outside the user's intended session.

Mitigation: Treat generated auto-login links as sensitive and avoid sharing them in public logs, tickets, or transcripts.

Risk: Company contact lookup may expose business contact data and can be misused for bulk harvesting.

Mitigation: Use contact lookup only for legitimate business purposes, respect masked contact responses, and avoid bulk export or enrichment of contact details.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bailianai/skills/tender-medical)
- [ZhiLiao BiaoXun Service Portal](https://ai.zhiliaobiaoxun.com/?ch=s154)
- [API Search Reference](references/api-search.md)
- [API Company Reference](references/api-company.md)
- [API Market Reference](references/api-market.md)
- [API Account Reference](references/api-account.md)
- [Auto-Registration Reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with tables, JSON request examples, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a user-approved auto-registration flow; contact details may be masked for free or trial accounts.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
