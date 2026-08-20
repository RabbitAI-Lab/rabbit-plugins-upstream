## Description:

This skill helps agents produce Chinese enterprise due diligence reports from bidding and tendering data, including business profile, customers and suppliers, award history, competitors, public risk notes, and an optional local HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business teams use this skill to review a company from a bidding and tendering perspective before supplier checks, competitor analysis, customer background checks, or light due diligence. The agent resolves company identity, queries ZLBX enterprise and tender data, summarizes evidence-backed findings, and can generate a shareable local HTML report.

### Deployment Geography for Use:

Global, subject to availability of ZLBX services and Chinese-language bidding data coverage.

## Known Risks and Mitigations:

Risk: The skill stores a ZLBX API key in local configuration when auto-registration succeeds.

Mitigation: Use a preconfigured ZLBX_API_KEY where possible, do not paste API keys into chat, and review ~/.zlbx/config.json handling before deployment.

Risk: Optional free-trial registration sends a hashed MAC-derived device signal.

Mitigation: Keep the documented consent gate before registration and limit collected device features to platform, architecture, and hashed MAC only.

Risk: Generated reports can include signed sk links and possibly contact phone data.

Mitigation: Treat generated Markdown and HTML reports as sensitive, avoid broad forwarding, and do not attempt to reconstruct masked contact details.

Risk: The server security verdict requires review before deployment.

Mitigation: Review the skill and scan results before enabling it in environments that handle business-sensitive due diligence workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-company-intel)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Workflow guide](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration flow](artifact/references/auto-register.md)
- [ZLBX API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZLBX AI platform](https://ai.zhiliaobiaoxun.com/?ch=s107)
- [ZLBX business intelligence platform](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance]

**Output Format:** [Markdown report in the agent conversation, with an optional self-contained HTML report file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-gated free-trial registration; generated reports may include signed sk links and optional contact phone data.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
