## Description:

This skill helps agents produce procurement and bidding competitor intelligence reports for a named company, including market position, customer and supplier ecosystem, bidding strength, competitors, public risk signals, and optional company comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to evaluate competitors, suppliers, or counterparties through public bidding data. It supports single-company intelligence reports, two-company comparisons, and ongoing competitor monitoring summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The provider receives company names, regions, keywords, and other query criteria used for business intelligence lookups.

Mitigation: Use the skill only for queries the user or organization is comfortable sending to the provider, and avoid adding sensitive strategy details to lookup terms.

Risk: Automatic free-trial registration can create a stable MAC-derived device hash and store an API key in ~/.zlbx/config.json.

Mitigation: Prefer a preconfigured ZLBX_API_KEY to skip auto-registration, require explicit user consent before registration, and check local config file permissions after use.

Risk: Generated HTML reports and provider-returned sk links can carry access-bearing report or platform URLs.

Mitigation: Treat generated reports and signed links as sensitive, share them only with intended recipients, and avoid broad redistribution.

Risk: The security summary flags unsafe HTML link rendering in generated reports.

Mitigation: Review generated report content and links before distribution, and open reports only when they come from a trusted run of the skill.

Risk: Reports discuss real companies and public risk signals, which can create reputational or decision-making risk if phrased as unsupported conclusions.

Mitigation: Keep public-risk sections factual, source-linked, and non-accusatory; separate facts from inferences and preserve the report disclaimer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/competitor-intel-analysis)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Workflow guide](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Automatic registration flow](artifact/references/auto-register.md)
- [ZhiLiao Biaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZhiLiao Biaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports plus optional self-contained HTML reports, with structured API-call guidance and local configuration steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports may include provider-returned signed links and a capped citations appendix; HTML reports are written to a local output directory.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
