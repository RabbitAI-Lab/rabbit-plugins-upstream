## Description:

This skill helps an agent produce procurement-based company intelligence reports covering bid-winning history, performance evidence, customer and supplier relationships, competitors, and public-risk findings for one or two companies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, procurement teams, and sales teams use this skill to evaluate a company's bid-winning track record, contract-performance evidence, customer ecosystem, competitive overlap, and publicly sourced risk signals. It supports single-company due diligence and two-company comparison reports based on ZhiLiao BiaoXun procurement data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use device-based trial registration when no API key is configured.

Mitigation: Require explicit user consent before registration and prefer a preconfigured ZLBX_API_KEY when users want to avoid auto-registration.

Risk: The skill may persist an API key in local plaintext configuration.

Mitigation: Use environment-variable configuration where possible and restrict access to any local credential file.

Risk: Generated reports may contain provider-signed links and local HTML exports with sensitive business context.

Mitigation: Store reports in a private directory and treat exported HTML files and sk-bearing links as sensitive material.

Risk: Optional contact lookups can expose project contact phone data.

Mitigation: Only perform contact lookups when needed, preserve provider masking, and avoid re-identifying or bulk exporting contact details.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/bid-winner-company-profile)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [API quick reference](references/api-quick.md)
- [Company intelligence workflow](references/workflow.md)
- [Report template](references/report-template.md)
- [Auto-registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report plus an optional local HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include source citations where available; exported HTML can contain provider-signed links and should be handled as sensitive.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
