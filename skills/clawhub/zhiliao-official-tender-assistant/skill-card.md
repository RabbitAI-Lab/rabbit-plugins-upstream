## Description:

Helps agents search Chinese tender and award notices, inspect companies, analyze competitors, summarize market trends, and query account usage through the Zhiliao Biaoxun API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business analysts use this skill to find procurement opportunities, review tender outcomes, inspect supplier and buyer profiles, and compare competitors or market activity. Developers can also use it as REST API guidance for authenticated Zhiliao Biaoxun workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create accounts automatically, use device-derived trial deduplication, and store API keys locally.

Mitigation: Review the account setup flow before installation, require user consent before device metadata is collected, and prefer providing ZLBX_API_KEY through a trusted secret mechanism.

Risk: The skill may print login-token links or append promotional or server-controlled messages in responses.

Mitigation: Review generated links and appended messages before sharing externally, and avoid exposing account recovery or recharge links in public transcripts.

Risk: Tender, company, contact, and market outputs depend on authenticated vendor API responses and may include masked or incomplete fields.

Mitigation: Tell users when data is masked or unavailable, avoid reconstructing masked contact data from other sources, and verify high-impact procurement decisions against primary records.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-official-tender-assistant)
- [Tender search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples and REST call instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or an approved account setup flow before authenticated data queries.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
