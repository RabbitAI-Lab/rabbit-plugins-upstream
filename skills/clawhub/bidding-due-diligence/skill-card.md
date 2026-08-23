## Description:

This skill helps agents produce company due-diligence reports from public bidding data, covering award history, customer concentration, competitors, and public risk signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business analysts use this skill to assess a company before investment, acquisition, partnership, or contracting by generating single-company or two-company bidding due-diligence reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create an account, send a hashed device identifier, and store an API key locally.

Mitigation: Use a preconfigured ZLBX_API_KEY when possible; otherwise require explicit user consent before automatic registration and review local credential storage.

Risk: Generated reports can be durable local files and may contain signed access links.

Mitigation: Review report contents before sharing and distribute generated HTML or signed links only to intended recipients.

Risk: Company names and query terms are sent to the ZLBX service for analysis.

Mitigation: Use the skill only when sharing those business queries with ZLBX is acceptable and avoid adding unnecessary confidential deal details.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/bidding-due-diligence)
- [Publisher Profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Workflow Guide](references/workflow.md)
- [API Quick Reference](references/api-quick.md)
- [Report Template](references/report-template.md)
- [Auto-Register Flow](references/auto-register.md)
- [ZLBX API Endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})
- [ZLBX Account Portal](https://ai.zhiliaobiaoxun.com/?ch=s126)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown report plus self-contained HTML report file; may use structured JSON for report rendering.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved automatic registration; generated reports can include signed access links.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
