## Description:

Generates Chinese-language company background-check reports from bid and tender data, including business profile, customers and suppliers, bid-winning strength, competitors, public risk signals, and optional side-by-side company comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business teams use this skill to investigate a named company before cooperation, supplier review, customer validation, competitor research, or light due diligence. The skill can produce a single-company report or compare two companies using bid/tender records and source-linked public information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create a vendor trial account and send a hashed device identifier when no API key is configured.

Mitigation: Preconfigure ZLBX_API_KEY to avoid auto-registration, or require explicit user consent before registration and confirm only platform, CPU architecture, and MAC hash are sent.

Risk: The skill may persist credentials and generated reports on disk.

Mitigation: Store API keys only in the documented local config or environment, never echo credentials in chat, and review local report files before retaining or sharing them.

Risk: Generated reports and HTML exports can include signed platform links or contact information.

Mitigation: Review exported Markdown and HTML before sharing, avoid public redistribution of signed links, and use contact lookup only for legitimate business purposes.

Risk: Company background-check conclusions can be misleading or reputationally sensitive if data gaps or public-risk signals are overstated.

Mitigation: Use source-linked factual statements, separate facts from inference, document data boundaries, and avoid definitive accusations or unsupported judgments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/company-background-check)
- [API Quick Reference](artifact/references/api-quick.md)
- [Seven-Step Workflow Manual](artifact/references/workflow.md)
- [Report Template](artifact/references/report-template.md)
- [Auto-Registration Flow](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Chinese Markdown report in chat, with optional self-contained HTML report file generated from structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based trial registration; outputs should include source links, data boundaries, and an absolute path for generated HTML reports.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
