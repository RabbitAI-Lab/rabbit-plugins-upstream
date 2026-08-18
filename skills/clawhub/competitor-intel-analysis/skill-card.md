## Description:

Provides bid-market competitor intelligence reports for a company, including business focus, award strength, major customers, real co-bid competitors, public-risk notes, and optional two-company comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams, sales analysts, procurement reviewers, and business-development staff use this skill to understand a named company's tendering footprint, customers, competitors, and public risk signals before bidding, partnering, or monitoring competitors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The vendor receives company search terms and bid-analysis queries.

Mitigation: Use the skill only for queries the user is comfortable sending to the vendor API, and avoid entering confidential strategy, trade-secret, or non-public deal information.

Risk: Automatic trial setup may use a consented hashed device identifier for free-quota de-duplication.

Mitigation: Require explicit user consent before automatic registration, disclose the three collected non-identity device attributes, and let users bypass registration with a preconfigured ZLBX_API_KEY.

Risk: Credentials and generated reports may be stored on disk.

Mitigation: Keep API keys out of chat transcripts, protect local configuration files, and treat generated report files as sensitive business documents.

Risk: Exported HTML reports may include contact details and tokenized platform links.

Mitigation: Share exported reports only with intended recipients, avoid public forwarding, and redact sensitive links or contact sections when broad distribution is needed.

Risk: Competitor reports about real companies can create reputational or decision-making risk if interpreted as definitive findings.

Mitigation: Present conclusions as public-data signals, cite supporting records, preserve data-boundary disclaimers, and avoid unsupported accusations or legal-risk labels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/competitor-intel-analysis)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Workflow guide](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Automatic registration flow](references/auto-register.md)
- [HTML report renderer](scripts/render_report.py)
- [ZhiLiaoBiaoXun agent site](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report text with optional self-contained HTML report files and concise setup guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY or consented automatic trial setup; may store an API key under ~/.zlbx/config.json and reports under ~/zlbx-company-intel-files/.]

## Skill Version(s):

1.0.1 (source: server release evidence, released 2026-08-13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
