## Description:

IT信息化商机雷达 helps users find early IT, Xinchuang, digital government, software, cloud, data center, cybersecurity, and smart-city project opportunities from proposed projects, procurement intentions, and expiring service contracts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business development, sales, and market research users use this skill to scan China-focused IT public procurement signals, rank opportunity leads by value and timing, and generate follow-up guidance and shareable opportunity reports.

### Deployment Geography for Use:

Global, with China-focused public procurement data coverage.

## Known Risks and Mitigations:

Risk: Generated reports and provider-returned links may include sk or auto-login parameters that should be treated as confidential.

Mitigation: Share reports only with intended recipients, avoid posting generated links publicly, and redact signed parameters before broad distribution.

Risk: Auto-registration can send a hashed MAC-derived identifier to the provider and store a persistent API credential locally.

Mitigation: Use a preconfigured ZLBX_API_KEY when possible, decline auto-registration if device-derived identifiers are not acceptable, and review ~/.zlbx/config.json permissions.

Risk: Scheduled or repeated scans can disclose search terms to the provider and consume account balance.

Mitigation: Review scan scope, frequency, and call budget before scheduling recurring reports.

Risk: Opportunity reports may influence outreach or commercial decisions based on public procurement data that can be incomplete or delayed.

Mitigation: Verify API-returned amounts, dates, organizations, and statuses before acting, and keep compliance disclaimers with shared reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/it-project-opportunity-radar)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [Workflow guide](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Auto-registration flow](references/auto-register.md)
- [Report template](references/report-template.md)
- [ZhiLiaoBiaoXun API endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名})
- [ZhiLiao business opportunity platform](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Markdown opportunity lead reports in chat, with optional self-contained HTML report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved auto-registration; generated reports may include provider-returned signed links and are saved under ~/zlbx-opportunity-radar-files/ when HTML export is used.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
