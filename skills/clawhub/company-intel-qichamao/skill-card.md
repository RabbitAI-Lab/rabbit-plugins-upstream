## Description:

Provides company intelligence reports from a procurement and bidding perspective, covering company profile, business keywords, customer and supplier relationships, bid history, competitive overlap, public-risk checks, and optional contacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and agents use this skill to produce single-company due-diligence reports or two-company comparisons based on public bidding data, company profiles, partner relationships, competitive overlap, and sourced public-risk signals.

### Deployment Geography for Use:

Global; data usefulness depends on Zhiliaobiaoxun's public procurement and bidding data coverage.

## Known Risks and Mitigations:

Risk: The skill can create an account using hashed device identifiers when no API key is configured.

Mitigation: Require explicit user consent before registration, disclose the three collected device features, and skip registration entirely when ZLBX_API_KEY or a local key is already configured.

Risk: The skill may store an API key in a local configuration file.

Mitigation: Treat the local key as a credential, avoid printing it in conversation, and prefer preconfigured environment credentials where available.

Risk: Generated HTML reports and platform URLs may contain signed login-bypass links.

Mitigation: Treat reports and sk links as sensitive and share them only with intended recipients.

Risk: Company reports may include public-risk statements and contact details returned by the API.

Mitigation: Keep risk language factual and sourced, preserve contact masking exactly as returned, and request contact details only with a legitimate business and compliance basis.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/company-intel-qichamao)
- [API Quick Reference](references/api-quick.md)
- [Seven-Step Workflow](references/workflow.md)
- [Report Template](references/report-template.md)
- [Automatic Registration Flow](references/auto-register.md)
- [Zhiliaobiaoxun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名})
- [Zhiliaobiaoxun Agent Portal](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, html, shell commands, configuration, guidance]

**Output Format:** [Markdown report in the agent conversation, with optional self-contained HTML report file and concise operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved automatic registration; generated reports may include signed platform links and contact information returned by the API.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
