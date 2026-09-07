## Description:

Generates Chinese company background-check reports from Zhiliaobiaoxun bidding data, covering business profile, customers and suppliers, winning-bid strength, competitors, public-risk signals, and optional company comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Business, procurement, sales, and compliance users use this skill to assess a named company from a bidding-data perspective. It helps compare companies, review supplier or partner background, identify bidding competitors, and generate a shareable HTML intelligence report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create or use a Zhiliaobiaoxun account and collect a persistent hashed MAC-derived device identifier for free-trial deduplication.

Mitigation: Proceed only after explicit user consent for auto-registration, and prefer a preconfigured ZLBX_API_KEY when users want to skip device-feature collection.

Risk: The skill stores an API key in ~/.zlbx/config.json when auto-registration succeeds.

Mitigation: Treat the local config file as a credential store and avoid exposing its contents in prompts, reports, logs, or shared artifacts.

Risk: Generated reports and raw API-returned sk links can provide signed login-bypass access to report-related resources.

Mitigation: Share generated HTML reports and sk links only with the intended audience, and preserve the skill's warnings about not distributing those links broadly.

Risk: Company background reports can be incomplete or misread as definitive judgments about real organizations.

Mitigation: Keep conclusions tied to cited public bidding data and source links, retain data-boundary disclaimers, and avoid unsupported accusations or categorical risk labels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/company-background-check)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Workflow guide](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Auto-registration flow](references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun AI platform](https://ai.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown report plus a generated self-contained HTML report file; may include JSON-shaped report data for rendering.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based auto-registration; reports may include signed sk links returned by the service.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
