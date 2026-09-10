## Description:

Helps sales and BD users produce procurement-focused customer background reports from public bidding records, supplier relationships, competitor overlap, and cited public-risk checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, BD, procurement, and competitive-intelligence users use this skill before customer visits, bids, or commercial outreach to understand an organization's purchasing history, budget scale, supplier landscape, competitors, and public risk signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names and query terms are sent to the vendor API for procurement and bidding analysis.

Mitigation: Use the skill only when this vendor data flow is acceptable, and disclose the expected data source and cost before beginning a report.

Risk: Trial signup can collect a MAC-derived hash and other minimal device attributes.

Mitigation: Run automatic signup only after explicit user consent, collect only the documented minimal attributes, and allow a preconfigured API key to skip signup.

Risk: The skill stores an API key locally for later use.

Mitigation: Do not expose API keys in chat or reports; prefer environment configuration where available and keep local credential files outside generated report outputs.

Risk: Generated HTML reports can include signed no-login company or announcement links.

Mitigation: Share generated reports only with trusted recipients and review signed-link handling before external distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/client-background-check)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [Seven-step workflow](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Automatic registration flow](artifact/references/auto-register.md)
- [Report template](artifact/references/report-template.md)
- [ZLBX API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZLBX signup and account portal](https://ai.zhiliaobiaoxun.com/?ch=s127)
- [ZLBX business intelligence portal](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with optional self-contained HTML report files and concise follow-up guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-gated account setup; generated HTML reports may be written under ~/zlbx-company-intel-files/.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
