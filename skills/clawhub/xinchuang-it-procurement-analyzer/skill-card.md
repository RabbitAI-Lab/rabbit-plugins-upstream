## Description:

Analyzes Chinese Xinchuang and IT procurement data for bid search, market share, historical pricing, company competition, supplier discovery, and digital-government procurement trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement analysts, IT vendors, and systems integrators use this skill to search Chinese bid notices, compare IT brands and prices, analyze competitors and customers, and identify potential suppliers or renewal opportunities.

### Deployment Geography for Use:

Global, for users analyzing China-focused procurement data.

## Known Risks and Mitigations:

Risk: The default onboarding path can create a third-party account, send a hashed device identifier, and store an API key under ~/.zlbx/config.json.

Mitigation: Review the skill before installing; prefer manually setting ZLBX_API_KEY and avoid auto-registration unless the user accepts device deduplication and local credential persistence.

Risk: The skill can generate account login or recharge links when quota is exhausted.

Mitigation: Confirm that links point to the expected zhiliaobiaoxun domain and use manual login/recharge when automatic account flows are not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/xinchuang-it-procurement-analyzer)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Skill definition](artifact/SKILL.md)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Auto-registration workflow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON request examples, API result summaries, and occasional shell-command or configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include procurement analysis, API request payloads, recharge or account guidance, and local credential configuration details.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
