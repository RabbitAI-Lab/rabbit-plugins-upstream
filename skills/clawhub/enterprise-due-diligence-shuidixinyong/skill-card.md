## Description:

Provides a lightweight pre-cooperation enterprise due-diligence workflow using Zhiliaobiaoxun tender and bidding data to produce business activity, customer and supplier, bid strength, competitor, and public-risk reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Business, procurement, sales, and partnership users use this skill before cooperation, contracting, or credit-period decisions to assess a company's observable business activity, project履约 history, customer concentration, competitive landscape, and publicly sourced risk signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can collect a device fingerprint for auto-registration when no API key is configured.

Mitigation: Prefer a preconfigured ZLBX_API_KEY or local config API key; if auto-registration is needed, require explicit user consent before collecting platform, architecture, and hashed MAC details.

Risk: API credentials are stored locally for reuse.

Mitigation: Treat ~/.zlbx/config.json as sensitive, avoid sharing credential values in conversation, and rotate or remove the key if the environment is shared.

Risk: Generated HTML reports can preserve signed links and business-sensitive retrieved data.

Mitigation: Share generated reports only with intended recipients and review embedded company, announcement, signed access, and contact information before redistribution.

Risk: Due-diligence outputs may be mistaken for definitive judgments about a real company.

Mitigation: Keep conclusions tied to cited public data, state data boundaries and gaps, avoid unsupported risk labels, and require the user to make their own cooperation or credit decision.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/dragonzu/skills/enterprise-due-diligence-shuidixinyong)
- [Enterprise intelligence workflow](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Auto-registration flow](references/auto-register.md)
- [Zhiliaobiaoxun main agent site](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report plus a self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY; reports may include signed source links, public-risk source URLs, and contact data returned by the service.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
