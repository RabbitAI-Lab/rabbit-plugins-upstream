## Description:

Helps agents find early medical procurement opportunities by scanning hospital construction projects, procurement intentions, and expiring service or maintenance contracts, then ranking leads by value and urgency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and sales or business-development agents use this skill to discover early hospital and public-health procurement leads for medical equipment, consumables, diagnostics, maintenance services, and hospital IT. The skill turns a product line and region into a ranked opportunity list with follow-up guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may store API credentials in ~/.zlbx/config.json and write generated HTML reports under ~/zlbx-opportunity-radar-files/.

Mitigation: Review the skill before installing, provide a user-managed ZLBX_API_KEY where possible, and treat generated reports as sensitive local files.

Risk: Auto-registration sends a hashed device identifier to the provider.

Mitigation: Use a preconfigured ZLBX_API_KEY to bypass auto-registration, or require explicit user consent before registration.

Risk: Provider-returned links can contain signed sk parameters that grant access to reports or procurement details.

Mitigation: Do not forward generated reports or signed links unless sharing that access is intentional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/medical-equipment-opportunity-radar)
- [Workflow guide](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Auto-registration flow](references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})
- [Zhiliaobiaoxun registration and account portal](https://ai.zhiliaobiaoxun.com/?ch=s103)
- [Zhiliaobiaoxun opportunity portal](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, HTML files, guidance]

**Output Format:** [Markdown opportunity lists in conversation, with optional self-contained HTML reports saved as local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include ranked leads, data gaps, next-step recommendations, citations or source notes, and sensitive signed links when returned by the provider API.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
