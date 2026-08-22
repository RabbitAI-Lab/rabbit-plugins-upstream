## Description:

A supplier due diligence agent skill that uses Zhiliaobiaoxun tender and bidding data to assess supplier qualifications, fulfillment history, customer relationships, public risk signals, and side-by-side supplier comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement teams, buyers, tender owners, contractors, and business users use this skill to investigate a supplier or compare two candidate suppliers before qualification, onboarding, or cooperation decisions. It produces source-backed supplier intelligence reports from bidding records, public risk checks, and optional contact lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or use a local provider account and store an API key in the user's home directory.

Mitigation: Prefer a user-supplied ZLBX_API_KEY where possible, require explicit consent before auto-registration, and protect or remove ~/.zlbx/config.json when credentials should not persist.

Risk: Generated reports may include signed company, announcement, or auto-login style links.

Mitigation: Review generated Markdown and HTML reports for signed URLs before redistributing them outside the intended audience.

Risk: Supplier reports can influence real procurement or partnership decisions and may include public risk information about named organizations.

Mitigation: Use the report as reference material only, keep facts and inferences separate, preserve source links, and confirm important findings through authoritative channels before acting.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/supplier-qualification-checker)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Workflow reference](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Auto-registration reference](references/auto-register.md)
- [Zhiliaobiaoxun API endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})
- [Zhiliaobiaoxun AI Open Platform](https://ai.zhiliaobiaoxun.com/?ch=s117)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown supplier due diligence report with optional self-contained HTML report and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-gated auto-registration; may write generated HTML reports locally and may store an API key in ~/.zlbx/config.json.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
