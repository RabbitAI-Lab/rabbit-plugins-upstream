## Description:

An agent skill that helps users perform bid-data-driven company due diligence before investment, acquisition, partnership, or contracting decisions by producing single-company or two-company comparison reports from public tender and award records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business, procurement, investment, and partnership reviewers use this skill to check a company's operating reality through public bid-award history, customer and supplier patterns, competitors, and public risk signals. It supports single-company due diligence and two-company comparison reports with cited sources and data-boundary notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names and related queries are sent to Zhiliaobiaoxun APIs for due diligence lookups.

Mitigation: Use the skill only when sharing those business queries with Zhiliaobiaoxun is acceptable, and avoid including unnecessary sensitive context in company lookup prompts.

Risk: The optional trial signup sends a hashed device identifier and stores the resulting API key in ~/.zlbx/config.json.

Mitigation: Preconfigure ZLBX_API_KEY to skip auto-registration, and review local credential storage practices before deployment.

Risk: Generated reports can preserve signed platform links that provide direct access to returned company or announcement pages.

Mitigation: Treat Markdown and HTML reports as sensitive business artifacts and share them only with intended recipients.

Risk: The skill may retrieve project contacts when explicitly requested.

Mitigation: Request contacts only when needed, preserve the platform-provided masking, and do not enrich masked contact details from other sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/bidding-due-diligence)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Workflow reference](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration reference](artifact/references/auto-register.md)
- [Zhiliaobiaoxun AI platform](https://ai.zhiliaobiaoxun.com/?ch=s126)
- [Zhiliaoshangji platform](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [Markdown, HTML, Guidance, Configuration]

**Output Format:** [Markdown report in conversation plus optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include source links, data-boundary notes, cost estimates, and disclaimers; HTML reports may contain signed platform links returned by the API.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
