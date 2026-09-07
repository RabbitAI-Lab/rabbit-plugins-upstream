## Description:

Produces company-intelligence reports from a bidding and procurement perspective, covering business profile, customer and supplier relationships, bidding strength, competitors, public-risk checks, and optional single-company or two-company comparison reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business analysts use this skill to assess a company's business direction, procurement footprint, customer base, competitive overlap, and public-risk signals using ZLBX/知了标讯 bidding data and referenced public sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores the ZLBX API key locally in ~/.zlbx/config.json when automatic registration is used.

Mitigation: Protect that file as a credential, remove it when the service is no longer needed, or use a managed ZLBX_API_KEY environment variable instead.

Risk: Generated HTML reports and returned company or notice links may contain signed no-login access parameters.

Mitigation: Treat generated reports and sk-bearing links as sensitive business material and avoid broad forwarding or publication.

Risk: Reports can include contact phone numbers in the form returned by the service.

Mitigation: Review reports before sharing, keep masked contacts masked, and avoid supplementing or bulk-exporting contact details.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/company-intel-qichamao)
- [Publisher Profile](https://clawhub.ai/user/dragonzu)
- [API Quick Reference](references/api-quick.md)
- [Seven-Step Workflow](references/workflow.md)
- [Report Template](references/report-template.md)
- [Automatic Registration Flow](references/auto-register.md)
- [ZLBX API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZLBX Skill Documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown report in conversation plus optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs cite supporting bidding records and public sources when available; generated HTML reports may include signed no-login links returned by the service.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
