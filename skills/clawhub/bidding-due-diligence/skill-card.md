## Description:

Helps agents produce procurement and tendering due-diligence reports on companies, using Zhiliaobiaoxun bid data to summarize business profile, contract activity, customers, competitors, and linked public risk information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business teams use this skill to investigate a company before investment, M&A, partnership, supplier selection, or contract signing. It produces single-company or two-company comparison reports grounded in bid records, company relationships, and cited public risk information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company queries are sent to Zhiliaobiaoxun services.

Mitigation: Install only if this data sharing is acceptable for the intended due-diligence workflow.

Risk: Automatic trial registration may use a MAC-derived device hash and may store an API key in ~/.zlbx/config.json.

Mitigation: Prefer configuring a user-provided ZLBX_API_KEY when available, and review local credential handling before deployment.

Risk: Generated HTML reports may include signed access links and contact information.

Mitigation: Review reports before sharing and enable contact lookup only when there is a legitimate need.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/bidding-due-diligence)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [API quick reference](references/api-quick.md)
- [Seven-step workflow](references/workflow.md)
- [Report template](references/report-template.md)
- [Auto-registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report with optional self-contained HTML export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include cited bid records, signed access links, data-boundary notes, and optional contact information returned by the service.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
