## Description:

Helps agents produce Chinese company-intelligence reports from Zhiliaobiaoxun tender and bidding data, covering company profiles, business keywords, customers and suppliers, bidding strength, competitors, public-risk checks, and optional HTML output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and agents use this skill to analyze a named company or compare two companies through tender and bidding records, public-risk searches, and generated report outputs. It is intended for company due diligence, supplier review, competitor monitoring, and bidding-market intelligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated chat and HTML reports can contain signed provider links that may bypass normal login checks.

Mitigation: Treat generated reports and signed links as sensitive; share them only with recipients who should have access.

Risk: The skill can expose company contact data and business-relationship details returned by the provider.

Mitigation: Use the returned contact data only in the intended report context, preserve any provider masking, and avoid forwarding reports beyond the intended audience.

Risk: Using the skill requires a provider API key and may spend provider credits.

Mitigation: Confirm the configured key and expected credit use before running company reports, especially for comparison or contact lookups.

Risk: The skill may save an API key under ~/.zlbx/config.json during account setup.

Mitigation: Prefer a preconfigured ZLBX_API_KEY when local key persistence is not desired, and protect any saved configuration file as a credential.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/company-intel-qichamao)
- [Workflow guide](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Auto-registration guide](references/auto-register.md)
- [Zhiliaobiaoxun API endpoint pattern](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})
- [Zhiliaobiaoxun AI platform](https://ai.zhiliaobiaoxun.com/?ch=s116)
- [Zhiliaobiaoxun business intelligence platform](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown company-intelligence reports with optional self-contained HTML report files and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local report files, consume provider credits, use WebSearch for public-risk checks, and include provider-returned signed links in reports.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
